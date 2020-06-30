from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue

def find_min(g, a, b):
    num_of_vertices = g.vertices
    # A list to hold the history of visited nodes (by default all false)
    # Make a node visited whenever you enqueue it into queue
    visited = [False] * num_of_vertices

    # For keeping track of distance of current_node from source
    distance = [0] * num_of_vertices

    # Create Queue for Breadth First Traversal and enqueue source in it
    queue = myQueue()
    queue.enqueue(a)
    visited[a] = True
    # Traverse while queue is not empty
    while (not queue.isEmpty()):
        # Dequeue a vertex/node from queue and add it to result
        current_node = queue.dequeue()
        # Get adjacent vertices to the current_node from the list,
        # and if they are not already visited then enqueue them in the Queue
        # and also update their distance from `a`
        # by adding 1 in current_nodes's distance
        temp = g.array[current_node].head_node
        while (temp is not None):
            if (not visited[temp.data]) or (temp.data is b):
                queue.enqueue(temp.data)
                visited[temp.data] = True
                distance[temp.data] = distance[current_node] + 1
                if temp.data is b:
                    return distance[b]
            temp = temp.next_element
    # end of while
    return -1


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
print(find_min(g, 1, 5))
