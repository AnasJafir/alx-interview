#!/usr/bin/python3
"""Make Change Module"""


def makeChange(coins, total):
    """
    function to determine the fewest number
    of coins needed to meet a given amount total.
    Parameters:
        coins: A list of the values of the coins in your possession.
        total: The given amount total.
    Returns:

        The fewest number of coins needed to meet the total.
        0 if the total is 0 or less.
        -1 if the total cannot be met by any number of coins.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else - 1
