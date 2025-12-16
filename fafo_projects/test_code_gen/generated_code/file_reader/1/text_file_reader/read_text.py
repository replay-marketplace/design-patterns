import os

# Function to read and display file content
def read_file(filename):
    with open(filename, 'r') as file:
        print(file.read())

# Test the function
read_file('sample.txt')