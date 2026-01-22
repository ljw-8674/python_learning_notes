# 可变位置参数
def f1(*args):
    print(f'args: {args}')

f1()
f1(1)
f1(1, 2, 3)

# 位置参数 + 可变位置参数
def f2(a, *args):
    print(f'a: {a}, args: {args}')

f2(1)
f2(1, 2, 3)

# 位置参数 + 可变位置参数 + 关键字参数
def f3(a, *args, b):
    print(f'a: {a}, args: {args}, b: {b}')

f3(1, b=2)
# f3(1, 2, 3) # 会报错

# 位置参数 + 可变关键字参数
def f4(a, **kwargs):
    print(f'a: {a}, kwargs: {kwargs}')

f4(1, x=10, y=20)

# 5种参数
def f5(a, b=1, *args, c, d=2, **kwargs):
    print(f'a: {a}, b: {b}, args: {args}, c: {c}, d: {d}, kwargs: {kwargs}')

f5(10, 20, 30, 40, c=50, x=60)

# 默认参数只在函数定义时创建一次，而不是每次调用都创建。
def f6(x, lst=[]):
    lst.append(x)
    return lst

print(f6(1))
print(f6(2))
print(f6(3))

# 默认值的参数，必须放在所有不带默认值参数的后面
# def f7(a=1, b):
    # print(f'a: {a}, b: {b}')

# *只是分隔符，其后面的参数只能用关键字方式传递
def connect(*, host, port):
    print(host, port)

connect(host="localhost", port=3306)



