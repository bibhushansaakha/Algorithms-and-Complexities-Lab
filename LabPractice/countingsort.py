def countingSort(Array):
    max_value=max(Array)
    count_array=[0]*(max_value+1)

    for num in Array:
        count_array[num]+=1
        
    sorted_array= []
    for i in range(len(count_array)):
        sorted_array.extend([i]*count_array[i])
    
    return sorted_array

initial_array= [3,4,5,2,4,3,4,5,2,3,5,1,2,3,3]
final_array= countingSort(initial_array)
print(final_array)
