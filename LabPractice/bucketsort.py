def bucketSort(array):
    minVal=min(array)
    maxVal=max(array)
    bucketRange = (maxVal-minVal)/15
    buckets= [[] for _ in range(15)]

    for num in array:
        index = int((num - minVal)//bucketRange)
        if index==15:
            index=14
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()
    
    sorted=[]
    for bucket in buckets:
        sorted.append(bucket)

    return sorted

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_arr = bucketSort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)