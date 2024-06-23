from algorithms.brute_force import fractional_knapsack_brute_force, knapsack_01_brute_force
from algorithms.greedy import fractional_knapsack_greedy
from algorithms.dynamic_programming import knapsack_01_dynamic

def main():
    print("Knapsack Problem Solver")
    print("1. Fractional Knapsack (Brute Force)")
    print("2. 0/1 Knapsack (Brute Force)")
    print("3. Fractional Knapsack (Greedy)")
    print("4. 0/1 Knapsack (Dynamic Programming)")
    
    choice = int(input("Enter your choice (1-4): "))
    
    n = int(input("Enter the number of items: "))
    capacity = int(input("Enter the knapsack capacity: "))
    
    weights = [int(x) for x in input("Enter the weights separated by space: ").split()]
    profits = [int(x) for x in input("Enter the profits separated by space: ").split()]
    
    if choice == 1:
        result = fractional_knapsack_brute_force(n, capacity, weights, profits)
    elif choice == 2:
        result = knapsack_01_brute_force(n, capacity, weights, profits)
    elif choice == 3:
        result = fractional_knapsack_greedy(profits, weights, capacity)
    elif choice == 4:
        result = knapsack_01_dynamic(n, capacity, profits, weights)
    else:
        print("Invalid choice")
        return
    
    print("Result:", result)

if __name__ == "__main__":
    main()