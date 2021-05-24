import pytest
from bst import BinarySearchTree

def test_root_insert():
    bst = BinarySearchTree()
    bst.insert(9)
    assert bst.root.value == 9

def test_insert1():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10])
    assert bst.root.right_child.left_child.value == 10

def test_insert2():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    assert bst.root.left_child.right_child.left_child.value == 4

def test_length1():
    bst = BinarySearchTree()
    assert len(bst) == 0

def test_length2():
    bst = BinarySearchTree()
    bst.insert(9)
    assert len(bst) == 1

def test_length3():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    assert len(bst) == 8

def test_find1():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    assert bst.find(3) == True

def test_find2():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    assert bst.find(4) == True

def test_find3():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    assert bst.find(11) == False

def test_delete_find1():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    bst.delete(12)
    assert bst.find(12) == False 

def test_delete_find2():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    bst.delete(3)
    assert bst.find(3) == False     

def test_delete_find2():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert([17, 3, 18, 10, 12, 5, 4])
    bst.delete([18, 10])
    assert bst.find(18) == False and bst.find(10) == False
