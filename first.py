import math

def bisection(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid interval")

    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def false_position(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid interval")

    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c


def newton_raphson(f, df, x0, tol=1e-6):
    x = x0
    while abs(f(x)) > tol:
        x = x - f(x) / df(x)
    return x


def secant(f, x0, x1, tol=1e-6):
    while abs(f(x1)) > tol:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
    return x1


# Function (i)
def f1(x):
    return math.exp(2*x) - math.exp(x) - 2

def df1(x):
    return 2*math.exp(2*x) - math.exp(x)


# Function (ii)
def f2(x):
    return x**3 + 4*x**2 - 10

def df2(x):
    return 3*x**2 + 8*x


print("\n----- ROOT FINDING RESULTS -----")

# Function 1
print("\nFunction: e^(2x) - e^x - 2 = 0")

root_bis = bisection(f1, 0, 1)
root_fp = false_position(f1, 0, 1)
root_nr = newton_raphson(f1, df1, 0.5)
root_sec = secant(f1, 0, 1)

print("Bisection       :", root_bis, "f(x) =", f1(root_bis))
print("False Position  :", root_fp, "f(x) =", f1(root_fp))
print("Newton-Raphson  :", root_nr, "f(x) =", f1(root_nr))
print("Secant Method   :", root_sec, "f(x) =", f1(root_sec))


# Function 2
print("\nFunction: x^3 + 4x^2 - 10 = 0")

root_bis = bisection(f2, 1, 2)
root_fp = false_position(f2, 1, 2)
root_nr = newton_raphson(f2, df2, 1.5)
root_sec = secant(f2, 1, 2)

print("Bisection       :", root_bis, "f(x) =", f2(root_bis))
print("False Position  :", root_fp, "f(x) =", f2(root_fp))
print("Newton-Raphson  :", root_nr, "f(x) =", f2(root_nr))
print("Secant Method   :", root_sec, "f(x) =", f2(root_sec))
