from CodeBreakers.Data_structures_interview.Trees.Node import Node
from CodeBreakers.Data_structures_interview.Trees.Binary_search_tree  import BinarySearchTree

# The time complexity of the code is O(n) as all the nodes of the entire tree have to be traversed.
def findHeight(root):
    if root is None:  # check if root exists
        return -1  # no root means -1 height Also we will not return 0 if the given node is None as the leaf node will have a height of 0.
    else:
        max_sub_tree_height = max(
            findHeight(root.leftChild),
            findHeight(root.rightChild)
        )  # find the max height of the two sub-tree
        # add 1 to max height and return

        return 1 + max_sub_tree_height


BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
BST.insert(10)
BST.insert(14)


print(findHeight(BST.root))
