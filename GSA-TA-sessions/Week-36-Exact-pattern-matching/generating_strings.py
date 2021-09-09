# Inexact pattern matching: The algorithmic idea
    # Given a string A we can generate n strings which are closely related to A. (The size of n depends on the magnitude of the edit distance. Proportional)
    # We can then search for all the n strings


# 1: That depends on the edit distance.
    # If edit distance = 1 and the length of a sequence is l, we can have one mismatch (?), and have to generate 4*l sequences. If edit distance = 2 we have to generate 16*l strings. The number of strings are l*4^edit distance
        # This makes the method unfeasible for large strings and large edit distances
        # Why do we need recursion for this?
            # Because an edit distance of two can also be one insertion + one deletion, or a mutation + deletion.

# 2: The recursion
    # f(0) = 1 # If edit distance = 0, we must have the same sequence
    # f(1) = l*4 + l + l*4 # Mutate all once, delete all once, insert all four once for every position
    # f(2) = l*4^2 + l^2 + l*4^2
    # f(n) = l*4^n + l^n + l*4^n  -> 2*l4^n + l^n

    # Is there a quick way to generate all possible cigar strings?
        # I have tried to adjust Thomas' script, but has ot been succesfull

# 3 The asymptotic complexity is  O(n^d) (the length of the sequence to the power of edit distance) (very loose)

# 4 The upper bound is especially important

# Not sure what is meant by implementing the recursion
    # End up with a plot with sting length, number of strings generated at a given edit distance (this is three variables





