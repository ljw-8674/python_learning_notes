class MyFib(object):
    def __init__(self):
        self.a = 1
        self.b = 1 

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # if self.a > 100:
        #     raise StopIteration()
        return self.a
	
    def __getitem__(self, n):
        # 不考虑负数索引
        if isinstance(n, int):
            a, b = 1, 1
            for _ in range(n):
                a, b = b, a + b
            return a
        
        if isinstance(n, slice):
            a, b = 1, 1
            L = []
            start = n.start or 0
            stop = n.stop
            step = n.step or 1
            for i in range(start, stop, step):
                for _ in range(i):
                    a, b = b, a + b
                L.append(a)
                a, b = 1, 1
            return L

# 1, 1, 2, 3, 5, 8, 13, ...
# 0, 1, 2, 3, 4, 5, 6, ...
nums = MyFib()
print(nums)
print(nums[6])
print(nums[0:6:2])
