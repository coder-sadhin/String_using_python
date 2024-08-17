'''
Question :
Given a string consisting of English alphabets, the task is to count the number of adjacent pairs of vowels.
For example :
Input: str = “abaebio”
Output: 2
(a, e) and (i, o) are the only valid pairs.
Source:A very Common Interview Question.

Time Complexity : The goal is to complete this question in O(n).
'''

#function to check whether a character is vowel or not
def is_vowel(character):
    if character.lower() in ['a', 'e', 'i', 'o', 'u']: 
        return True
    else:  
        return False
  
