from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack


def isBalanced(exp):
    closing = ['}', ')', ']']
    stack = myStack()
    for character in exp:
        if character in closing:
            if stack.isEmpty():
                return False
            topElement = stack.pop()
            if (character == '}' and topElement !='{'):
                return False
            if (character == ')' and topElement != '('):
                return False
            if (character == ']' and topElement != '['):
                return False
        else:
            stack.push(character)
    if (stack.isEmpty() is False):
        return False
    return True


# to test your logic
inputString = "{[(a)]}" #balanced string
print(inputString + " " + str(isBalanced(inputString)))

inputString = "{[([({))]}}" #imbalanced string
print(inputString + " " + str(isBalanced(inputString)))


inputString = "" # an empty string is balanced
print(inputString + " " + str(isBalanced(inputString)))
