from CodeBreakers.Data_structures_interview.Trees.Node import Node
from CodeBreakers.Data_structures_interview.Trees.Binary_search_tree  import BinarySearchTree

# The time complexity of this solution is in O(n)
def findKNodes(root, k):
    res = []
    findK(root, k, res)  # recurse the tree for node at k distance
    return str(res)


def findK(root, k, res):
    if root is None:  # return if root does not exist
        return 
    if k == 0:
        res.append(root.val)  # append as root is kth node
    else:
        # check recursively in both sub-tree for kth node
        findK(root.leftChild, k - 1, res)
        findK(root.rightChild, k - 1, res)


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
print(findKNodes(BST.root, 2))
