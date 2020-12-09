from queue import PriorityQueue

class Node():

    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVLTree():

    def __init__(self):
        self.root = None
        self.node_count = 0

    def __repr__(self):
        if self.root==None: return ''
        content='\n' # to hold final string
        cur_nodes=[self.root] # all nodes at current level
        cur_height=self.root.height # height of nodes at current level
        sep=' '*(2**(cur_height-1)) # variable sized separator between elements
        while True:
            cur_height+=-1 # decrement current height
            if len(cur_nodes)==0: break
            cur_row=' '
            next_row=''
            next_nodes=[]

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n==None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None,None])
                    continue

                if n.v!=None:       
                    buf=' '*int((5-len(str(n.v)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.v),buf)+sep
                else:
                    cur_row+=' '*5+sep

                if n.left!=None:  
                    next_nodes.append(n.left)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

                if n.right!=None: 
                    next_nodes.append(n.right)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)

            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes=next_nodes
            sep=' '*int(len(sep)/2) # cut separator size in half
        return content    

    def add(self, v):
        if self.root == None:
            self.root = Node(v)
            self.node_count = self.node_count + 1
        else:
            self._add(v, self.root)

    def _add(self, v, curr_node):
        if curr_node.v > v:
            if curr_node.left == None:
                curr_node.left = Node(v)
                curr_node.left.parent = curr_node
                self.node_count = self.node_count + 1
                self._inspect_insertion(curr_node.left)
            else:    
                self._add(v, curr_node.left)
        elif curr_node.v < v:
            if curr_node.right == None:
                curr_node.right = Node(v)
                curr_node.right.parent = curr_node
                self.node_count = self.node_count + 1
                self._inspect_insertion(curr_node.right)
            else:
                self._add(v, curr_node.right)
        else:
            return                 

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent == None: return
        path=[cur_node]+path

        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height-right_height) > 1:
            path=[cur_node.parent]+path
            self._rebalance_node(path[0],path[1],path[2])
            return

        new_height = 1 + cur_node.height 
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('_rebalance_node: z,y,x node configuration not recognized!')

    def _right_rotate(self, z):
        sub_root = z.parent 
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 != None: t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.root=y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent 
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 != None: t2.parent = z
        y.parent = sub_root
        if y.parent == None: 
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def get_height(self, cur_node):
        if cur_node == None: return 0
        return cur_node.height

    def taller_child(self,cur_node):
        left = self.get_height(cur_node.left)
        right = self.get_height(cur_node.right)
        return cur_node.left if left >= right else cur_node.right
    
    def get_parent(self, v):
        if self.root == None: return None
        return self._get_parent(self.root, v)

    def _get_parent(self, curr_node, v):
        if curr_node.v == v:
            return curr_node.parent
        elif curr_node.v > v:
            if curr_node.left != None:
                return self._get_parent(curr_node.left, v)
            else:
                return None    
        else:
            if curr_node.right != None:
                return self._get_parent(curr_node.right, v)
            else:
                return None        

    def contains(self, v):
        if self.root == None: return False
        return self._contains(self.root, v)

    def _contains(self, curr_node, v):
        if curr_node == None: return False

        if curr_node.v == v:
            return True
        elif curr_node.v > v:
            return self._contains(curr_node.left, v)
        else:
            return self._contains(curr_node.right, v)    


    def height(self):
        if self.root == None: return 0
        return self._height(self.root, 0)

    def _height(self, curr_node, curr_height):
        if curr_node == None: return curr_height
        
        left_height = self._height(curr_node.left, curr_height + 1)
        right_height = self._height(curr_node.right, curr_height + 1)
        
        return max(left_height,right_height)

    def is_balanced(self, root): 
        if root is None: 
            return True
    
        # left and right heights
        lh = self.get_height(root.left) 
        rh = self.get_height(root.right) 
    
        # if the absolute difference between left and right's heights is smaller or equal to 1, is balanced
        if (abs(lh - rh) <= 1) and self.is_balanced(root.left) is True and self.is_balanced(root.right) is True: 
            return True
    
        # Tree is unbalanced
        return False

    def size(self):
        return self.node_count

    def is_empty(self):
        return self.size() == 0

    def positions_pre(self):
        if self.root == None:
            raise Exception('Tree is empty!')
        self._positions_pre(self.root)

    def _positions_pre(self, curr_node):
        if curr_node != None:
            print(curr_node.v)
            if curr_node.left != None:
                self._positions_pre(curr_node.left)
            
            if curr_node.right != None:
                self._positions_pre(curr_node.right)

    def positions_central(self):
        if self.root == None:
            raise Exception('Tree is empty!')

        self._positions_central(self.root)

    def _positions_central(self, curr_node):
        if curr_node != None:
            if curr_node.left != None:
                self._positions_central(curr_node.left)

            print(curr_node.v)

            if curr_node.right != None:
                self._positions_central(curr_node.right)


    def positions_pos(self):
        if self.root == None:
            raise Exception('Tree is empty!')

        self._positions_pos(self.root)

    def _positions_pos(self, curr_node):
        if curr_node != None:
            if curr_node.left != None:
                self._positions_pos(curr_node.left)
            
            if curr_node.right != None:
                self._positions_pos(curr_node.right)
            
            print(curr_node.v)

    def positions_width(self):
        q = PriorityQueue()
        idx = 0
        q.put((idx, self.root.v, self.root.left, self.root.right))

        while not q.empty():
            n = q.get()

            print(n[1])
            idx += 1

            if n[2] != None:
                q.put((idx, n[2].v, n[2].left, n[2].right))
            
            if n[3] != None:
                q.put((idx, n[3].v, n[3].left, n[3].right))