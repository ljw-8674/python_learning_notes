L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 访问
assert L[0][0] == 'Apple'
assert L[1][1] == 'Python'
assert L[-1][-1] == 'Bob'

# 添加
L.append(['man','woman'])
assert L == [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Bob'], ['man', 'woman']]
L.insert(0, None)
assert L == [None, ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Bob'], ['man', 'woman']]

# 删除
L.remove(None)
assert L == [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Bob'], ['man', 'woman']]
L.pop()
assert L ==[['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Bob']]

# 切片
assert L[:1] == [['Apple', 'Google', 'Microsoft']]
assert L[::-1] == [['Adam', 'Bart', 'Bob'], ['Java', 'Python', 'Ruby', 'PHP'], ['Apple', 'Google', 'Microsoft']]

# 排序
L.sort(reverse=True)
assert L == [['Java', 'Python', 'Ruby', 'PHP'], ['Apple', 'Google', 'Microsoft'], ['Adam', 'Bart', 'Bob']]


tp1 = (1, 2, 3, 4, 5)
assert tp1[2] == 3
assert tp1[-2] == 4

tp2 = ()
tp2 = tp2 + (10,) + (20, 30)
assert tp2 == (10, 20, 30)

tp3 = (5, 10 , 15, 20, 25)
assert tp3[1:3] == (10, 15)

print('ok')

