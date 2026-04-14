import math

# Simpson's 1/3 Rule
def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even")
    
    h = (b - a) / n
    s = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            s += 2 * f(x)
        else:
            s += 4 * f(x)
    
    return (h/3) * s


# ----------- Define functions normally -----------

# (a) 1/x
def f1(x):
    return 1 / x

# (b) e^x / x
def f2(x):
    return math.exp(x) / x

# (c) cos^2(x)
def f3(x):
    return math.cos(x) ** 2

# (d) sqrt(1 + 3cos^2(x))
def f4(x):
    return math.sqrt(1 + 3 * (math.cos(x) ** 2))


# ----------- Compute results -----------

res1 = simpson(f1, 1, 3, 4)
res2 = simpson(f2, 1, 2, 4)
res3 = simpson(f3, 0, 3, 6)
res4 = simpson(f4, 0, math.pi, 6)

print("(a):", res1)
print("(b):", res2)
print("(c):", res3)
print("(d):", res4)


# 1
import math

# Function
def f(x):
    return 1 / (1 + x*x)

# Trapezoidal Rule
def trapezoidal(a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        s += f(a + i*h)
    
    return h * s

# Simpson's 1/3 Rule
def simpson(a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule")
    
    h = (b - a) / n
    s = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 0:
            s += 2 * f(a + i*h)
        else:
            s += 4 * f(a + i*h)
    
    return (h/3) * s

# Main
a, b, n = 0, 1, 4

trap = trapezoidal(a, b, n)
simp = simpson(a, b, n)

# Exact value
exact = math.atan(1) - math.atan(0)

print("Trapezoidal:", trap)
print("Simpson:", simp)
print("Exact:", exact)