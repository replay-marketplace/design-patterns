import unittest
from src.coin_change import min_coins


class TestMinCoins(unittest.TestCase):
    """Test cases for the minimum coin change dynamic programming solution."""
    
    def test_standard_case(self):
        """Test standard coin denominations with achievable amount."""
        coins = [1, 2, 5]
        amount = 11
        # 11 = 5 + 5 + 1 = 3 coins
        self.assertEqual(min_coins(coins, amount), 3)
    
    def test_exact_coin_match(self):
        """Test when amount exactly matches a coin denomination."""
        coins = [1, 2, 5]
        amount = 5
        self.assertEqual(min_coins(coins, amount), 1)
    
    def test_zero_amount(self):
        """Test when target amount is zero."""
        coins = [1, 2, 5]
        amount = 0
        self.assertEqual(min_coins(coins, amount), 0)
    
    def test_impossible_amount(self):
        """Test when amount cannot be made with given coins."""
        coins = [2]
        amount = 3
        self.assertEqual(min_coins(coins, amount), -1)
    
    def test_single_coin_type(self):
        """Test with only one coin denomination."""
        coins = [1]
        amount = 7
        self.assertEqual(min_coins(coins, amount), 7)
    
    def test_large_coins(self):
        """Test with larger coin denominations."""
        coins = [1, 5, 10, 25]
        amount = 30
        # 30 = 25 + 5 = 2 coins
        self.assertEqual(min_coins(coins, amount), 2)
    
    def test_greedy_fails(self):
        """Test case where greedy approach would fail."""
        coins = [1, 3, 4]
        amount = 6
        # Greedy would pick 4 + 1 + 1 = 3 coins
        # Optimal is 3 + 3 = 2 coins
        self.assertEqual(min_coins(coins, amount), 2)
    
    def test_negative_amount(self):
        """Test with negative amount."""
        coins = [1, 2, 5]
        amount = -5
        self.assertEqual(min_coins(coins, amount), -1)
    
    def test_empty_coins(self):
        """Test with empty coin list and non-zero amount."""
        coins = []
        amount = 5
        self.assertEqual(min_coins(coins, amount), -1)
    
    def test_empty_coins_zero_amount(self):
        """Test with empty coin list and zero amount."""
        coins = []
        amount = 0
        self.assertEqual(min_coins(coins, amount), 0)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMinCoins)
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
