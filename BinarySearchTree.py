class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Bst(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if(self.root is None):
            self.root = new_node
            return

        else:
            root_node = self.root
            if(root_node.val > val) :
                if(root_node.left is None):
                    root_node.left = new_node
                else:
                    root_node = root_node.left

            elif(root_node.val < val):
                if(root_node.right is None):
                    root_node.right  = new_node
                else:
                    root_node = root_node.right


    def print_nodes(self):
        root_node = self.root
        print(root_node.val)
        print(root_node.left.val)

        print(root_node.right.val)
        # print(root_node.right.right.val)


bst = Bst()
bst.insert(10)
bst.insert(5)
bst.insert(14)
bst.insert(32)
bst.insert(2)

bst.print_nodes()





