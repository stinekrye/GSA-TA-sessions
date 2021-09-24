from breadthFirstTraversal import Trie
string1 = "ABC"
string2 = "ABE"
string3 = "ACE"
test = Trie()
test.insert(string1)
test.insert(string2)
test.insert(string3)
# i = 5
# print(test.nodes)
# print(test.nodes[i])
# print(test.nodes[i].children)







# def iterate(trie):
#     traversal = []
#     for node in trie.roots:
#         traversal.append(node)
#     p = 0                           # p for pointer
#     while p < len(trie.roots):
#         c = trie.roots[p]
#         traversal.append(unlist(c.children)
#         p +=1
#     return traversal

#
# def iterate(trie):
#     traversal = []
#     current = trie.roots[0]
#     while current.children != []:
#         traversal.append(current)
#         traversal.append(current.siblings)
#         current = current.children[0]
#
#         if len(traversal) > len(trie.nodes):
#             break
#     return traversal


res = iterate(test)
for i in res:
    print(i)
# print(res)


# test = [[1],[2]]
# print(len(test))