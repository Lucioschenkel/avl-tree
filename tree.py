class Node():

    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def add(self, n):
        if self.v > n.v:
            if self.left == None:
                self.left = n
            else:
                self.left.add(n)
        elif self.v < n.v:
            if self.right == None:
                self.right = n
            else:
                self.right.add(n)    


class Tree():

    """
        Adicionar elementos na árvore (método add);
        • Retornar o pai de um elemento (método getParent);
        • Verificar se um elemento está armazenado na árvore ou não (método contains);
        • Verificar qual é a altura da árvore (método height);
        • Verificar se a árvore está balanceada ou não (método isBalanced);
        • Verificar quantos elementos tem na árvore (método size);
        • Verificar se a árvore está vazia ou não (método isEmpty);
        • Retornar os elementos da árvore em uma lista usando diferentes caminhamentos (métodos
        positionsPre, positionsCentral, positionsPos e positionsWidth).
    """

    def __init__(self):
        self.root = None
        self.tree_height = 0
        self.node_count = 0

    def add(self, v):
        n = Node(v)
        if self.root == None:
            self.root = n
        else:
            self.root.add(n)

        self.node_count = self.node_count + 1        
        pass

    def get_parent(self, v):
        pass

    def contains(self, v):
        pass

    def height(self):
        return self.tree_height

    def is_balanced(self):
        pass

    def size(self):
        return self.node_count

    def is_empty(self):
        return self.size() == 0

    def positions_pre(self):
        pass

    def positions_central(self):
        pass

    def positions_pos(self):
        pass

    def positions_width(self):
        pass
