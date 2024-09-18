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
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins += total // coin
            total %= coin

    return num_coins if total == 0 else -1
