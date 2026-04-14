
# x = [0.2, 0.3, 0.5, 1.0, 2.0]
# y = [16, 14, 11, 6, 3]

# n = len(x)

# X1 = x
# X2 = [xi**(-0.5) for xi in x]

# Sx1x1 = sum(X1[i]*X1[i] for i in range(n))
# Sx2x2 = sum(X2[i]*X2[i] for i in range(n))
# Sx1x2 = sum(X1[i]*X2[i] for i in range(n))
# Syx1  = sum(y[i]*X1[i]  for i in range(n))
# Syx2  = sum(y[i]*X2[i]  for i in range(n))

# # Solve 2 equations using determinant
# D  = Sx1x1*Sx2x2 - Sx1x2*Sx1x2
# Da = Syx1*Sx2x2 - Syx2*Sx1x2
# Db = Sx1x1*Syx2 - Sx1x2*Syx1

# a = Da / D
# b = Db / D

# print("Best fit curve:")
# print(f"y = {a:.4f}x + {b:.4f}x^(-0.5)")
# 2
# x1, y1 = 1, 1
# x2, y2 = 4, 2
# x = 2

# y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)

# print("Value of sqrt(2) ≈", y)
# 3
x = [1.2, 1.3, 1.4, 1.5]
y = [1.063, 1.091, 1.119, 1.145]

xp = 1.35
n = len(x)

result = 0

for i in range(n):
    term = y[i]
    for j in range(n):
        if i != j:
            term *= (xp - x[j]) / (x[i] - x[j])
    result += term

print("Interpolated value at x = 1.35 is", result)
