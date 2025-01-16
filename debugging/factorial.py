#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to prevent infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Ensure an argument is provided
        try:
            number = int(sys.argv[1])  # Convert the argument to an integer
            if number < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(factorial(number))
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: ./factorial.py <integer>")
