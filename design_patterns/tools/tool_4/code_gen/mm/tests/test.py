import unittest
from src.matrix import matrix_multiply


class TestMatrixMultiplication(unittest.TestCase):
    """Test cases for matrix multiplication function."""
    
    def test_simple_2x2_multiplication(self):
        """Test multiplication of two 2x2 matrices."""
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_3x3_multiplication(self):
        """Test multiplication of two 3x3 matrices."""
        matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_rectangular_matrices(self):
        """Test multiplication of rectangular matrices (2x3 * 3x2)."""
        matrix_a = [[1, 2, 3], [4, 5, 6]]
        matrix_b = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_identity_matrix(self):
        """Test multiplication with identity matrix."""
        matrix_a = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        result = matrix_multiply(matrix_a, identity)
        self.assertEqual(result, [[1, 2], [3, 4]])
    
    def test_single_element_matrices(self):
        """Test multiplication of 1x1 matrices."""
        matrix_a = [[5]]
        matrix_b = [[3]]
        expected = [[15]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)
    
    def test_incompatible_dimensions(self):
        """Test that incompatible dimensions raise ValueError."""
        matrix_a = [[1, 2], [3, 4]]
        matrix_b = [[1, 2], [3, 4], [5, 6]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix_a, matrix_b)
    
    def test_empty_matrix(self):
        """Test that empty matrices raise ValueError."""
        with self.assertRaises(ValueError):
            matrix_multiply([], [[1, 2]])
    
    def test_float_values(self):
        """Test multiplication with float values."""
        matrix_a = [[1.5, 2.5], [3.5, 4.5]]
        matrix_b = [[2.0, 0.0], [0.0, 2.0]]
        expected = [[3.0, 5.0], [7.0, 9.0]]
        result = matrix_multiply(matrix_a, matrix_b)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMatrixMultiplication)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    import os
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
