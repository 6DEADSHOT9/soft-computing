import numpy as np

def single_point_crossover(A, B, x):
    """
    Performs single point crossover between two parent chromosomes
    """
    A_new = np.append(A[:x], B[x:])
    B_new = np.append(B[:x], A[x:])
    return A_new, B_new

def multi_point_crossover(A, B, y):
    """
    Performs multi-point crossover between two parent chromosomes
    """
    for i in y:
        A, B = single_point_crossover(A, B, i)
    return A, B

def uniform_crossover(A, B, P):
    """
    Performs uniform crossover between two parent chromosomes
    based on probability array P
    """
    # Create copies of input arrays to avoid modifying originals
    A_new = A.copy()
    B_new = B.copy()
    
    for i in range(len(P)):
        if P[i] < 0.5:
            temp = A_new[i]
            A_new[i] = B_new[i]
            B_new[i] = temp
    return A_new, B_new

# Example usage
if __name__ == "__main__":
    # Initialize parent chromosomes
    A = np.array([4, 8, 6, 5, 9, 2, 6, 9, 2, 3])
    B = np.array([9, 8, 7, 4, 5, 2, 3, 5, 8, 7])
    
    # Single point crossover
    x = 2  # crossover point
    A_new, B_new = single_point_crossover(A, B, x)
    print("Single Point Crossover")
    print("Parent A:", A)
    print("Parent B:", B)
    print("A_new:", A_new)
    print("B_new:", B_new)
    print()
    
    # Multi point crossover
    y = np.array([2, 5])  # List of crossover points
    m_new, n_new = multi_point_crossover(A, B, y)
    print("Multi Point Crossover")
    print("Parent A:", A)
    print("Parent B:", B)
    print("M_new:", m_new)
    print("N_new:", n_new)
    print()
    
    # Uniform crossover
    P = np.random.rand(10)  # Probability array of length 10
    U_new, V_new = uniform_crossover(A, B, P)
    print("Uniform Crossover")
    print("Parent A:", A)
    print("Parent B:", B)
    print("Probability array P:", P)
    print("U_new:", U_new)
    print("V_new:", V_new)
