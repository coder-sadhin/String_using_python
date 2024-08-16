#Python program for KMP Algorithm
def KMP_pattern_search(pattern, text):
    P = len(pattern)
    Q = len(text)
