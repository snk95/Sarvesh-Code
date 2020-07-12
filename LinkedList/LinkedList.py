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

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data is value:
            self.delete_at_head()  # Use the previous function
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

        return deleted

    def remove_duplicates(self):
        if self.is_empty():
            return

        current_node = self.get_head()
        prev_node = self.get_head()
        # To store values of nodes which we already visited
        visited_nodes = set()
        # If List is not empty and there is more than 1 element in List
        if not self.is_empty() and current_node.next_element:
            while current_node:
                value = current_node.data
                if value in visited_nodes:
                    # current_node is already in the HashSet
                    # connect prev_node with current_node's next element
                    # to remove it
                    prev_node.next_element = current_node.next_element
                    current_node = current_node.next_element
                    continue
                # Visiting currentNode for first time
                visited_nodes.add(current_node.data)
                prev_node = current_node
                current_node = current_node.next_element
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

