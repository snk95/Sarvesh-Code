from CodeBreakers.Data_structures_interview.Trees.Node import Node
from CodeBreakers.Data_structures_interview.Trees.Binary_search_tree  import BinarySearchTree


def findKthMax_myCode(root, k):
    list = []
    if root is not None:
        inorder(root, list)
    return list[-k]


def inorder(node, list):
    if node is not None:
        returned = inorder(node.leftChild, list)
        list.append(node.val)
        inorder(node.rightChild, list)

# O(n) where n is the number of nodes in the tree. The reason is that no matter the value of k is, the function always traverses the entire tree!
def findKthMax(root, k):
    tree = []
    inOrderTraverse(root, tree)  # Get sorted tree list
    if ((len(tree)-k) >= 0) and (k > 0):  # check if k is valid
        return tree[-k]  # return the kth max value
    return None  # return none if no value found


def inOrderTraverse(node, tree):
    # Helper recursive function to traverse the tree inorder
    if node is not None:  # check if node exists
        inOrderTraverse(node.leftChild, tree)  # traverse left sub-tree
        if len(tree) == 0:
            # Append if empty tree
            tree.append(node.val)
        elif tree[-1] is not node.val:
            # Ensure not a duplicate
            tree.append(node.val)  # add current node value
        inOrderTraverse(node.rightChild, tree)  # traverse right sub-tree

def findKthMax_recursive(root, k):
    if k < 1:
        return None
    node = findKthMaxRecursive(root, k)  # get the node at kth position
    if(node is not None):  # check if node received
        return node.val  # return kth node value
    return None  # return None if no node found


counter = 0  # global count variable
current_max = None


# The worst-case complexity of this solution is the same as the previous solution, i.e O(n)O(n).
# But for the best-case scenario, when k = 1, the complexity of this solution will be O(h) where h is the height of the tree.
# Therefore, on average, this solution is more efficient than the previous one.
def findKthMaxRecursive(root, k):
    global counter  # use global counter to track k
    global current_max # track current max
    if(root is None):  # check if root exists
        return None

    # recurse to right for max node
    node = findKthMaxRecursive(root.rightChild, k)
    if(counter is not k) and (root.val is not current_max):
        # Increment counter if kth element is not found
        counter += 1
        current_max = root.val
        node = root
    elif current_max is None:
        # Increment counter if kth element is not found
        # and there is no current_max set
        counter += 1
        current_max = root.val
        node = root
    # Base condition reached as kth largest is found
    if(counter == k):
        return node  # return kth node
    else:
        # Traverse left child if kth element is not reached
        # traverse left tree for kth node
        return findKthMaxRecursive(root.leftChild, k)





BST = BinarySearchTree(6)
BST.insert(1)
BST.insert(133)
BST.insert(12)
print(findKthMax_myCode(BST.root, 3))

BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)

print(findKthMax(BST.root, 4))
