from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList
from CodeBreakers.Data_structures_interview.LinkedList.Insertion_at_tail import insert_at_tail_myCode

#O(n) and space O(1)
def search(lst, value):
    head_pointer = lst.get_head()

    if head_pointer is None:
        return False

    while head_pointer:
        if head_pointer.data == value:
            return True
        head_pointer = head_pointer.next_element
    return False

L1=LinkedList()
insert_at_tail_myCode(L1,1)
insert_at_tail_myCode(L1,2)
L1.insert_at_tail_myCode(3)
L1.insert_at_tail_myCode(5)
L1.print_list()
print(search(L1,5))


