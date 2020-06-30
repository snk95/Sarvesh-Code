from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack

def sortStack_myCode(stack):
    if stack.isEmpty():
        return None
    helper=[]
    while not stack.isEmpty():
        helper.append(stack.pop())
    helper.sort()
    while helper !=[]:
        stack.push(helper.pop())
    return stack



def sortStack(stack):

    tempStack = myStack()

    while stack.isEmpty() is False:

        value = stack.pop()

        if tempStack.top() is not None and value >= int(tempStack.top()):
            # if value is not none and larger, push it at the top of tempStack
            tempStack.push(value)
        else:
            while tempStack.isEmpty() is False:
                stack.push(tempStack.pop())
            # place value as the smallest element in tempStack
            tempStack.push(value)

    # Transfer from tempStack => stack
    while tempStack.isEmpty() is False:
        stack.push(tempStack.pop())

    return stack

def sortStack_dont_recomment(stack):
  stack.stackList.sort(reverse=True)
  return stack


stack = myStack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

sortStack(stack)

# Printing by popping
print([stack.pop() for i in range(stack.size())])
