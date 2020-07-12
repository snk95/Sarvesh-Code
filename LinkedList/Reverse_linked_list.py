
from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList


def reverse_myCode(lst):
    if lst.is_empty():
        return []
    prev=None
    current_node=lst.get_head()
    while current_node.next_element:                  #wrong code
                                                      # dont refer this solution
        prev = current_node
        prev.next_element.next_element = prev
        prev.next_element = None
        current_node = current_node.next_element
    current_node.next_element=prev
    lst.head_node=current_node
    return lst

def reverse(lst):
  # To reverse linked, we need to keep track of three things
  previous = None # Maintain track of the previous node
  current = lst.get_head() # The current node
  next = None # The next node in the list

  #Reversal
  while current:
    next = current.next_element
    current.next_element = previous
    previous = current
    current = next

    #Set the last element as the new head node
    lst.head_node = previous
  return lst

lst = LinkedList()
lst.insert_at_head(6)
lst.insert_at_head(4)
lst.insert_at_head(9)
lst.insert_at_head(10)
lst.print_list()

reverse_myCode(lst)
lst.print_list()

