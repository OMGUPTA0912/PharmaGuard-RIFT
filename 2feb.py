
# 1
#        import math

# # Given data
# x = [0.2, 0.3, 0.5, 1.0, 2.0]
# y = [16, 14, 11, 6, 3]

# n = len(x)

# # Compute z = x^(-0.5)
# z = [1 / math.sqrt(xi) for xi in x]

# # Required sums
# sum_x = sum(x)
# sum_z = sum(z)
# sum_y = sum(y)
# sum_x2 = sum(xi**2 for xi in x)
# sum_z2 = sum(zi**2 for zi in z)
# sum_xz = sum(x[i]*z[i] for i in range(n))
# sum_yz = sum(y[i]*z[i] for i in range(n))

# # Normal equations:
# # sum_y = a*sum_x + b*sum_z
# # sum_yz = a*sum_xz + b*sum_z2

# # Solve using Cramer's rule
# D = sum_x * sum_z2 - sum_z * sum_xz
# Da = sum_y * sum_z2 - sum_z * sum_yz
# Db = sum_x * sum_yz - sum_y * sum_xz

# a = Da / D
# b = Db / D

# print("a =", a)
# print("b =", b)
# print("Equation: y =", a, "* x +", b, "* x^(-0.5)")
       

                                    #   2
# Given points
# x0, y0 = 1, 1
# x1, y1 = 4, 2

# x = 2   # we want sqrt(2)

# # Linear interpolation formula
# y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)

# print("sqrt(2) ≈", y)
                                #    3
# Given data
# x = [1.2, 1.3, 1.4, 1.5]
# y = [1.063, 1.091, 1.119, 1.145]

# xp = 1.35   # point to interpolate
# n = len(x)

# yp = 0

# for i in range(n):
#     L = 1
#     for j in range(n):
#         if i != j:
#             L *= (xp - x[j]) / (x[i] - x[j])
#     yp += y[i] * L

# print("f(1.35) =", yp)
