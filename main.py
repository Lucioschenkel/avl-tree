import tree

tr = tree.AVLTree()

tr.add(5)
tr.add(3)
tr.add(10)
tr.add(10)
tr.add(10)
tr.add(4)
tr.add(20)

tr.print_tree()

print(tr.size())