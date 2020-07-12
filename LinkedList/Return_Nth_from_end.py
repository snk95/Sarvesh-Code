from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList

def find_nth_myCode(lst, n):
    list_len=lst.length()
    if list_len ==0:
        return -1
    start_index=list_len-n+1
    if start_index <0 or start_index > list_len:
        return -1
    pointer=lst.get_head()
    while start_index!=1:
        pointer=pointer.next_element
        start_index-=1
    return pointer.data

def find_nth(lst, n):

    if lst.is_empty():
        return -1

    nth_node = lst.get_head()  # This iterator will reach the Nth node
    end_node = lst.get_head()  # This iterator will reach the end of the list

    count = 0
    if not lst.is_empty():
        while count < n:
            if end_node is None:
                return -1
            end_node = end_node.next_element
            count += 1

    while end_node is not None:
        end_node = end_node.next_element
        nth_node = nth_node.next_element

    return nth_node.data


lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)


lst.print_list()
print(find_nth(lst, 5))
print(find_nth(lst, 1))
print(find_nth(lst, 10))

