
# Given data
t = [0, 5, 10, 15, 20]
x = [0, 3, 9, 18, 30]

h = 5   # time interval

# index for t = 10 sec
i = t.index(10)

# (a) Two-point forward difference
v_forward = (x[i+1] - x[i]) / h

# (b) Three-point central difference
v_central3 = (x[i+1] - x[i-1]) / (2*h)

# (c) Five-point central difference
v_central5 = (x[i-2] - 8*x[i-1] + 8*x[i+1] - x[i+2]) / (12*h)

# Acceleration (second derivative, central)
a = (x[i+1] - 2*x[i] + x[i-1]) / (h*h)

print("Velocity at t=10 sec")
print("Two-point forward  =", v_forward)
print("Three-point central =", v_central3)
print("Five-point central  =", v_central5)

print("\nAcceleration at t=10 sec =", a)