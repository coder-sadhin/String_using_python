"""
Question:
Check whether two strings are anagram of each other:
Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.
Source:A very Common Interview Question,asked in companies like Amazon,Goldman Sachs and Nagarro.

Time Complexity:
The goal is to complete this question in O(n).
This solution is optimized by using bit manipulation. If we start at a value of 0 and XOR all the characters of both strings, we should return an end value of 0 if they are anagrams because there would be an even occurrence of all characters in the anagram.

Space Complexity:
The space complexity of this approach is O(1).
"""