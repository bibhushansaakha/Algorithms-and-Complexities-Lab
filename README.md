# Algorithms-and-Complexities-Lab

# Tasks:

1. Implement the following sorting algorithms:
(a) Insertion sort
(b) Selection sort
2. Write some test cases to test your program.
3. Generate some random inputs for your program and apply both insertion sort and merge sort algorithms to sort the generated sequence of data. Record the execution times of both algorithms for inputs of different sizes. Plot an input-size vs execution-time graph.
4. Explain your observations.

# Insertion Sort
The function "insertion_sort" has a loop which compares the current element (known as key) with the elements in the already sorted part of the array. It shifts larger elements to the right to make space for the key until it finds the correct position for it. This approach gradually constructs the sorted part of the array. The function repeats this process for every element until the entire array is sorted. In the worst-case scenario, insertion sort has a time complexity of O(n^2).

# Selection Sort
The function "selection_sort" starts by assuming that the current element is the smallest (`min_index = i`). Then, it scans through the unsorted part of the array to find the actual minimum element by comparing it with each subsequent element. If it discovers a smaller element, it updates `min_index` to the index of that smaller element. Once it completes scanning all elements, it swaps the element at index `i` with the minimum element found (`arr[i]` and `arr[min_index]`), effectively positioning the minimum element correctly. This process repeats until the entire array is sorted. Selection sort maintains a time complexity of O(n^2) in all scenarios.



# 2. Unit Test
This unit test script evaluates the correctness of the insertion sort and selection sort algorithms. It imports the `unittest` module along with the implementations of insertion sort (`insertion`) and selection sort (`selection`). Test cases are defined as pairs of input arrays and their corresponding expected sorted outputs.
Each test method iterates over the defined test cases, using `self.subTest()` to isolate individual test cases for easy identification. Within each iteration, the respective sorting function is called with the input array, and the sorted output is compared against the expected output using `self.assertEqual()`. If any assertion fails, `subTest` helps identify which specific test case failed. Finally, if the script is run as the main module, it executes the tests using `unittest.main()`.



# 3. Comparison
This script benchmarks the performance of insertion sort and selection sort algorithms. It imports these algorithms from separate files (`insertion` and `selection`). It also imports necessary modules like `time`, `random`, `matplotlib.pyplot`, `tqdm`, and `datetime`.
The `time_iteration` function generates random data of varying sizes, then times both insertion and selection sort on this data. It returns the time taken for each sorting algorithm.
The `generate_random` function creates an array of random integers within a specified range.
The `compare` function compares the execution time of insertion sort and selection sort algorithms for different input sizes. It iterates over a range of input sizes, timing both sorting algorithms on random data. It also calculates the best and worst-case scenarios for insertion sort. Finally, it plots the time differences for comparison.
The script prompts the user to input the sample size, and then it executes the `compare` function with the provided input size.

# 4. Outputs
![Output graph of comparison between selection sort, insertion sort](/Lab1/graph.png "Fig: Output graph of comparison between selection sort, insertion sort (including its best and worst cases)")


# 5. Observations
Initially, both insertion sort (shown in blue) and selection sort (depicted in orange) work well for smaller inputs (below 3000 in our graph). However, as the input size grows, selection sort's execution time increases a bit faster than insertion sort. Insertion sort usually runs with an average and worst-case time complexity of O(n^2), but it can outperform selection sort when the input is somewhat sorted. Selection sort, on the other hand, always maintains a time complexity of O(n^2), causing it to become slower as the input size rises. The graph reflects these trends as the input size increases.
Additionally, the graph highlights insertion sort's performance in both its best-case scenario (green line) and worst-case scenario (red line). In the best-case scenario, insertion sort operates in linear time (O(n)), happening when the input is already sorted. Conversely, the worst-case scenario occurs when the input is sorted in reverse order, leading to slower performance. As seen in the graph, insertion sort's best-case scenario is much faster than its average and worst-case scenarios, while its worst-case scenario is notably slower than the rest.

# 6. Github Link
https://github.com/bibhushansaakha/Algorithms-and-Complexities-Lab

