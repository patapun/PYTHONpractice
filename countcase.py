"""
Write a Python function named case_counter that counts the number of uppercase and lowercase letters in a given string.

The function should calculate and return two numbers: the count of uppercase letters and the count of lowercase letters in the string.
If there are no letters of a particular case (uppercase or lowercase) in the string, the function should return 0 for that case.
Non-alphabetic characters in the string should be ignored and not counted.
"""
#Dont forget def is the main, you have to inline print at inner paragraph
#s here is string
#d is what we determine to start counting case at 0
#for c in s means for case in string
#c.isupper is function text.isupper 
# d["UPPER_CASE"] += 1 mean UPPER_CASE = 0+1

def case_counter(s):
    d = {"UPPER_CASE": 0,"LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        if c.islower():
            d["LOWER_CASE"] += 1

        
    print("Original String", s)
    print("Number of Upper case character: ",d["UPPER_CASE"])
    print("Number of Lower case character: ",d["LOWER_CASE"])

print(case_counter("Hello World!"))
print(case_counter("PYTHON"))
print(case_counter("python"))
print(case_counter("1234!@#$"))
print(case_counter("Pata DONT BE SCARE of Python"))
