from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# database initialise
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                student_id TEXT NOT NULL
            )
        ''')
        conn.commit()

    with sqlite3.connect('orders.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                number_of_people INTEGER NOT NULL,
                table_type TEXT NOT NULL,
                music_artist TEXT,
                contact_phone TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')
        conn.commit()

# user login
def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
        user = cursor.fetchone()
        return user

# user register
def register_user(username, password, student_id):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password, student_id) VALUES (?, ?, ?)', (username, hashed_password, student_id))
        conn.commit()

# make a reservation
@app.route('/reserve', methods=['GET', 'POST'])
def reserve():

    if request.method == 'POST':
        user_id = request.form['user_id']
        date = request.form['date']
        time = request.form['time']
        number_of_people = request.form['number_of_people']
        table_type = request.form['table_type']
        music_artist = request.form.get('music_artist', None)
        contact_phone = request.form['contact_phone']

        # validation
        if not (date and time and number_of_people and table_type and contact_phone):
            flash('Please fill in all mandatory fields.', 'error')
        else:
            # Save reservation to the database
            with sqlite3.connect('orders.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO orders (user_id, date, time, number_of_people, table_type, music_artist, contact_phone) VALUES (?, ?, ?, ?, ?, ?, ?)',
                               (1, date, time, number_of_people, table_type, music_artist, contact_phone))
                conn.commit()

            flash('Reservation successful!', 'success')
            return redirect(url_for('index'))

    return render_template('reserve.html')

# view existing reservations
@app.route('/reservations')
def view_reservations():
    with sqlite3.connect('orders.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders WHERE user_id=?', ((1,)))
        reservations = cursor.fetchall()
    return render_template('reservations.html', reservations=reservations)

# index page
@app.route('/')
def index():
    return render_template('index.html')

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = login_user(username, password)

        if user:
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your username and password.', 'error')

    return render_template('login.html')

# register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        student_id = request.form['student_id']

        # Check if the user exists
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username=?', (username,))
            existing_user = cursor.fetchone()

        if existing_user:
            flash('Username already exists. Please choose another username.', 'error')
        else:
            # Register this user
            register_user(username, password, student_id)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

# menu Page
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
