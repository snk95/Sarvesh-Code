from CodeBreakers.Data_structures_interview.LinkedList.LinkedList import LinkedList

def detect_loop(lst):
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False


lst = LinkedList()
lst.insert_at_tail_myCode(6)
lst.insert_at_tail_myCode(4)
lst.insert_at_tail_myCode(9)
lst.insert_at_tail_myCode(10)
lst.print_list()

print(detect_loop(lst))

l2 = LinkedList()

l2.insert_at_head(21)
l2.insert_at_head(14)
l2.insert_at_head(7)

# Adding a loop
head = l2.get_head()
node = l2.get_head()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(l2)) # note that we cant print the linkedlist as there is loop and it will run infinitely