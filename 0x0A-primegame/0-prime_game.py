#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(max_n):
    """computes prime numbers up to max_n using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return is_prime


def count_prime_picks(n, is_prime):
    """Counts how many turns it takes to finish the game for a given n."""
    picked = set()
    prime_picks = 0

    for i in range(2, n + 1):
        if i not in picked and is_prime[i]:
            prime_picks += 1
            for multiple in range(i, n + 1, i):
                picked.add(multiple)

    return prime_picks


def isWinner(x, nums):
    """Determines the winner of the prime game over x rounds."""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_picks = count_prime_picks(n, is_prime)

        if prime_picks % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
