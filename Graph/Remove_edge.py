from CodeBreakers.Data_structures_interview.Graph.Graph import Graph
from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList



def remove_edge_myCode(graph, source, dest):

    visited = [False] * graph.vertices

    queue = myQueue()
    queue.enqueue(source)
    visited[source] = True

    while (not queue.isEmpty()):

        source_point = queue.dequeue()

        next_to_source_node = graph.array[source_point].head_node
        if source_point  == source and next_to_source_node.data==dest:
            graph.array[source_point].head_node = None                  # this code is wrong as we need to implement delete method strategy of linkedlist
            next_to_source_node = None

        while (next_to_source_node is not None):
            if (not visited[next_to_source_node.data]):
                queue.enqueue(next_to_source_node.data)
                visited[next_to_source_node.data] = True


            next_to_source_node = next_to_source_node.next_element
    # end of while
    return graph


#O(E)
def remove_edge(graph, source, dest):
    # If empty graph
    if(len(graph.array) == 0):
        return graph
    # check if source valid
    if(source >= len(graph.array) or source < 0):
        return graph
    # check if dest valid
    if(dest >= len(graph.array) or dest < 0):
        return graph
    # Delete by calling delete on head of LinkedList
    # Note: the delete method caters for if the edge does not exist
    graph.array[source].delete(dest)
    return graph

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 0)

g.print_graph()

remove_edge(g, 4, 0)

g.print_graph()




