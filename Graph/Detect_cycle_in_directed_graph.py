from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack



def helper_method(g, i, visited):
    q = myQueue()
    q.enqueue(i)
    visited[i] = True

    while not q.isEmpty():

        current_node = q.dequeue()
        temp = g.array[current_node].head_node

        while temp is not None:
            if visited[temp.data] is True:
                return True, visited
            visited[temp.data] = True
            temp = temp.next_element

    return False, visited


def detect_cycle_myCode(g):
    no_of_vertices = g.vertices

    if no_of_vertices == 0:
        return False
    result = False
    visited = []

    for i in range(no_of_vertices):
        visited.append(False)

    for i in range(no_of_vertices):
        if visited[i] is False:
            result, visited = helper_method(g, i, visited)
        if result is True:
            return True

    return False

def detect_cycle(g):
    # visited list to keep track of the nodes that have been visited
    # since the beginning of the algorithm
    visited = [False] * g.vertices

    # rec_node_stack keeps track of the nodes which are part of the
    # current recursive call
    rec_node_stack = [False] * g.vertices

    for node in range(g.vertices):
        # DFS recursion call
        if detect_cycle_rec(g, node, visited, rec_node_stack):
            return True

    return False


def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in recursion stack. Cycle found.
    if (rec_node_stack[node]):
        return True

    # It has been visited before this recursion
    if (visited[node]):
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True

    head_node = g.array[node].head_node
    while(head_node is not None):
        # Pick adjacent node and call it recursively
        adjacent = head_node.data

        # If the node is visited again in the same recursion => Cycle found
        if (detect_cycle_rec(g, adjacent, visited, rec_node_stack)):
            return True
        head_node = head_node.next_element

    # remove the node from the recursive call
    rec_node_stack[node] = False
    return False


g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(3, 0)

g2 = Graph(3)
g2.add_edge(0, 1)
g2.add_edge(1, 2)

g3 = Graph(4)
g3.add_edge(0, 1)
g3.add_edge(0, 2)
g3.add_edge(0, 3)

g4 = Graph(5)
g4.add_edge(0, 1)
g4.add_edge(1, 2)
g4.add_edge(0, 3)
g4.add_edge(3, 4)


# print(detect_cycle(g1))
# print(detect_cycle(g2))
# print(detect_cycle(g3))
# print(detect_cycle(g4))

