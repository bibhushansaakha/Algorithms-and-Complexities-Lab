def fractional_knapsack_greedy(profits, weights, capacity):
    n = len(profits)
    items = sorted(zip(profits, weights, range(n)), key=lambda x: x[0]/x[1], reverse=True)
    
    total_profit = 0
    fractions = [0] * n
    
    for profit, weight, index in items:
        if capacity >= weight:
            fractions[index] = 1
            total_profit += profit
            capacity -= weight
        else:
            fraction = capacity / weight
            fractions[index] = fraction
            total_profit += profit * fraction
            break
    
    return total_profit, fractions