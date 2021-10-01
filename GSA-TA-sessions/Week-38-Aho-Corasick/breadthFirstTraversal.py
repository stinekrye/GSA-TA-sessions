# First I need to define the node class and generate a tree
# I need to insert string labels and edge labels
class Node():
    def __init__(self, val, parent = None, edge_label = None, string_label = None, siblings = None, children = None, children_val = None):
        self.val = val # This is the edge_label
        self.parent = None
        self.edge_label = None
        self.string_label = None
        self.siblings = [] # Do I need to make some sort of list here?
        self.children = [] # Do I need to make some sort of list here?
        self.children_val = []

    def __repr__(self):
        rep = f"{self.val}"
        return rep

# Then I can define the trie
class Trie():
    def __init__(self):
        self.nodes = [[],[]]
        self.roots = []
        self.roots_vals = []

    def insert(self, seq):                          # We insert an entire sequence at the time
        layer = 0
        root = Node(seq[0])                         # The root is a special case
        if root.val not in self.roots_vals:         # Check if we have already encounterd this root. In not append this new root and set that as prev.
            for r in self.roots:
                r.siblings.append(root)
                root.siblings.append(r)
            self.roots.append(root)
            self.roots_vals.append(root.val)
            self.nodes[layer].append(root)
            prev = root


        else:                                       # If the root is already there choose the correct root as prev
            n = self.roots_vals.index(root.val)
            prev = self.nodes[0][n]                 # The node which root val equals the value rootvalue == "A". if index value is "A" return node

        layer += 1
        i = 1
        while i < len(seq):                         # Then insert the sequence one character at the time
            next = Node(seq[i])

            if next.val not in prev.children_val:   # Check if the character is already found as a child of prev. If not append it
                if len(prev.children) > 0:          # Update siblings while we build the trie
                    for child in prev.children:
                        if child.val != next.val:
                            child.siblings.append(next)
                            next.siblings.append(child)

                self.nodes[layer].append(next)      # I think this can be done smarter, so it can helt us in the depth first traversal
                prev.children.append(next)
                prev.children_val.append(next.val)
                next.parent = prev
                prev = next
            else:                                   # If it is already there - just skip it
                m = prev.children_val.index(next.val)
                prev = prev.children[m]
            i += 1
            if layer == len(self.nodes)-1:
                self.nodes.append([])
            layer +=1


    def __iter__(self):
        for layer in self.nodes:
            for node in layer:
                yield node

    def __getitem__(self, i):
        traversal = []
        for node in self:
            traversal.append(node)
        return traversal[i]

    def __repr__(self):
        rep = f"{self.nodes}"
        return rep

    def __len__(self):
        return len(self.nodes)

string1 = "ABC"
string2 = "ABE"
string3 = "ACE"
test = Trie()
test.insert(string1)
test.insert(string2)
test.insert(string3)
i = 2
j = 1
# print(test.nodes)
# print(test.nodes[i])
# print(test.nodes[i][j].siblings)
# print(test[4])
# print("next")
# for i in test:
#     print(i)
print(test)
#############################################################
    # def __insert__(self, val, parent):
    #     node = Node(val, parent)
    #     self.nodes.append(node)
    #     parent.children.append(node)