# 1. 遍历序列
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

# 2. 遍历字典
person = {'name': 'Alice', 'age': 25}

for key in person:
    print(key)

for key, value in person.items():
    print(f'{key} -> {value}')

# 3. 使用 enumerate() 获取索引和值
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors):
    print(index, color)

# 4. 使用 zip() 同时迭代多个序列
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 5. 列表推导式 / 字典推导式 / 集合推导式
numbers = [1, 2, 3, 4]
squared = [x**2 for x in numbers]
print(squared)

# 6. 文件读取
try:
    with open('data.txt', 'r') as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print('没找到文件')

# 7. 使用 iter() 和 next() 自定义迭代
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

# 8. 与生成器结合
def squares(n):
    for i in range(n):
        yield i**2

for num in squares(5):
    print(num)




