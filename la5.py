
import numpy as np

# Given data points
x = np.array([1, 4, 6, 5], dtype=float)
y = np.array([0, 1.3863, 1.7918, 1.6094], dtype=float)

n = len(x)

# Create divided difference table
dd = np.zeros((n, n))
dd[:, 0] = y

# Compute divided differences
for j in range(1, n):
    for i in range(n - j):
        dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (x[i+j] - x[i])

# Function to evaluate Newton polynomial
def newton_interpolation(value):
    result = dd[0][0]
    product = 1.0
    
    for i in range(1, n):
        product *= (value - x[i-1])
        result += dd[0][i] * product
        
    return result

# Estimate ln(2)
ln2_estimate = newton_interpolation(2)

print("Estimated ln(2) using 3rd order Newton polynomial:", ln2_estimate)

# 2

import numpy as np

x1 = np.array([1, 4], dtype=float)
y1 = np.array([0, 1.3863], dtype=float)

def lagrange(x_data, y_data, value):
    n = len(x_data)
    total = 0
    
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (value - x_data[j]) / (x_data[i] - x_data[j])
        total += term
        
    return total

ln2_first_order = lagrange(x1, y1, 2)
print("Estimated ln(2) using 1st order Lagrange:", ln2_first_order)


x2 = np.array([1, 4, 6], dtype=float)
y2 = np.array([0, 1.3863, 1.7918], dtype=float)

ln2_second_order = lagrange(x2, y2, 2)
print("Estimated ln(2) using 2nd order Lagrange:", ln2_second_order)