# First I need to define the node class and generate a tree

class Node():
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.edge_label = None
        self.string_label = None
        self.siblings = [] # Do I need to make some sort of list here?
        self.children = [] # Do I need to make some sort of list here?
        self.children_val = []

    def __repr__(self):
        rep = f"{self.val}"
        return rep



a = Node("A")
b = Node("B")
c = Node("C")

a.children.append(b)
a.children.append(c)
b.parent = a
c.parent = a
# print(a.children)
# print(b.parent)




class Trie():
    def __init__(self):
        self.nodes = []
        self.roots = []
        self.roots_vals = []

    def insert(self, seq):
        root = Node(seq[0])
        if root.val not in self.roots_vals:
            self.roots.append(root)
            self.roots_vals.append(root.val)
            self.nodes.append(root) # Not correct
            prev = root
        else:
            n = self.roots_vals.index(root.val)
            prev = self.nodes[n] # The node which root val equals the value rootvalue == "A". if index value is "A" return node
        for i in range(1,len(seq)):
            next = Node(seq[i])
            if next.val not in prev.children_val: # How to get this value without having to make a new list? with values?
                self.nodes.append(next)
                prev.children.append(next)
                prev.children_val.append(next.val)
                next.parent = prev
            prev = next
        return self.nodes

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
print(test.nodes[1].children)
print(len(test.nodes))
# Why does B not have E as a child?

#############################################################
    # def __insert__(self, val, parent):
    #     node = Node(val, parent)
    #     self.nodes.append(node)
    #     parent.children.append(node)