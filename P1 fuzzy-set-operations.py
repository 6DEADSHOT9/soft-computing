def union(A, B):
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
    Y = dict()
    
    print("UNION")
    print('The First Fuzzy set is:', A)
    print('The Second Fuzzy set is:', B)
    
    for A_key, B_key in zip(A,B):
        A_value = A[A_key]
        B_value = B[B_key]
        if A_value > B_value:
            Y[A_key] = A_value
        else:
            Y[B_key] = B_value
    print('Fuzzy Set Union is:', Y)

def intersection(A, B):
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
    Y = dict()
    
    print("INTERSECTION")
    print('The First Fuzzy set is:', A)
    print('The Second Fuzzy set is:', B)
    
    for A_key, B_key in zip(A,B):
        A_value = A[A_key]
        B_value = B[B_key]
        if A_value < B_value:
            Y[A_key] = A_value
        else:
            Y[B_key] = B_value
    print('Fuzzy Set Intersection:', Y)

def complement(A, B):
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    Y = dict()
    
    print('COMPLEMENT')
    print('The Fuzzy Set is:', A)
    
    for A_Key in A:
        Y[A_Key] = 1 - A[A_Key]
    print('Fuzzy set Complement is:', Y)

def difference(A, B):
    A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
    Y = dict()
    
    print("DIFFERENCE")
    print('The First Fuzzy set:', A)
    print('The Second Fuzzy set:', B)
    
    for A_Key, B_Key in zip(A,B):
        A_value = A[A_Key]
        B_value = B[B_Key]
        B_value = 1 - B_value
        if A_value < B_value:
            Y[A_Key] = A_value
        else:
            Y[B_Key] = B_value
    print('Fuzzy Set Difference is:', Y)

def cartesian():
    n = int(input("Enter number of elements in first set(A):"))
    A = []
    B = []
    
    print("CARTESIAN PRODUCT")
    print('Enter elements for A:')
    for i in range(0,n):
        ele = float(input())
        A.append(ele)
    
    m = int(input("\nEnter number of elements in second set(B):"))
    print("Enter elements for B:")
    for i in range(0,m):
        ele = float(input())
        B.append(ele)
    
    print("A={"+str(A)[1:-1]+"}")
    print("B={"+str(B)[1:-1]+"}")
    
    cart_prod = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            cart_prod[i][j] = min(A[i], B[j])
    
    print("A x B =")
    for i in range(n):
        for j in range(m):
            print(cart_prod[i][j], end=" ")
        print("\n")
    return

def main():
    while True:
        print("1.Union")
        print("2.Intersection")
        print("3.Complement")
        print("4.Difference")
        print("5.Cartesian Product")
        print("6.EXIT")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            union(A,B)
        elif choice == 2:
            intersection(A,B)
        elif choice == 3:
            complement(A,B)
        elif choice == 4:
            difference(A,B)
        elif choice == 5:
            cartesian()
        elif choice == 6:
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
