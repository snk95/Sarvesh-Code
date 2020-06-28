def removeEven(List):
    return [i for i in List if i%2 !=0]

def removeEven_my_code(List):
    """
    List iteration works by keeping track of an index, incrementing it each time around the loop until it falls off the end of the list.
    So, if you remove at (or before) the current index, everything from that point until the end shifts one spot to the left.
    But the iterator doesn't know about this, and effectively skips the next element since it is now at the current index rather than the next one.
    However, removing things that are after the current index doesn't affect things.

    """
    if len(List) == 0:
        return None
    for i in List:
        print(i)
        if i % 2 == 0:
            List.remove(i)
            print(List)

    return List

a= [-99, 186, -4, 69, -161, 140, 77, 54, -190, 101, -58, -59, -148, -15, -177,
               159, -92, 43, 52, -6, 107, 72, 182, 189, 104, 19, 83, -49, 111, -172, 109, -51, -98,
               -94, -126, 57, -55, 1, -157, 73, -199, 98, -194, -100, 191, -78, 146, 154, 188, -61, -121, 181, 157,
               -106, 131, -41, -196, -107, -159, 82, 96, 34]
b=[-2,-4,-6,-8]
print(removeEven(a))
#print(removeEven_my_code(b))