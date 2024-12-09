import numpy as np

def print_matrices(x, y, cb):
    print("\nMatrix A:")
    print(x)
    print("\nMatrix B:")
    print(y)
    print("\nMatrix C basis:")
    print(cb)

def print_variables(entering_variable, leaving_variable, pi, c_hat):
    print("\nEntering Variable:")
    print(entering_variable)
    
    print("\nLeaving Variable:")
    print(leaving_variable)
    
    print("\nSimplex Multipliers (pi):")
    print(pi)
    
    print("\nReduced Costs (c_hat):")
    print(c_hat)

def revised_simplex_method(x, y, c, cb, b, n_iterations):
    for iteration in range(1, n_iterations + 1):
        print(f"\nIteration {iteration}:")

        # Calculate simplex multipliers
        Y = np.linalg.inv(y)
        pi = np.dot(cb, Y)

        # Calculate c_hat (reduced costs)
        c_hat = c - np.dot(pi, x)
        
        # Find entering variable (column)
        entering_variable = np.argmax(c_hat)
        
        # Check for optimality
        if c_hat[0, entering_variable] <= 0:
            print("Optimal solution reached.")
            break

        # Choose the entering column
        entering_column = x[:, entering_variable].reshape(-1, 1)
        
        # Calculate ratios and find leaving variable (row)
        ratios = np.divide(b, entering_column)
        leaving_variable_index = np.argmin(ratios)
        
        # Update matrices
        leaving_variable = x[leaving_variable_index, :]
        x[:, entering_variable] = leaving_variable
        y[:, leaving_variable_index] = entering_column.flatten()
        cb[:, leaving_variable_index] = c[:, entering_variable]
        
        # Print matrices for this iteration
        print_matrices(x, y, cb)
        
        # Print variables for this iteration below the matrices
        print_variables(entering_variable, leaving_variable_index, pi, c_hat)

# Input matrices
p1 = np.array([[3,2,1]])
p2 = np.array([[4,1,3]])
p3 = np.array([[2,2,2]])
p4 = np.array([[1],[0],[0]])
p5 = np.array([[0],[1],[0]])
p6 = np.array([[0],[0],[1]])
c = np.array([[1, -1, 2]])
cb = np.array([[2, 0, 3]])
b = np.array([[4], [1], [3]])
n = 3  # Number of iterations

# Concatenate matrices
x = np.hstack((p1, p2, p3))
y = np.hstack((p4, p5, p6))

# Run revised simplex method
revised_simplex_method(x, y, c, cb, b, n)
