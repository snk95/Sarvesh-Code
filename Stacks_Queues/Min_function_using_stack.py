from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack

class minStack:
    # Constructor
    def __init__(self):
        self.minStack = myStack()
        self.mainStack = myStack()
        return

        # Removes and returns value from minStack
    def pop(self):
        self.minStack.pop()
        return self.mainStack.pop()

        # Pushes values into minStack
    def push(self, value):
        self.mainStack.push(value)
        if(self.minStack.isEmpty() or self.minStack.top() > value):
            self.minStack.push(value)
        else:
            self.minStack.push(self.minStack.top())


        # Returns minimum value from newStack in O(1) Time
    def min(self):
        if not self.minStack.isEmpty():
            return self.minStack.top()


stack = minStack()
stack.push(5)

stack.push(2)
stack.push(4)
stack.push(1)
stack.push(3)
stack.push(0)

print(stack.mainStack.stackList)
print("minimum value: " + str(stack.min()))
print(stack.minStack.stackList)
print("-------------------------------------------------")
stack.pop()
print(stack.mainStack.stackList)
print("minimum value: " + str(stack.min()))
print(stack.minStack.stackList)