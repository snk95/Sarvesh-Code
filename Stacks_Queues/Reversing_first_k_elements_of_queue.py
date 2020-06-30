from CodeBreakers.Data_structures_interview.Stacks_Queues.Queue import myQueue
from CodeBreakers.Data_structures_interview.Stacks_Queues.Stack import myStack

def reverseK_myCode(queue, k):
    q_size = queue.size()
    if k > q_size or k < 0 or k == 0:
        return None

    s = myStack()
    q = myQueue()

    while k > 0:
        s.push(queue.dequeue())
        k -= 1
    while not s.isEmpty():
        q.enqueue(s.pop())
    while not queue.isEmpty():
        q.enqueue(queue.dequeue())
    return q

def reverseK(queue, k):
    if queue.isEmpty() is True or k > queue.size() or k < 0:
        # Handling invalid input
        return None

    stack = myStack()
    for i in range(k):
        stack.push(queue.dequeue())

    while stack.isEmpty() is False:
        queue.enqueue(stack.pop())

    size = queue.size()

    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue



queue = myQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print("the queue before reversing:")
print(queue.queueList)
reverseK(queue, 5)
print("the queue after reversing:")
print(queue.queueList)
