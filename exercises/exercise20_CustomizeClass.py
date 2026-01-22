class MyFib(object):
    def __init__(self):
        self.a = 0
        self.b = 1 

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # 限制打印输出
        if self.a > 1000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            if n < 0:
                raise IndexError("不支持负数索引！")
            a, b = 1, 1
            # 循环几次就是去取索引为几的值
            for _ in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            x = n.start or 0
            y = n.stop
            z = n.step or 1
            if x < 0 or y <= 0 or y is None:
                raise IndexError("索引错误！")
            res = []
            a, b = 0, 1
            # 切片是左闭右开，右索引的值取不到
            for i in range(y-1):
                a, b = b, a + b
                # 取最后一个值会经历中间的值，按需取出来即可
                if i >= x and (i - x) % z == 0:
                    res.append(a)
            return res

if __name__=="__main__":
    fib = MyFib()
    for n in fib:
        print(n)
    print("=" * 20)
    print(fib[10])
    print("=" * 20)
    print(fib[:10:2])    
