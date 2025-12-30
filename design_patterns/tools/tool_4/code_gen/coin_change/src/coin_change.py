def min_coins(coins: list, amount: int) -> int:
    """
    Find the minimum number of coins needed to make the target amount.
    
    Uses dynamic programming (bottom-up approach) to solve the coin change problem.
    
    Args:
        coins: List of coin denominations available
        amount: Target amount to make
        
    Returns:
        Minimum number of coins needed, or -1 if amount cannot be made
    """
    if amount < 0:
        return -1
    if amount == 0:
        return 0
    
    # dp[i] represents the minimum coins needed to make amount i
    # Initialize with amount + 1 (impossible value, acts as infinity)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    # Build up the solution for each amount from 1 to target
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # If we can use this coin, check if it gives a better solution
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still the impossible value, return -1
    return dp[amount] if dp[amount] != amount + 1 else -1
