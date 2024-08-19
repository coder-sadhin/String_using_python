'''
Question: Given three strings A, B and C. Write a function that checks whether C 
is an interleaving of A and B. C is said to be interleaving A and B, if 
it contains all characters of A and B and order of all characters in 
individual strings is preserved.

Solution: We include one character from String A or String B and check whether the resultant 
string formed so far by one particular interleaving of the the current prefix of String A 
and String B form a prefix of String C. This can be achieved using dynamic programming.
This approach relies on fact that in order to determine whether a 
substring of String C(upto index k), can be formed by interleaving strings String A 
and String B upto indices i and j respectively depends on the characters of 
String A and String B upto indices i and j only and not on characters coming afterwards.

Complexity analysis -
Time complexity : O(m x n) . dp array of size n is filled m times where m and n are lengths of 
String A and String B respectively.
Space complexity : O(n)

'''

#Function to check if String C is formed by interleaving of String A and B
#Returns a boolean value
