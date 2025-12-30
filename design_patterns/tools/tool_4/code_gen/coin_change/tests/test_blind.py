import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import min_coins

class TestMinCoins(unittest.TestCase):
    """Test cases for min_coins function that finds minimum number of coins needed to make target amount."""
    
    def test_basic_case(self):
        """Test basic case with common coin denominations."""
        coins = [1, 2, 5]
        amount = 11
        result = min_coins(coins, amount)
        self.assertEqual(result, 3)  # 5 + 5 + 1 = 11
    
    def test_amount_zero(self):
        """Test when amount is zero, should return 0 coins."""
        coins = [1, 2, 5]
        amount = 0
        result = min_coins(coins, amount)
        self.assertEqual(result, 0)
    
    def test_impossible_amount(self):
        """Test when amount cannot be made with given coins."""
        coins = [2]
        amount = 3
        result = min_coins(coins, amount)
        self.assertEqual(result, -1)
    
    def test_single_coin_exact_match(self):
        """Test when amount exactly matches a single coin."""
        coins = [1, 5, 10]
        amount = 10
        result = min_coins(coins, amount)
        self.assertEqual(result, 1)
    
    def test_multiple_same_coins(self):
        """Test when multiple of same coin is needed."""
        coins = [3]
        amount = 9
        result = min_coins(coins, amount)
        self.assertEqual(result, 3)  # 3 + 3 + 3 = 9
    
    def test_greedy_not_optimal(self):
        """Test case where greedy approach would fail."""
        coins = [1, 3, 4]
        amount = 6
        result = min_coins(coins, amount)
        self.assertEqual(result, 2)  # 3 + 3 = 6, not 4 + 1 + 1
    
    def test_single_coin_type(self):
        """Test with only one coin denomination."""
        coins = [1]
        amount = 5
        result = min_coins(coins, amount)
        self.assertEqual(result, 5)
    
    def test_large_coins_small_amount(self):
        """Test when all coins are larger than amount."""
        coins = [5, 10]
        amount = 3
        result = min_coins(coins, amount)
        self.assertEqual(result, -1)
    
    def test_empty_coins_nonzero_amount(self):
        """Test with empty coins list and non-zero amount."""
        coins = []
        amount = 5
        result = min_coins(coins, amount)
        self.assertEqual(result, -1)
    
    def test_standard_us_coins(self):
        """Test with standard US coin denominations."""
        coins = [1, 5, 10, 25]
        amount = 30
        result = min_coins(coins, amount)
        self.assertEqual(result, 2)  # 25 + 5 = 30

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMinCoins)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
