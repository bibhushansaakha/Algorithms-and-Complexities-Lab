def quicksort(array):
    length = len(array)

    if (length<=1):
        return array
    else:
        pivot = array.pop()

    left =[]
    right = []

    for element in array:
        if element<pivot:
            left.append(element)
        else:
            right.append(element)
    
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([4,3,5,6,2,5,3,7]))