# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解。
import math

def quadratic(a, b, c):
    delta = b*b - 4*a*c
    
    if delta < 0:
        return False
    
    elif delta == 0:
        x = -b / (2*a)
        return x
    
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

# 测试:
assert quadratic(1, 2, 5) == False
assert quadratic(1, 2, 1) == -1
assert quadratic(1, 3, -4) == (1.0, -4.0)

print('OK')

