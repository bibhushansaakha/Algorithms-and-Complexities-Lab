def fractional_knapsack_brute_force(n, capacity, weights, profits):
    combinations = [bin(i)[2:].zfill(n) for i in range(2**n)]
    best_combination = None
    max_profit = 0
    best_weight = 0

    for comb in combinations:
        current_weight = 0
        current_profit = 0
        for i in range(n):
            if comb[i] == '1' and current_weight + weights[i] <= capacity:
                current_weight += weights[i]
                current_profit += profits[i]
        
        if current_profit > max_profit:
            max_profit = current_profit
            best_combination = [int(x) for x in comb]
            best_weight = current_weight

    return best_combination, best_weight, max_profit
def knapsack_01_brute_force(n, capacity, weights, profits):
    combinations = [bin(i)[2:].zfill(n) for i in range(2**n)]
    best_combination = None
    max_profit = 0
    best_weight = 0

    for comb in combinations:
        current_weight = 0
        current_profit = 0
        for i in range(n):
            if comb[i] == '1':
                if current_weight + weights[i] <= capacity:
                    current_weight += weights[i]
                    current_profit += profits[i]
                else:
                    break
        
        if current_profit > max_profit:
            max_profit = current_profit
            best_combination = [int(x) for x in comb]
            best_weight = current_weight

    return best_combination, best_weight, max_profit