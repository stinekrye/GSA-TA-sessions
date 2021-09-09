import random
DNA = ["a", "g", "c", "t"]

def mutate(seq, d):
    res = []
    seq = list(seq)
    for _ in range(d):
        for position in range(len(seq)):
            for mutation in range(3):
                if mutation == 0:
                    seq[position] = random.choice(DNA)
                elif mutation == 1:
                    del seq[position]
                else:
                    seq = seq[:position] + [random.choice(DNA)] + seq[position:]
                res.append(''.join(seq))
    return res



seq = "a"
print(mutate(seq,1))
