
# Gauss Elimination Method
# Solves a system of linear equations

def gauss_elimination(a):
    n = len(a)

    # Forward elimination
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = a[i][k] / a[k][k]
            for j in range(k, n + 1):
                a[i][j] -= factor * a[k][j]

    # Back substitution
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]

    return x


# Augmented matrix
A = [
    [4, -1, 1, -5],
    [2,  2, 3, 10],
    [5, -2, 6,  1]
]

solution = gauss_elimination(A)

print("Solution using Gauss Elimination:")
print(f"x = {solution[0]:.2f}")
print(f"y = {solution[1]:.2f}")
print(f"z = {solution[2]:.2f}")
# Gauss-Jordan Method
# Converts matrix into reduced row echelon form

def gauss_jordan(a):
    n = len(a)

    for i in range(n):
        # Make the diagonal element 1
        pivot = a[i][i]
        for j in range(n + 1):
            a[i][j] /= pivot

        # Make other elements in column zero
        for k in range(n):
            if k != i:
                factor = a[k][i]
                for j in range(n + 1):
                    a[k][j] -= factor * a[i][j]

    # Extract solution
    return [a[i][n] for i in range(n)]


# Augmented matrix
A = [
    [2, 1, 1, 10],
    [3, 2, 3, 18],
    [1, 4, 9, 16]
]

solution = gauss_jordan(A)

print("Solution using Gauss-Jordan Method:")
print(f"x = {solution[0]:.2f}")
print(f"y = {solution[1]:.2f}")
print(f"z = {solution[2]:.2f}")
