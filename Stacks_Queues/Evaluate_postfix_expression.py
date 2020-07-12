from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack


def evaluatePostFix_myCode(exp):
    stack=myStack()

    for i in exp:
        if i.isdigit():
            stack.push(i)
        else:
            num1=stack.pop()
            num2=stack.pop()
            result=eval(num2+i+num1)
            print(result)
            stack.push(str(result))

    return stack.pop()

def evaluatePostFix(exp):
    stack = myStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"

print("Result: " + str(evaluatePostFix("921*-8-4+")))
print("Result: " + str(evaluatePostFix("921*-8--4+")))





