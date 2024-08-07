#!/usr/bin/python3
"""
Primary module for the game.
"""


def sieve_of_eratosthenes(limit):
    """
    method to generate all prime numbers less than or equal to limit
    """
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]


def isWinner(x, nums):
    """
    method to determine the winner of the game
    """
    if x == 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    dp = [False] * (max_n + 1)

    for i in range(1, max_n + 1):
        for prime in primes:
            if prime > i:
                break
            if not dp[i - prime]:
                dp[i] = True
                break

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if dp[n]:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
