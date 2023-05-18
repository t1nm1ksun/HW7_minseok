import numpy as np

def calculate_eigen(arr):
    eigenvalues, eigenvectors = np.linalg.eig(arr)
    return eigenvalues, eigenvectors

def calculate_cross_product(vec1, vec2):
    cross_product = np.cross(vec1, vec2)
    return cross_product

def solve_linear_equation(A, b):
    x = np.linalg.solve(A, b)
    return x

def main():
    
    arr = np.array([[1, 2],
                    [3, 4]])

    
    eigenvalues, eigenvectors = calculate_eigen(arr)

    
    determinant = np.linalg.det(arr)

    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
    print("Determinant:", determinant)


    vec1 = np.array([1, 2, 3])
    vec2 = np.array([4, 5, 6])

    cross_product = calculate_cross_product(vec1, vec2)

    print("Cross Product:", cross_product)


    A = np.array([[1, 2, -2],
                  [2, 1, -5],
                  [1, -4, 1]])

    b = np.array([[-15],
                  [-21],
                  [18]])

    x = solve_linear_equation(A, b)

    print("Solution :")
    print(x)

if __name__ == "__main__":
    main()
