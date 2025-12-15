"""
Example test script to demonstrate package usage
Run this after installing the package with: pip install -e .
"""

from python_tools_utils import add_numbers, multiply_numbers

if __name__ == "__main__":
    # Test add_numbers
    result1 = add_numbers(5, 3)
    print(f"add_numbers(5, 3) = {result1}")
    
    # Test multiply_numbers
    result2 = multiply_numbers(4, 7)
    print(f"multiply_numbers(4, 7) = {result2}")
    
    # Test with floats
    result3 = add_numbers(2.5, 3.7)
    print(f"add_numbers(2.5, 3.7) = {result3}")
    
    result4 = multiply_numbers(1.5, 2.5)
    print(f"multiply_numbers(1.5, 2.5) = {result4}")
    
    print("\n✅ All tests passed!")

