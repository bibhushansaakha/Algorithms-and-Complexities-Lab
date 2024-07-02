def quick_sort(array):
    length = len(array)

    if (length<=1):
        return array
    else:
        pivot = array.pop()

    right = []
    left = []

    for element in array:
        if (element>pivot):
            right.append(element)
        else:
            left.append(element)
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([2,5,4,3,5,6,7,2]))