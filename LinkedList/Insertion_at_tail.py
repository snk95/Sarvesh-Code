from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList
from CodeBreakers.Data_structures_interview.LinkedList.LinkedList_Node import Node


def insert_at_tail_myCode(lst, value):
    new_node = Node(value)
    node=lst.get_head()

    if node is None:
        lst.head_node = new_node
        return

    last = lst.get_head()
    while last.next_element:
        last = last.next_element

    last.next_element = new_node
    return


def insert_at_tail(lst, value):
    # Creating a new node
    new_node = Node(value)

    # Check if the list is empty, if it is simply point head to new node
    if lst.get_head() is None:
        lst.head_node = new_node
        return

    # if list not empty, traverse the list to the last node
    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element

    # Set the nextElement of the previous node to new node
    temp.next_element = new_node
    return


# l1=LinkedList()
# insert_at_tail_myCode(l1,0)
# l1.print_list()
# insert_at_tail_myCode(l1,1)
# l1.print_list()
# insert_at_tail_myCode(l1,2)
# l1.print_list()
# insert_at_tail_myCode(l1,3)
# l1.print_list()