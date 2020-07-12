from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList

def remove_duplicates(lst):
    list_len = lst.length()
    if list_len == 0:
        return lst
    elif list_len == 1:
        return lst

    d = dict()
    current = lst.get_head()
    prev = None
    for i in range(0, list_len):
        if current is None:
            break
        if current.data in d:
            next = current.next_element
            prev.next_element = next
            current.next_element = None
            current = next
        else:
            d[current.data] = current.data
            prev = current
            current = current.next_element
    return lst




def remove_duplicates_optimal(self):
    if self.is_empty():
        return

    current_node = self.get_head()
    prev_node = self.get_head()
    # To store values of nodes which we already visited
    visited_nodes = set()
    # If List is not empty and there is more than 1 element in List
    if not self.is_empty() and current_node.next_element:
        while current_node:
            value = current_node.data
            if value in visited_nodes:
                # current_node is already in the HashSet
                # connect prev_node with current_node's next element
                # to remove it
                prev_node.next_element = current_node.next_element
                current_node = current_node.next_element
                continue
            # Visiting currentNode for first time
            visited_nodes.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next_element
    return


# lst = LinkedList()
# lst.insert_at_tail_myCode(6)
# lst.insert_at_tail_myCode(6)
# lst.insert_at_tail_myCode(9)
# lst.insert_at_tail_myCode(10)
# lst.print_list()
# remove_duplicates(lst)
# lst.print_list()