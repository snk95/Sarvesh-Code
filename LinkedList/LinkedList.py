from CodeBreakers.Data_structures_interview.LinkedList.LinkedList_Node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

    def insert_at_tail_myCode(lst, value):
        new_node = Node(value)
        node = lst.get_head()

        if node is None:
            lst.head_node = new_node
            return

        last = lst.get_head()
        while last.next_element:
            last = last.next_element

        last.next_element = new_node

        return

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node

        return self.head_node

    def delete_at_head(lst):
        # Get Head and firstElement of List
        first_element = lst.get_head()

        # if List is not empty then link head to the
        # nextElement of firstElement.
        if first_element is not None:
            lst.head_node = first_element.next_element
            first_element.next_element = None
        return

    def length(lst):
        # start from the first element
        curr = lst.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr:
            length += 1
            curr = curr.next_element
        return length

    def search(self, dt):
        if self.is_empty():
            return None
        temp = self.head_node
        while (temp is not None):
            if (temp.data is dt):
                return temp
            temp = temp.next_element

        return None

