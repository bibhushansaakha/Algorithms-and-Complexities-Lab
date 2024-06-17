def knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0

    for i in range(2**n):
        total_weight = 0
        total_value = 0
        for j in range(n):
            if i & (1 << j):
                total_weight += weights[j]
                total_value += values[j]
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value

    return max_value

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print(knapsack(weights, values, capacity))
