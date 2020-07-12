from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList

def delete_myCode(lst, value):
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return True

    if lst.get_head().data == value:
        lst.delete_at_head()
        return True

    head_pointer = lst.get_head()
    prev = None
    while head_pointer != None:
        if  head_pointer.data == value:
            prev.next_element = head_pointer.next_element
            head_pointer.next_element = None
            return True

        prev = head_pointer
        head_pointer = head_pointer.next_element

    return False

def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return deleted
    current_node = lst.get_head()  # Get current node
    previous_node = None  # Get previous node
    if current_node.data is value:
        lst.delete_at_head()  # Use the previous function
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node is not None:
        # Node to delete is found
        if value is current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted is False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted

l1=LinkedList()
l1.insert_at_tail_myCode(0)
l1.insert_at_tail_myCode(1)
l1.insert_at_tail_myCode(6)
l1.insert_at_tail_myCode(9)
l1.print_list()
delete_myCode(l1,6)
l1.print_list()
delete_myCode(l1,6)
l1.print_list()
delete_myCode(l1,1)
l1.print_list()