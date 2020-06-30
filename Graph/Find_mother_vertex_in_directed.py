from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack


def helper_method(g, i, no_of_vertices):
    q = myQueue()
    q.enqueue(i)
    visited = []

    for j in range(no_of_vertices):
        visited.append(False)

    visited[i] = True
    check_till_end = []
    check_till_end.append(i)

    while not q.isEmpty():
        current_node = q.dequeue()
        temp = g.array[current_node].head_node

        while temp is not None:
            if visited[temp.data] is False:
                check_till_end.append(temp.data)
                q.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element

    if len(check_till_end) == no_of_vertices:
        return i
    return -1


def find_mother_vertex_myCode(g):
    no_of_vertices = g.vertices
    multiple_in_loopcase = []
    result = -1

    if no_of_vertices == 0:
        return None

    for i in range(no_of_vertices):
        result = helper_method(g, i, no_of_vertices)
        if result != -1:
            multiple_in_loopcase.append(result)

    if len(multiple_in_loopcase) > 1:
        return multiple_in_loopcase.pop(0)

    return result

def find_mother_vertex(g):
    # visited[] is used for DFS. Initially all are
    # initialized as not visited
    visited = [False]*(g.vertices)

    # To store last finished vertex (or mother vertex)
    last_v = 0

    # Do a DFS traversal and find the last finished
    # vertex
    for i in range(g.vertices):
        if visited[i] is False:
            perform_DFS(g, i, visited)
            last_v = i
            print("last v",last_v)

    # If there exist mother vertex (or vetices) in given
    # graph, then v must be one (or one of them)

    # Now check if v is actually a mother vertex (or graph
    # has a mother vertex). We basically check if every vertex
    # is reachable from v or not.

    # Reset all values in visited[] as false and do
    # DFS beginning from v to check if all vertices are
    # reachable from it or not.
    visited = [False]*(g.vertices)
    print("calling here")
    perform_DFS(g, last_v, visited)
    if any(i is False for i in visited):
        return -1
    else:
        return last_v


# A recursive function to print DFS starting from v
def perform_DFS(g, node, visited):

    # Mark the current node as visited and print it
    visited[node] = True

    # Recur for all the vertices adjacent to this vertex
    temp = g.array[node].head_node
    while(temp):
        if visited[temp.data] is False:
            print("temp data",temp.data)
            perform_DFS(g, temp.data, visited)
        temp = temp.next_element


# g = Graph(4)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(3, 0)
# g.add_edge(3, 1)
# print(find_mother_vertex(g))


g1 = Graph(4)

g1.add_edge(1, 3)
g1.add_edge(3, 2)

print(find_mother_vertex(g1))
