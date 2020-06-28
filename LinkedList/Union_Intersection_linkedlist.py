from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList
from CodeBreakers.Data_structures_interview.LinkedList.Remove_duplicates_from_linkedlist import remove_duplicates

def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    start = list1.get_head()

    # Traverse the first list till the tail
    while start.next_element:
        start = start.next_element

    # Link last element of first list to the first element of second list
    start.next_element = list2.get_head()
    remove_duplicates(list1)
    return list1

# better time complexity in hashing chapter
def intersection(list1, list2):

    result = LinkedList()
    current_node = list1.get_head()

    # Traversing list1 and searching in list2
    # insert in result if the value exists
    while current_node is not None:
        value = current_node.data
        if list2.search(value) is not None:
            result.insert_at_head(value)
        current_node = current_node.next_element

    # Remove duplicates if any
    remove_duplicates(result)
    return result


ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(7)

print("List 1")
ulist1.print_list()

ulist2.insert_at_head(7)
ulist2.insert_at_head(14)
ulist2.insert_at_head(8)

print("List 2")
ulist2.print_list()

new_list = union(ulist1,ulist2)

print("Union of list 1 and 2")
new_list.print_list()

print("****************************")
ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)
ilist1.print_list()

ilist2.insert_at_head(15)
ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.print_list()
print("Intersection of list 1 and 2")
lst = intersection(ilist1, ilist2)
lst.print_list()
