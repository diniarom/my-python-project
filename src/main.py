# src/main.py

import os  # Unused import

def greet(  name  ):
print(f"Hello, {name}!")  # Incorrect indentation and extra spaces

def add_numbers(a,b):return a+b  # No whitespace around operators and too much code on one line


def main():
    greet("World")
    result = add_numbers(5,7) # No whitespace after comma
    print(f"The sum is: {result}")

if __name__=="__main__":main()  # No whitespace around operators and too much code on one line
