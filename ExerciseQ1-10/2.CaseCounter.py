"""
Letter Case Counter Function

Objective:
Write a function named 'case_counter' that counts the number of uppercase and lowercase letters in a given string.

Function Parameter:
text (string): The string in which the letters need to be counted.

Instructions:
- The function should calculate and print two numbers: the count of uppercase letters and the count of lowercase letters in the string.
- If there are no letters of a particular case (uppercase or lowercase) in the string, the function should print 0 for that case.
- Non-alphabetic characters in the string should be ignored and not counted.

Example Test Cases:
1. case_counter("Hello World!") should print the counts of uppercase and lowercase letters.
2. case_counter("PYTHON") should print the counts of uppercase and lowercase letters.
3. case_counter("python") should print the counts of uppercase and lowercase letters.
4. case_counter("1234!@#$") should print 0 for both counts.
"""


def case_counter(text):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in text:
        if c.isupper():
            d["UPPER_CASE"] += 1
        if c.islower():
            d["LOWER_CASE"] += 1

    print("Original word: ",text)
    print("Number of Uppecase letter: ",d["UPPER_CASE"])
    print("Number of Lowercase letter: ",d["LOWER_CASE"])

print(case_counter("Hello World!"))
print(case_counter("PYTHON"))
print(case_counter("python"))
print(case_counter("1234!@#$"))

       
# Your code goes here
# Remember to count uppercase and lowercase letters and ignore non-alphabetic characters
# Delete this after implementing some code inside this function.


# Test cases
case_counter("Hello World!")  # Expected: Uppercase letters: 2, Lowercase letters: 8
case_counter("PYTHON")  # Expected: Uppercase letters: 6, Lowercase letters: 0
case_counter("python")  # Expected: Uppercase letters: 0, Lowercase letters: 6
case_counter("1234!@#$")  # Expected: Uppercase letters: 0, Lowercase letters: 0
