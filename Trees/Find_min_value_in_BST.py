from CodeBreakers.Data_structures_interview.Trees.Node import Node
from CodeBreakers.Data_structures_interview.Trees.Binary_search_tree  import BinarySearchTree

#O(h) and worst case O(n)
def findMin(root):
    if(root is None):
        return None
    while root.leftChild:
        root = root.leftChild
    return root.val

def findMin_recursive(root):
    if(root is None):  # check if root exists
        return None
    elif root.leftChild is None:  # check if left child exists
        return root.val  # return if not left child
    else:
        return findMin((root.leftChild))  # recurse onto the left child



BST = BinarySearchTree(6)
BST.insert(20)
BST.insert(-1)

print(findMin(BST.root))