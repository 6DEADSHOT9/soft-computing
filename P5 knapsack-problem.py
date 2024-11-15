def knapsack(max_capacity, weights, values, n):
    """
    Solves the 0/1 Knapsack problem using dynamic programming
    
    Parameters:
    max_capacity (int): Maximum weight capacity of the knapsack
    weights (list): List of weights of the items
    values (list): List of values of the items
    n (int): Number of items
    
    Returns:
    int: Maximum value that can be achieved
    list: Items selected (0 or 1 for each item)
    """
    # Initialize the 2D array with zeros
    K = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]
    
    # Keep track of selected items
    selected = [[False for x in range(max_capacity + 1)] for x in range(n + 1)]
    
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(max_capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                value1 = values[i-1] + K[i-1][w-weights[i-1]]
                value2 = K[i-1][w]
                if value1 > value2:
                    K[i][w] = value1
                    selected[i][w] = True
                else:
                    K[i][w] = value2
                    selected[i][w] = False
            else:
                K[i][w] = K[i-1][w]
                selected[i][w] = False
    
    # Find selected items
    selected_items = []
    w = max_capacity
    for i in range(n, 0, -1):
        if selected[i][w]:
            selected_items.append(i-1)
            w = w - weights[i-1]
    
    return K[n][max_capacity], selected_items

def print_selected_items(selected_items, weights, values):
    """
    Prints details of selected items
    """
    print("\nSelected items:")
    print("Index\tWeight\tValue")
    total_weight = 0
    total_value = 0
    for i in selected_items:
        print(f"{i}\t{weights[i]}\t{values[i]}")
        total_weight += weights[i]
        total_value += values[i]
    print(f"\nTotal weight: {total_weight}")
    print(f"Total value: {total_value}")

# Driver code
if __name__ == "__main__":
    # Example problem
    max_capacity = 10
    values = [50, 40, 80, 10]
    weights = [3, 4, 6, 2]
    n = len(values)
    
    print("Knapsack Problem")
    print("Maximum capacity:", max_capacity)
    print("\nAvailable items:")
    print("Index\tWeight\tValue")
    for i in range(n):
        print(f"{i}\t{weights[i]}\t{values[i]}")
    
    # Solve knapsack
    max_value, selected_items = knapsack(max_capacity, weights, values, n)
    print(f"\nMaximum value that can be obtained: {max_value}")
    
    # Print selected items
    print_selected_items(selected_items, weights, values)
    
    # Additional example
    print("\n--- Another Example ---")
    max_capacity = 15
    values = [60, 100, 120, 80, 30]
    weights = [5, 8, 12, 6, 4]
    n = len(values)
    
    print("Knapsack Problem")
    print("Maximum capacity:", max_capacity)
    print("\nAvailable items:")
    print("Index\tWeight\tValue")
    for i in range(n):
        print(f"{i}\t{weights[i]}\t{values[i]}")
    
    max_value, selected_items = knapsack(max_capacity, weights, values, n)
    print(f"\nMaximum value that can be obtained: {max_value}")
    print_selected_items(selected_items, weights, values)
