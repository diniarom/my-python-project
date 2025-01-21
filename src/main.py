# src/main.py

def greet(name):
    print(f"Hello, {name}!")  # This is a well-formatted line


def add_numbers(a, b): return a + b  # This line violates PEP8 guidelines


def main():
    greet("World")
    result = add_numbers(5, 7)
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()
