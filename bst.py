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
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
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
        if self.root == None:
            return False
        else:
            return self._find(self.root, value)
    
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

    def sort(self, n=None):
        if n == None:
            n = self.root
        self._sorted = []
        if n != None:
            self._sort(n)
            return self._sorted
    
    def _sort(self, current_node):
        if current_node != None:
            self._sort(current_node.left_child)
            self._sorted.append(current_node.value)
            self._sort(current_node.right_child)
        return self._sorted

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
        sorted = self.sort(n)
        if len(sorted) > 1:
            return sorted[0]
        else:
            return None

    def delete(self, value):
        if self.root != None:
            self._delete(self.root, value)

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
    bst.insert(9)
    bst.insert(12)
    bst.insert(7)
    bst.insert(2)
    bst.insert(21)
    bst.insert(10)
    bst.insert(4)
    bst.insert(1)
    bst.insert(13)
    bst.insert(24)
    bst.insert(23)
    bst.insert(28)
    bst.insert(17)
    bst.insert(14)
    print(bst.sort())
    print(bst.min_value())
    print('-'*10)
    print('Height:', bst.height())
    print('-'*10)
    bst.delete(12)
    print(bst.sort())
    print(bst.find(2))
