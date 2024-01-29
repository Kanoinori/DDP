def morse_translator(input_string):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    }

    input_string = input_string.upper()
    translated_string = []

    for word in input_string.split():
        morse_word = []
        for char in word:
            if char.isalpha():
                morse_word.append(morse_code_dict[char])
        translated_string.append(' '.join(morse_word))

    return '/'.join(translated_string)

# Example usage:
input_string = "Hello World"
result = morse_translator(input_string)
print(result)