from insertion import insertion_sort
from selection import selection_sort
import time
import random
import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import datetime

def time_iteration():
    num_values = random.randint(500,5000)
    rand_data = random.sample(range(1,10000),num_values)
    initial_time = datetime.now()
    sorted = insertion_sort(rand_data.copy())
    insertion_time = datetime.now()-initial_time
    initial_time = datetime.now()
    sorted = selection_sort(rand_data.copy())
    selection_time = datetime.now()-initial_time
    return {"num_values":num_values, "insertion_time":insertion_time.total_seconds(),"selection_time":selection_time.total_seconds()}

# Function to generate n random numbers
def generate_random(n: int):
    arr = []
    for i in range(n):
        arr.append(random.randint(-1000, 10000))
    return arr


# Function to compare the time taken by the sorting algorithms
def compare(input_size):
    select_diff, insert_diff, insert_diff_best, insert_diff_worst = [], [], [], []
    number = []
    time_list = []
    for i in tqdm(range(1,input_size)):
        time_list.append(time_iteration())

    for i in range(10, input_size, 30):
        random_array = generate_random(i)

        # Time the sorting algorithms
        selection_start = time.time()
        selection_sorted = selection_sort(random_array.copy())
        selection_end = time.time()

        insertion_start = time.time()
        insertion_sorted = insertion_sort(random_array.copy())
        insertion_end = time.time()

        # Find best and worst case for insertion sort
        insertion_start_best = time.time()
        insertion_sort(insertion_sorted.copy())
        insertion_end_best = time.time()

        insertion_sorted_reverse = insertion_sorted[::-1]
        insertion_start_worst = time.time()
        insertion_sort(insertion_sorted_reverse.copy())
        insertion_end_worst = time.time()

       # Append the time differences to the respective lists
        select_diff.append(selection_end - selection_start)
        insert_diff.append(insertion_end - insertion_start)
        insert_diff_best.append(insertion_end_best - insertion_start_best)
        insert_diff_worst.append(insertion_end_worst - insertion_start_worst)
        number.append(i)

    # Make a plot of the time differences
    fig, ax = plt.subplots()
    ax.plot(number, insert_diff, label="Insertion Sort")
    ax.plot(number, select_diff, label="Selection Sort")
    ax.plot(number, insert_diff_best, label="Insertion Sort (Best Case)")
    ax.plot(number, insert_diff_worst, label="Insertion Sort (Worst Case)")

    ax.legend(loc="upper left")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (s)")
    plt.show()


if __name__ == "__main__":
    input_size = int(input("Enter Sample Size: "))
    compare(input_size)