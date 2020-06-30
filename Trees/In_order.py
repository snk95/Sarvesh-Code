from CodeBreakers.Data_structures_interview.Trees.Node import Node
from CodeBreakers.Data_structures_interview.Trees.Binary_search_tree  import BinarySearchTree


def inOrderPrint(node):
    if node is not None:
        inOrderPrint(node.leftChild)
        print(node.val)
        inOrderPrint(node.rightChild)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)

inOrderPrint(BST.root)
