import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to test
from matrix_multiply import matrix_multiply


class TestMatrixMultiply(unittest.TestCase):
    """Test cases for matrix_multiply function."""
    
    def test_basic_multiplication(self):
        """Test basic 2x2 matrix multiplication."""
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_identity_matrix(self):
        """Test multiplication with identity matrix."""
        matrix_a = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        result = matrix_multiply(matrix_a, identity)
        # Compare with floats since implementation returns floats
        expected = [[1.0, 2.0], [3.0, 4.0]]
        self.assertEqual(result, expected)
    
    def test_different_dimensions(self):
        """Test multiplication of matrices with different dimensions (2x3 * 3x2)."""
        matrix_a = [[1, 2, 3], [4, 5, 6]]
        matrix_b = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_single_element_matrices(self):
        """Test multiplication of 1x1 matrices."""
        matrix_a = [[5]]
        matrix_b = [[3]]
        expected = [[15.0]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_float_values(self):
        """Test multiplication with float values."""
        matrix_a = [[1.5, 2.5], [3.5, 4.5]]
        matrix_b = [[2.0, 0.0], [0.0, 2.0]]
        expected = [[3.0, 5.0], [7.0, 9.0]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_zero_matrix(self):
        """Test multiplication with zero matrix."""
        matrix_a = [[1, 2], [3, 4]]
        zero_matrix = [[0, 0], [0, 0]]
        expected = [[0.0, 0.0], [0.0, 0.0]]
        result = matrix_multiply(matrix_a, zero_matrix)
        self.assertEqual(result, expected)
    
    def test_incompatible_dimensions_raises_error(self):
        """Test that incompatible dimensions raise ValueError."""
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix_a, matrix_b)
    
    def test_empty_matrix_raises_error(self):
        """Test that empty matrices raise ValueError."""
        matrix_a = []
        matrix_b = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix_a, matrix_b)
    
    def test_rectangular_result(self):
        """Test multiplication resulting in rectangular matrix (3x2 * 2x4)."""
        matrix_a = [[1, 2], [3, 4], [5, 6]]
        matrix_b = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected = [[11, 14, 17, 20], [23, 30, 37, 44], [35, 46, 57, 68]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMatrixMultiply)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
