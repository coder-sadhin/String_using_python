"""
Question:
Check Permutation: Given two strings, write a method to decide if
one is a permutation of the other.
Source: Cracking the Code Interview 6th Edition Question 1.2

Time Complexity:
Every letter must be looped which means O(n) time complexity. Then,
we must check if each letter is in the dictionary which is another
O(n) time complexity. Overall, the total time complexity is O(n^2).
"""

letter_counts = {}


def check_permutations(word1, word2):
    # Case 1: Not matching length
    if len(word1) != len(word2):
        return False
    