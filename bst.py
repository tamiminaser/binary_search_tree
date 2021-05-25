class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        if isinstance(value, int):
            if self.root == None:
                self.root = Node(value)
            else:
                self._insert(self.root, value)
        elif isinstance(value, list):
            for v in value:
                self.insert(v)
    
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child == None:
                current_node.left_child = Node(value)
                current_node.left_child.parent = current_node
            else:
                self._insert(current_node.left_child, value)
        elif value > current_node.value:
            if current_node.right_child == None:
                current_node.right_child = Node(value)
                current_node.right_child.parent = current_node
            else:
                self._insert(current_node.right_child, value)
        else:
            print('Double value is not allowed.')

    def find(self, value):
        if isinstance(value, int):
            if self.root == None:
                return False
            else:
                return self._find(self.root, value)
        elif isinstance(value, list):
            list_find = []
            for v in value:
                list_find.append(self.find(v))
            return list_find

    
    def _find(self, n, value):
        if n.value == value:
            return True
        elif value > n.value and n.right_child != None:
            return self._find(n.right_child, value)
        elif value < n.value and n.left_child != None:
            return self._find(n.left_child, value)
        return False

    def height(self):
        if self.root == None:
            return -1
        else:
            return self._height(self.root)
    
    def _height(self, n):
        if n == None:
            return -1
        else:
            return max(self._height(n.left_child)+1, self._height(n.right_child)+1)

    def __len__(self):
        if self.root == None:
            return 0
        return len(self.inorder())    

    def inorder(self, n=None):
        if n == None:
            n = self.root
        self._inorder_lst = []
        if n != None:
            self._inorder(n)
            return self._inorder_lst
    
    def _inorder(self, current_node):
        if current_node != None:
            self._inorder(current_node.left_child)
            self._inorder_lst.append(current_node.value)
            self._inorder(current_node.right_child)
        return self._inorder_lst

    def preorder(self, n=None):
        if n == None:
            n = self.root
        self._preorder_lst = []
        if n != None:
            self._preorder(n)
            return self._preorder_lst
    
    def _preorder(self, current_node):
        if current_node != None:
            self._preorder_lst.append(current_node.value)
            self._preorder(current_node.left_child)
            self._preorder(current_node.right_child)
        return self._inorder_lst

    def postorder(self, n=None):
        if n == None:
            n = self.root
        self._postorder_lst = []
        if n != None:
            self._postorder(n)
            return self._postorder_lst
    
    def _postorder(self, current_node):
        if current_node != None:
            self._postorder(current_node.left_child)
            self._postorder(current_node.right_child)
            self._postorder_lst.append(current_node.value)
        return self._postorder_lst

    def number_of_children(self, n):
        no_children = 0
        if n.left_child != None:
            no_children += 1
        if n.right_child != None:
            no_children += 1   
        return no_children

    def min_value(self, n=None):
        if n == None:
            n = self.root
        sorted = self.inorder(n)
        if len(sorted) > 0:
            return sorted[0]
        else:
            return None

    def delete(self, value):
        if isinstance(value, int):
            if self.root != None:
                self._delete(self.root, value)
        elif isinstance(value, list):
            for v in value:
                self.delete(v)        

    def _delete(self, current_node, value):
        if current_node.value == value:
            if self.number_of_children(current_node) == 0:
                if current_node.parent.left_child == current_node:
                    current_node.parent.left_child = None
                elif current_node.parent.right_child == current_node:
                    current_node.parent.right_child = None
            elif self.number_of_children(current_node) == 1:
                if current_node.parent.left_child == current_node:
                    if current_node.left_child != None:
                        current_node.parent.left_child = current_node.left_child
                    else:
                        current_node.parent.left_child = current_node.right_child
                elif current_node.parent.right_child == current_node:
                    if current_node.left_child != None:
                        current_node.parent.right_child = current_node.left_child
                    else:
                        current_node.parent.right_child = current_node.right_child
            elif self.number_of_children(current_node) == 2:
                current_node.value = self.min_value(current_node.right_child)
                self._delete(current_node.right_child, current_node.value)            
        else:
            if current_node.left_child != None:
                self._delete(current_node.left_child, value)
            if current_node.right_child != None:
                self._delete(current_node.right_child, value)

if __name__ == '__main__':
    bst = BinarySearchTree()
    
    # First we insert some values to the tree
    # We can insert values as integer or a list of integers
    bst.insert(9)
    bst.insert(12)
    bst.insert([7, 2, 21, 10, 4, 1, 13, 24, 23, 28, 17, 14])

    #
    print('Find([2, 21]):', bst.find([2, 21]))

    # inorder() method returns a sorted list of values    
    print('Inorder:', bst.inorder())
    print('Pre-order:', bst.preorder())
    print('Post-order:', bst.postorder())
    
    # height() method returns the height of the tree
    print('Height:', bst.height())


    print('Length:', len(bst))
    
    # find() method return True if it finds the value in the tree
    print(bst.find(2))

    # delete() method removes values from the tree
    bst.delete(28)
    bst.delete([2, 21])
    
    # Two tests to make sure deleting was done properly
    print(bst.inorder())
    print(bst.find(2))

