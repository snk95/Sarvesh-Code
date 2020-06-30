from CodeBreakers.Data_structures_interview.Trees.Node import Node
from CodeBreakers.Data_structures_interview.Trees.Binary_search_tree  import BinarySearchTree

# O(logn)
def findAncestors(root, k):
    if not root:  # check if root exists
        return None
    ancestors = []  # empty list of ancestors
    current = root  # iterator current set to root

    while current is not None:  # iterate until we reach None
        if k > current.val:  # go right
            ancestors.append(current.val)
            current = current.rightChild
        elif k < current.val:  # go left
            ancestors.append(current.val)
            current = current.leftChild
        else:  # when k == current.val
            return ancestors[::-1]
    return []

# O(n)
def findAncestors_recursive(root, k):
    result = []
    recfindAncestors(root, k, result)  # recursively find ancestors
    return str(result)  # return a string of ancestors


def recfindAncestors(root, k, result):
    if root is None:  # check if root exists
        return False
    elif root.val is k:  # check if val is k
        return True
    recur_left = recfindAncestors(root.leftChild, k, result)
    recur_right = recfindAncestors(root.rightChild, k, result)
    if recur_left or recur_right:
        # if recursive find in either left or right sub tree
        # append root value and return true
        result.append(root.val)
        return True
    return False  # return false if all failed


BST = BinarySearchTree(6)
BST.insert(1)
BST.insert(133)
BST.insert(12)
print(findAncestors(BST.root, 12))