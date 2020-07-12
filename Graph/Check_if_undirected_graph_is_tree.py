from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.Graph.Detect_cycle_in_directed_graph import detect_cycle



def helper_method(g, i, visited):
    q = myQueue()
    q.enqueue(i)
    visited[i] = True

    while not q.isEmpty():
        current_node = q.dequeue()
        temp = g.array[current_node].head_node

        while temp is not None:
            if visited[temp.data] is False:
                q.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element

    return visited


def is_tree_myCode (g):
    no_of_vertices = g.vertices

    if no_of_vertices == 0:
        return False

    visited = []

    for i in range(no_of_vertices):
        visited.append(False)

    result = helper_method(g, 0, visited)

    check_cyclic= detect_cycle(g)

    if any(i is False for i in result) or check_cyclic:
        return False
    return True



def is_tree(g):
    # All vertices unvisited
    visited = [False] * g.vertices

    # Check cycle using recursion stack
    # Also mark nodes visited to check connectivity
    if check_cycle(g, 0, visited, -1) is True:
        return False

    # Check if all nodes we visited from the source (graph is connected)
    for i in range(len(visited)):
        # Graph is not connected
        if visited[i] is False:
            return False
    # Not cycle and connected graph
    return True


def check_cycle(g, node, visited, parent):
    # Mark node as visited
    visited[node] = True

    # Pick adjacent node and run recursive DFS
    adjacent = g.array[node].head_node
    while adjacent:
        if visited[adjacent.data] is False:
            if check_cycle(g, adjacent.data, visited, node) is True:
                return True

        # If adjacent is visited and not the parent node of the current node
        elif adjacent.data is not parent:
            # Cycle found
            return True

        adjacent = adjacent.next_element

    return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)

print(is_tree(g))


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


print(is_tree(g1))
print(is_tree(g2))
print(is_tree(g3))
print(is_tree(g4))

