# 练习1：请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(F'Hello, {x}!')


# 练习2：打印1~100以内的奇数，若为合数则退出。
def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return True
    return False

for i in range(1,101):
    if i %2 != 0:
        if is_composite(i) :
            break
        else:
            print(i)


# 练习3：
import random

target = random.randint(0,100)
count = 0
print("========欢迎来到猜数字游戏！========")
print("我已经想好了一个 1 到 100 之间的数字。你能猜到它是什么吗？")
while True:
    try:
        guess = int(input("请输入你的猜测: "))
        count += 1
        if guess < target:
            print("猜的数字太小了！")
        elif guess > target:
            print("猜的数字太大了！")
        else:
            print(f"恭喜你，猜对了！你猜了 {count} 次。")
            break       
    except ValueError:
        print("请输入一个有效的数字！")
