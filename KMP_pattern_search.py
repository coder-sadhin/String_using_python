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

    # index for text[]
    i=0

    while i < Q:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == P:
            print("Pattern found at index " + str(i-j))
            j=long_prefix_suffix[j-1]

        # mismatch after j matches
        elif i < Q and pattern[j] != text[i]:
            if j != 0:
                j=long_prefix_suffix[j-1]
            else:
                i += 1
