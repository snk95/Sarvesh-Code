from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack



def dfs_traversal_myCode(g, source):
    result = ""
    stack = myStack()
    ver = g.vertices
    if ver == 0:
        return result

    visited = []
    for i in range(ver):
        visited.append(False)

    stack.push(source)
    while not stack.isEmpty():
        current = stack.pop()
        visited[current] = True
        result += str(current)
        temp = g.array[current].head_node
        while temp is not None:
            stack.push(temp.data)
            temp = temp.next_element

    for i in range(ver):
        if visited[i] is False:
            stack.push(i)
            while not stack.isEmpty():
                current = stack.pop()
                visited[current] = True
                result += str(current)
                temp = g.array[current].head_node
                while temp is not None:
                    stack.push(temp.data)
                    temp = temp.next_element

    return result



def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack = myStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while (stack.isEmpty() is False):
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (visited[temp.data] is False):
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited  # For the above graph it should return "12453"

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if visited[i] is False:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result

g = Graph(7)
num_of_vertices = g.vertices
if(num_of_vertices == 0):
    print("Graph is empty")
elif(num_of_vertices < 0):
    print("Graph cannot have negative vertices")
else:
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    print(dfs_traversal(g, 1))
