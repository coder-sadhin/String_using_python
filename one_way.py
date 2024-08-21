"""
Question:
One Away: There are three types of edits that can be performed on
strings: insert a character, remove a character, or replace a
character. Given two strings, write a function to check if they
are one edit (or zero edits) away.

Example:
pale,   ple  -> true
pales,  pale -> true
pale,   bale -> true
pale,   bake -> false

Source: Cracking the Code Interview 6th Edition Question 1.5

Time Complexity:
We are going through both strings at the same time and stopping when
more than one letter is different, which means O(n) time complexity
on the while loop. No extra space is required.
"""