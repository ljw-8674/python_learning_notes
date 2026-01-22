count = 0

def hanoi(num, source, auxiliary, target):
    global count
    if num == 1:
        count += 1
        print(f'第{count}次移动圆盘，{source} --> {target}')
        
    else:
        # 第一步：把上面 n−1 个盘子，从 A 移到 B（借助 C）
        hanoi(num-1, source, target, auxiliary)
        
        # 第二步：把第 n 个（最大）盘子，从 A 移到 C
        count += 1
        print(f'第{count}次移动圆盘，{source} --> {target}')

        # 第三步：把 n−1 个盘子，从 B 移到 C（借助 A）
        hanoi(num-1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')
