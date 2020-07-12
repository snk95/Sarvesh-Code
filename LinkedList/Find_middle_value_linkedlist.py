from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList


def find_mid_myCode(lst):
    list_len = lst.length()

    if list_len == 0:
        return -1

    count=0
    if list_len % 2 == 0:
        count = list_len // 2
    elif list_len % 2 != 0:
        count = list_len // 2 + 1

    list_pointer = lst.get_head()
    while count != 1:
        list_pointer = list_pointer.next_element
        count -= 1
    return list_pointer.data

def find_mid(lst):
    if lst.is_empty():
        return -1
    current_node = lst.get_head()
    if current_node.next_element is None:
        # Only 1 element exist in array so return its value.
        return current_node.data

    mid_node = current_node
    current_node = current_node.next_element.next_element
    # Move mid_node (Slower) one step at a time
    # Move current_node (Faster) two steps at a time
    # When current_node reaches at end, mid_node will be at the middle of List
    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
            current_node = current_node.next_element
    if mid_node:
        return mid_node.data
    return -1


lst = LinkedList()
lst.insert_at_tail_myCode(6)
lst.insert_at_tail_myCode(4)
lst.insert_at_tail_myCode(9)
lst.insert_at_tail_myCode(10)
lst.print_list()
print(find_mid_myCode(lst))