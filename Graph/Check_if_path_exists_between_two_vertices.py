from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack


def check_path(g, source, dest):
    # BFS to check path between source and dest
    # Keep track of visited vertices
    visited = [False]*(g.vertices)

    # Create a queue for BFS
    queue = myQueue()

    # Enque source and mark it as visited
    queue.enqueue(source)
    visited[source] = True

    # Loop to traverse the whole graph using BFS
    while not(queue.isEmpty()):

        node = queue.dequeue()

        # Check if dequeued node is the destination
        if node is dest:
            return True

        # Continue BFS by obtaining first element in linked list
        adjacent = g.array[node].head_node
        while adjacent:
            # enqueue adjacent node if it has not been visited
            if visited[adjacent.data] is False:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
            adjacent = adjacent.next_element

    # Destination was not found in the search
    return False


g1 = Graph(9)
g1.add_edge(0, 2)
g1.add_edge(0, 5)
g1.add_edge(2, 3)
g1.add_edge(2, 4)
g1.add_edge(5, 3)
g1.add_edge(5, 6)
g1.add_edge(3, 6)
g1.add_edge(6, 7)
g1.add_edge(6, 8)
g1.add_edge(6, 4)
g1.add_edge(7, 8)
print(check_path(g1, 0, 7))

g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)
print(check_path(g2, 3, 0))
