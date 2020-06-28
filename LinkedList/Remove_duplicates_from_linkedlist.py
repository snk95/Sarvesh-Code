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


# lst = LinkedList()
# lst.insert_at_tail_myCode(6)
# lst.insert_at_tail_myCode(6)
# lst.insert_at_tail_myCode(9)
# lst.insert_at_tail_myCode(10)
# lst.print_list()
# remove_duplicates(lst)
# lst.print_list()