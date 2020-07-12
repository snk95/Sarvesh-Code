from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack


class newQueue_myCode:
    def __init__(self):
        self.mainStack = myStack()
        # Write your code here

        # Inserts Element in the Queue
    def enqueue(self, value):
        helper_stack=myStack()
        while not self.mainStack.isEmpty():
            helper_stack.push(self.mainStack.pop())
        self.mainStack.push(value)
        while not helper_stack.isEmpty():
            self.mainStack.push(helper_stack.pop())
        # Removes Element From Queue

    def dequeue(self):
        return self.mainStack.pop()




class newQueue:
    def __init__(self):
        # Can use size from argument to create stack
        self.mainStack = myStack()
        self.tempStack = myStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into mainStack in O(1)
        if self.mainStack.isEmpty() and self.tempStack.isEmpty():
            self.mainStack.push(value)
            print(str(value) + "init main enqueued")
            return True
        else:
            while self.mainStack.isEmpty() is False:
                tmep = self.mainStack.pop()
                self.tempStack.push(tmep)
            self.mainStack.push(value)
            print(str(value) + "temp enqueued")
            while self.tempStack.isEmpty() is False:
                temp = self.tempStack.pop()
                self.mainStack.push(temp)
            return True

    # Removes Element From Queue
    def dequeue(self):
        if not self.mainStack.isEmpty():
            value = self.mainStack.pop()
            print(str(value) + "main dequeued")
            return value
        # If stack empty then return None
        return None


class newQueue_efficient:
    def __init__(self):
        # Can use size from argument to create stack
        self.mainStack = myStack()
        self.tempStack = myStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into mainStack in O(1)
        self.mainStack.push(value)
        print(str(value) + " enqueued")

        return True

    # Removes Element From Queue
    def dequeue(self):
        # If both stacks are empty, end operation
        if self.tempStack.isEmpty():
            if self.mainStack.isEmpty():
                return None
            # Transfer all elements to tempStack
            while self.mainStack.isEmpty() == False:

                value = self.mainStack.pop()
                self.tempStack.push(value)
        # Pop the first value. This is the oldest element in the queue
        print(self.tempStack.top())
        temp = self.tempStack.pop()
        print(str(temp) + " dequeued")
        return temp

queue = newQueue_efficient()
for i in range(5):
    queue.enqueue(i+1)

print("----------")


queue.dequeue()
queue.enqueue(6)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

