#Python program for KMP Algorithm
def KMP_pattern_search(pattern, text):
    P = len(pattern)
    Q = len(text)

    # create long_prefix_suffix[] that will hold the longest prefix suffix
    # values for pattern
    long_prefix_suffix = [0]*P

    # index for pattern[]
    j=0

    # preprocess the pattern (caluclate long_prefix_suffix[] array)
    long_Prefix_Suffix_Array(pattern, P, long_prefix_suffix)
