import graphviz
import os
os.environ["PATH"] += os.pathsep + "C:/Users/ASUS/miniconda3/Lib/site-packages/graphviz"

def remap(x):
    m = {a:i+1 for i,a in enumerate(sorted(set(x)))}
    n = [m[a] for a in x]
    return n, len(m)

def build_suffix(x):
    res = []
    n, alpha = remap(x)
    for i in range(len(n)):
        res.append(n[i:])
    return res, alpha


class Node():
    def __init__(self, range_start = None, range_end = None, string_label = None, children = None, parent = None):
        self.range_start = range_start
        self.range_end = range_end
        self.string_label = string_label # only for leaves
        self.children = {}
        self.parent = parent
        # Siblings is parent.children
        # parent + suffix_link is not needed

    def __repr__(self):
        rep = f"Node({self.range_start},{self.range_end})"
        return rep

class SuffixTree(): #not compressed

    def __init__(self):
        self.root = Node()
        self.n = 0

    def insert(self, seq, idx): # debug indexes
        s, alpha = remap(seq)
        c = self.root

        i = 0                   # index into the string

        while i < len(s):       # break when we have inserted the full sequence
            if s[i] in c.children:
                k = 0  # counter along the edges
                c = c.children[s[i]]    # Choose the right node, to follow
                while s[i+k] == s[k]:      # use its range here
                    k += 1
                if k != c.range_end: # break string # else restart loop
                    b = Node(i, i+k, parent = c.parent)
                    c.range_start = i+k
                    c.parent = b
                    b.children[s[i+k]] = Node(range_start = i+k, range_end = len(s)-1, parent = b)
                    self.n += 2

            else:
                c.children[s[i]] = Node(range_start = i, range_end = i+len(s), string_label = idx, parent = c)
                self.n += 1
                break

    def __len__(self):
        return self.n

    # def search(self, pattern):

    def __repr__(self):
        f = graphviz.Digraph(comment="suffix tree")
        # Make depth first traversal. Might be difficult with the dictionaries

        c = self.root
        # while c.children != None:
        f.edge("", "1", label = f"{c.range_start},{c.range_end}")
            # c = c.children

        f.view()



# Idea make graphviz work, then debug

y = "GCGCA"
x, alpha = build_suffix(y)



res = SuffixTree()
res.insert(x[0],0)

print(res)
