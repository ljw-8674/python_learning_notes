"""
# 1. 捕获异常
try:
    print('【Begin】')
    x = input('Enter an integer：')
    r = 10 / int(x)
    print(f'10 / {x} = {r}:')

except ValueError as e:
    print('ValueError:', e)

except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)

else:
    print('No error!')

finally:
    print('【End】')
"""
"""
# 2. 抛出异常
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

print(divide(10, 2))
print(divide(10, 0))
"""
"""
# 3. 自定义异常类
class MyError(Exception):
    pass

try:
    raise MyError("自定义错误")

except MyError as e:
    print("捕获到自定义异常：", e)
"""
import logging

logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
    
except ZeroDivisionError as e:
    logging.error("发生错误", exc_info=True)
