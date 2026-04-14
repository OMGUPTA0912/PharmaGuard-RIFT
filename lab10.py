# 1
def taylor_a(h, steps):
    x = 0
    y = 0
    
    for i in range(steps):
        y1 = x**2 + y**2
        y2 = 2*x + 2*y*y1
        y3 = 2 + 2*(y1**2) + 2*y*y2
        
        y = y + h*y1 + (h**2/2)*y2 + (h**3/6)*y3
        x += h
        
        print(f"x={x:.2f}, y={y:.6f}")
        
taylor_a(0.05, 2)
# 1b
import math

def taylor_b(h, steps):
    x = 0
    y = 0
    
    for i in range(steps):
        y1 = x * math.exp(y)
        y2 = math.exp(y) + x * math.exp(y) * y1
        y3 = math.exp(y)*y1 + math.exp(y)*y1 + x*math.exp(y)*(y1**2) + x*math.exp(y)*y2
        
        y = y + h*y1 + (h**2/2)*y2 + (h**3/6)*y3
        x += h
        
        print(f"x={x:.2f}, y={y:.6f}")

taylor_b(0.05, 2)
# 2
# import math

# def euler(h):
#     x = 1
#     y = 1
    
#     while x < 3:
#         y = y + h * (3 * x**2 * y)
#         x += h
    
#     return y

# # Compare different h
# for h in [0.5, 0.2, 0.1, 0.01]:
#     approx = euler(h)
#     exact = math.exp(3**3 - 1)
#     print(f"h={h}, approx={approx:.6f}, exact={exact:.6f}")
    # 3
   


def modified_euler(h):
    x = 1
    y = 2
    
    while x < 2:
        f1 = 2*y/x
        
        y_pred = y + h*f1
        x_next = x + h
        
        f2 = 2*y_pred/x_next
        
        y = y + (h/2)*(f1 + f2)
        x = x_next
    
    return y

approx = modified_euler(0.1)
exact = 2*(2**2)

print(f"Approx = {approx:.6f}, Exact = {exact}")   