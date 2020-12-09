import tree

tr = tree.AVLTree()

tr.add(1)
tr.add(3)
tr.add(5)
tr.add(6)
tr.add(8)
tr.add(9)
tr.add(10)

print(tr.contains(9))
print(tr.get_parent(8))
print(tr.get_parent(6))
print(tr.size())
print(tr.is_balanced(tr.root))

print(tr)
print(tr.positions_central())