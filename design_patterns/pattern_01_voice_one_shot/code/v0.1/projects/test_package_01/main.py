"""
Simple Python program that uses function_one from package_01.
"""

from package_01 import function_one


def main():
    """Main function to demonstrate usage of function_one."""
    # Example usage of function_one
    result1 = function_one("world", prefix="Hello ", suffix="!")
    print(f"Result 1: {result1}")
    
    result2 = function_one("Python", prefix="Welcome to ", suffix=" programming!")
    print(f"Result 2: {result2}")
    
    result3 = function_one("test", suffix=" passed")
    print(f"Result 3: {result3}")
    
    result4 = function_one("prefix only", prefix="[INFO] ")
    print(f"Result 4: {result4}")


if __name__ == "__main__":
    main()

