from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue  import myQueue


def findBin_myCode(number):
    counter = 1
    if number == 0:
        return ["0"]
    elif number == 1:
        return ["1"]
    ans = []
    result=[]
    q = myQueue()

    while counter <= number:

        binary_number = counter
        while binary_number != 1:
            remainder = binary_number % 2
            ans.insert(0, str(remainder))
            binary_number = binary_number // 2
        ans.insert(0, "1")
        s = "".join(ans)
        q.enqueue(s)
        result.append(s)
        ans = []
        counter += 1
    return result

def findBin(number):
    result = []
    queue = myQueue()
    queue.enqueue(1)
    for i in range(number):
        print(i)
        result.append(str(queue.dequeue()))
        print(result)
        s1 = result[i] + "0"
        s2 = result[i] + "1"
        queue.enqueue(s1)
        queue.enqueue(s2)

    return result



print(findBin_myCode(10))
