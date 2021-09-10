
# The naive algorithm:
# It will compare the first index of the substring to all indexes of the reference string. When a match is found, the second index of the substring is compared to the next index of the ref. string.
# If the match can be extented to cover the entire substring a match is found!


# Warm up
# 1: How would I test the correctness of the algorithm?
    # Make a "test-suite" which has a lot of substrings and reference sequences to match
        # Start with simple cases, then build a test suite
        # Good idea to make this random, and sample subsequences at specific indexes. Or generate sequences with a specific edit distance from a template
        # Write special cases by hand (empty strings, strings with same character, prefix and suffix)
        # Use classes of strings, which are different: Random, repetitive (fibonnaci?)
        # Compare to already working algorithms

# 2: How would you use that naive algorithm to test a more sophisticated algorithm?
    # I would check if they find the same matches?


# 3a: How do you test the running time of an algorithm?
    # Feed it input of different lengths, measure the time and make a graph
    # For each alg make a graph with time/expeced runningtime* as a function of n, with different lines for m
        # How can we derive the expected running time?

# Implementation of the naïve algorithm
    # What output is desired? I decide to only output the match and the pythonic index of the match


substr = "abc"
refseq = "abchhhabc"

def exact_naive(substr,refseq):
    match = []
    matches = []
    i,j,k = 0,0,0
    while j <= (len(refseq)-len(substr)): #break when we reach the end of the sequence
        if substr[i] == refseq[j]:
            k = j # We want to save j
            while len(match) != len(substr) and substr[i] == refseq[k]:
                match.append(substr[i])
                k+=1
                i+=1

            if i == len(substr): # if a match is found
                matches.append([j, match])
                i = 0
                j += 1 # We want to look at the next letter in j, from where we found the previous match
                match = []

            else:
                i = 0
                j += 1 # We want to look at the next letter in j, from where we found the previous match
                match = []


        else:
            j += 1
    return matches



res = exact_naive(substr, refseq)
print(res)