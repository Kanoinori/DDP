"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.
2. r (float): Annual interest rate in decimal.
3. n (integer): Number of times interest is compounded per year.
4. t (integer): Number of years for investment.

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""


def compound_interest_calculator(P, r, n, t):
    # Your code goes here
    # Implement the compound interest calculation
    final_value = (P * (1 + (r / n))) ** (n * t)
    print(f"{final_value} after {t} years")
 # Delete this after implementing some code inside this function


# Test cases
compound_interest_calculator(1000, 0.05, 12, 5)  # Expected: Amount after 5 years
compound_interest_calculator(500, 0.07, 4, 10)  # Expected: Amount after 10 years
compound_interest_calculator(1500, 0.03, 6, 7)  # Expected: Amount after 7 years