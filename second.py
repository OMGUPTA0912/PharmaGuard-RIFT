import math

def bisect(f,a,b, tol=1e-6):
    if f(a)*f(b) >= 0:
        raise ValueError("wrong interval")
    while abs(b-a) > tol:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
    return (a+b)/2


def false_position(f,a,b,tol=1e-6):
    if f(a)*f(b) >= 0:
        raise ValueError("wrong interval")
    while True:
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c


def secant(f,a,b,tol=1e-6):
    while abs(f(b)) > tol:
        if abs(f(b) - f(a)) < 1e-12:
            raise ValueError("division by zero in secant")
        c = b - f(b)*(b-a)/(f(b)-f(a))
        a, b = b, c
    return b  


def newton(f,df,a,tol=1e-6):
    x = a
    while abs(f(x)) > tol:
        if abs(df(x)) < 1e-12:
            raise ValueError("derivative too small")
        x = x - f(x)/df(x)
    return x


def f1(x):
    return math.exp(2*x) - math.exp(x) - 2


def df1(x):
    return 2*math.exp(2*x) - math.exp(x)


print("root of the equation\n")

try:
    root_bisect = bisect(f1,0,1)
    root_false  = false_position(f1,0,1)
    root_secant = secant(f1,0,1)
    root_newton = newton(f1,df1,0.5) 

    print("Bisection :", root_bisect)
    print("False Pos :", root_false)
    print("Secant    :", root_secant)
    print("Newton    :", root_newton)

except Exception as e:
    print("Error:", e)
