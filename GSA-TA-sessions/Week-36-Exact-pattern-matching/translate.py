# 1st function: Translates an alignment into a cigar string
# 2nd function: Compresses the cigar string
# 3rd function: Translates the compressed cigar string into an alignment

# Input
seq1 = "ag-ct"
seq2 = "agacg"

def align_to_cigar(seq1,seq2):
    j,i = 0,0
    cigar = []
    while i < len(seq1):
        if seq1[i] == seq2[j]:
            cigar.append("M")
        elif seq1[i] == "-":
            cigar.append("D")
        elif seq2[j] == "-":
            cigar.append("I")
        else:
            cigar.append("X")
        i += 1
        j += 1
    return ''.join(cigar)

def compress_cigar(cigar):
    compress = []
    counter = 1
    i = 0
    while i < len(cigar)-1:
        if cigar[i] == cigar[i+1]:
            counter += 1
            i += 1

        else:
            compress.append("{}{}".format(counter,cigar[i]))
            counter = 1
            i += 1

    if cigar[-1] != cigar[-2]:
        compress.append("1{}".format(cigar[-1]))
    if cigar[-1] == cigar[-2]:
        compress.append("{}{}".format(counter,cigar[i]))
    return ''.join(compress)


def cigar_to_alignment(seq1,seq2,cigar):
    align1 = []
    align2 = []
    n = 0 # number from cigar
    c = 0 # counter to track progress
    i = 0
    while i < len(cigar):
        if cigar[i].isnumeric():
            n = int(cigar[i])
            c += int(cigar[i])
            i += 1
        elif cigar[i] == "M" or cigar[i] == "X":
            align1.append(seq1[c-n:c])
            align2.append(seq2[c-n:c])
            n = 0
            i += 1
        elif cigar[i] == "D":
            align1.append("-"*n)
            align2.append(seq2[c-n:c])
            n = 0
            i += 1
        elif cigar[i] == "I":
            align1.append(seq1[c-n:c])
            align2.append("-"*n)
            n = 0
            i += 1

    return ''.join(align1), ''.join(align2)

res = align_to_cigar(seq1,seq2)
res2 = compress_cigar(res)
res3 = cigar_to_alignment(seq1,seq2,res2)
print(res)
print(res2)
print(res3)