from CodeBreakers.Data_structures_interview.Heaps.MaxHeap import MaxHeap

# O(klogn)
def findKLargest(lst, k):
    heap = MaxHeap()  # Create a MaxHeap
    # Populate the MaxHeap with elements of lst
    heap.buildHeap(lst)
    # Create a list such that:
    # It has k elements where
    # the k elements are the first k
    # elements received from calling removeMax()
    kLargest = [heap.removeMax() for i in range(k)]
    return kLargest


lst = [9, 4, 7, 1, -2, 6, 5]
k = 3
print(findKLargest(lst, k))
