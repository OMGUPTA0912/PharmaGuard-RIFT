# import numpy as np

# # Given data
# x = np.array([0, 1, 2, 3], dtype=float)
# y = np.array([1, 2, 33, 244], dtype=float)

# n = len(x)

# # Step 1: intervals
# h = np.diff(x)

# # Step 2: set up system for second derivatives M
# A = np.zeros((n, n))
# rhs = np.zeros(n)

# # Natural boundary conditions
# A[0, 0] = 1
# A[-1, -1] = 1
# rhs[0] = 0
# rhs[-1] = 0

# # Interior equations
# for i in range(1, n - 1):
#     A[i, i - 1] = h[i - 1]
#     A[i, i] = 2 * (h[i - 1] + h[i])
#     A[i, i + 1] = h[i]
#     rhs[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

# # Solve for M
# M = np.linalg.solve(A, rhs)

# # Function to evaluate spline in interval
# def spline_eval(x_val):
#     # find interval index
#     i = np.searchsorted(x, x_val) - 1
#     if i < 0:
#         i = 0
#     if i >= n - 1:
#         i = n - 2

#     hi = h[i]
#     xi, xi1 = x[i], x[i + 1]

#     term1 = M[i] * (xi1 - x_val)**3 / (6 * hi)
#     term2 = M[i + 1] * (x_val - xi)**3 / (6 * hi)
#     term3 = (y[i] - M[i] * hi**2 / 6) * (xi1 - x_val) / hi
#     term4 = (y[i + 1] - M[i + 1] * hi**2 / 6) * (x_val - xi) / hi

#     return term1 + term2 + term3 + term4

# # Estimate f(1.5)
# x_val = 1.5
# f_est = spline_eval(x_val)

# print("Second derivatives M:", M)
# print("Estimated f(1.5) =", f_est)

# 
# import numpy as np

# x = [0, 1, 2, 3]
# y = [1, 2, 33, 244]

# h = 1
# n = 4

# # Second derivatives array
# M = np.zeros(n)

# # Right hand side values
# rhs1 = 6 * (y[2] - 2*y[1] + y[0]) / (h*h)
# rhs2 = 6 * (y[3] - 2*y[2] + y[1]) / (h*h)

# # Coefficient matrix
# A = np.array([[4, 1],
#               [1, 4]])

# B = np.array([rhs1, rhs2])

# # Solve for M1, M2
# M1, M2 = np.linalg.solve(A, B)

# M[1] = M1
# M[2] = M2

# print("Second derivatives M =", M)
# z=1.5
# i=2
# f=(((x[i]-z)**3)*M[i-1]+((z-x[i-1])**3)*M[i])/6*h  +((x[i]-z)*(y[i-1]-((h*h)*M[i-1])/6))/h+((-x[i-1]+z)*(y[i]-((h*h)*M[i])/6))/h
# print(f)



# 
import numpy as np

x = [0, 1, 2, 3]
y = [1, 2, 33, 244]

h = 1
n = 4

# Second derivatives array
M = np.zeros(n)

# Right hand side values
rhs1 = 6 * (y[2] - 2*y[1] + y[0]) / (h*h)
rhs2 = 6 * (y[3] - 2*y[2] + y[1]) / (h*h)

# Coefficient matrix
A = np.array([[4, 1],
              [1, 4]])

B = np.array([rhs1, rhs2])

# Solve for M1, M2
M1, M2 = np.linalg.solve(A, B)

M[1] = M1
M[2] = M2

print("Second derivatives M =", M)


# -------- function to find interval ----------
def find_interval(x, z):
    for i in range(1, len(x)):
        if x[i-1] <= z <= x[i]:
            return i
    return None


# -------- spline function ----------
def spline_value(x, y, M, z):
    i = find_interval(x, z)
    
    if i is None:
        print("z is outside range")
        return None
    
    h = x[i] - x[i-1]
    
    f = (((x[i] - z)**3) * M[i-1] + ((z - x[i-1])**3) * M[i]) / (6*h) \
        + ((x[i] - z) * (y[i-1] - (h*h * M[i-1]) / 6)) / h \
        + ((z - x[i-1]) * (y[i] - (h*h * M[i]) / 6)) / h
    
    return f


# Example
z = 1.5
f = spline_value(x, y, M, z)

print("f(", z, ") =", f)