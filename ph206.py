import math
def expf(x,n_terms=20):
    term=1.0
    ranges=1.0
    for n in range(1,n_terms):
        term*=x/n
        ranges+=term
    return ranges
x=0.5
a=expf(x)
b=math.exp(x)    
print(a)
print(b)
print(abs(b-a))
