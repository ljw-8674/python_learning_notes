## 一、Python基础

### 1. 缩进

Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用4个空格的缩进；在文本编辑器中，需要设置把Tab自动转换为4个空格，确保不混用Tab和空格。

### 2. 数据类型和变量

Python 能直接处理的主要数据类型有：数值型、布尔型、字符串、列表、元组、字典、集合、空值。

变量在程序中就是用变量名表示，变量名必须是大小写英文、数字和下划线的组合，且不能用数字开头。

等号 `=` 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，且可以是不同类型的变量。

```python
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
```

这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言

### 3. 字符串和编码

最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如：大写字母A的编码是65，小写字母z的编码是122。

全世界有上百种语言，各国有各国的标准，就会不可避免地出现冲突，在多语言混合的文本中显示出来会有乱码。 因此，Unicode字符集应运而生，把所有语言都统一到一套编码里。

用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

| 字符 | ASCII    | Unicode           | UTF-8                      |
| ---- | -------- | ----------------- | -------------------------- |
| A    | 01000001 | 00000000 01000001 | 01000001                   |
| 中   |          | 01001110 00101101 | 11100100 10111000 10101101 |

总结一下现在的计算机系统通用的字符编码工作方式：

- 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
- 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。
- 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器。

搞清楚了令人头疼的字符编码问题后，我们再来研究Python的字符串。

在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言。

对于单个字符的编码，Python提供了 `ord()` 函数获取字符的整数表示，`chr()` 函数把编码转换为对应的字符。

```python
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

对于字符串的编码，由于Python的字符串类型在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。要注意区分`'ABC'` 和 `b'ABC'` ，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

以Unicode表示的str通过 `encode()` 方法可以编码为指定的bytes，例如：

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用 `decode()` 方法：

```python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

`len()` 函数计算的是str的字符数，如果换成bytes， `len()` 函数就计算字节数:

```python
>>> len('ABC')
3
>>> len('中文')
2
>>> len(b'ABC')
3
>>> len('中文'.encode('utf-8'))	# len(b'\xe4\xb8\xad\xe6\x96\x87')
6
```

可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。在操作字符串时，我们经常遇到str和bytes的互相转换，为了避免乱码问题，应当始终坚持使用UTF-8编码进行转换。

### 4. 使用list和tuple

列表（list）是一种有序的集合，可以随时添加和删除其中的元素。

可以用索引来访问list中每一个位置的元素，索引是从0开始，其次为1，2，3，...，要确保索引不要越界。也可以从右往左计数，依次为-1，-2，-3，...。

list是一个可变的有序表，所以，可以往list中追加元素（ `append()` 方法）到末尾：

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates.append('Adam')
>>> classmates
['Michael', 'Bob', 'Tracy', 'Adam']
```

把元素插入到指定的位置，用 `insert()` 方法，比如插入到索引号为1的位置：

```python
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

删除list末尾的元素，用 `pop()` 方法（有返回值）

```python
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```

要删除指定位置的元素，用 `pop(i)` 方法，其中 i 是索引位置：

```python
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

```python
>>> classmates[1] = 'Sarah'
>>> classmates
['Michael', 'Sarah', 'Tracy']
```

另一种有序集合叫元组（tuple）。tuple和list非常类似，但是tuple一旦初始化就不能修改。

当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。

```python
>>> t = (1, 2)
>>> t = ()
>>> t = (1,)
```

tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。但这个元素如果可变则可变。

```python
>>> my_tuple = ('a', 'b', ['A', 'B'])
>>> my_tuple[2][0] = 'X'
>>> my_tuple[2][1] = 'Y'
>>> my_tuple
('a', 'b', ['X', 'Y'])
```

### 5. 条件判断

- if语句
- if-else语句
- if-elif-else语句

if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else：

```python
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```

if判断条件还可以简写，比如写：

```python
if x:
    print('True')
```

只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

### 6. 模式匹配

当我们用 `if ... elif ... elif ... else ...` 判断时，会写很长一串代码，可读性较差。 如果要针对某个变量匹配若干种情况，可以使用match语句:

```python
score = input('请输入分数（A/B/C）：')
match score:
    case 'A':
		print('score is A.')
    case 'B':
 		print('score is B.')
 	case 'C':
 		print('score is C.')
 	case _: # “_”表示匹配到其他任何情况
 		print('score is ???.')
```

match语句除了可以匹配简单的单个值外，还可以匹配多个值、匹配一定范围，并且把匹配后的值绑定到变量：

```python
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
```

match语句还可以匹配列表。

```python
args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print(f'gcc compile: {file1}, {', '.join(files)})
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
```

- 第一个 `case ['gcc']` 表示列表仅有 `'gcc'` 一个字符串，没有指定文件名，报错；

- 第二个 `case ['gcc', file1, *files]` 表示列表第一个字符串是 `'gcc'` ，第二个字符串绑定到变量 `file1` ，后面的任意个字符串绑定到 `*files` ，它实际上表示至少指定一个文件；

- 第三个 `case ['clean']` 表示列表仅有 `'clean'` 一个字符串；

- 最后一个 `case _` 表示其他所有情况。

可见，match语句的匹配规则非常灵活，可以写出非常简洁的代码。

### 7. 循环

- Python的循环有两种，一种是for循环，例如计算1~100的整数之和：

```python
sum = 0
for x in range(1, 101):	# 从 1 到 100（不含 101）
    sum = sum + x
print(sum)
```

Python提供一个 `range()` 函数，可以生成一个整数序列。for循环就是把每个元素代入变量 `x` ，然后执行缩进块的语句。

for 循环适用于：已知循环次数或可遍历序列的情况（如列表、字符串、range 等）。

- 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如计算100以内所有奇数之和：

```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```

在循环内部变量 `n` 不断自减，直到变为 `-1` 时，不再满足while条件，循环退出。

while 循环适用于：循环次数不确定、依赖运行时条件结束的情况（如等待输入、处理直到满足条件等）。

在循环中， `break` 语句可以提前退出循环，适用于找到目标、用户输入退出等场景。 `continue` 语句则可以跳过当前的这次循环，直接开始下一次循环，适用于跳过某些不符合条件的元素。这两个语句通常都配合if语句使用。

### 8. 使用dict和set

用Python写一个字典（dict）如下：

```python
>>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>> d['Michael']
95
```

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

```python
>>> d['Adam'] = 67
>>> d['Adam']
67
```

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉。

如果key不存在，dict就会报错。要避免key不存在的错误，有两种办法，一是通过 `in` 判断key是否存在：

```python
>>> 'Thomas' in d
False
```

二是通过dict提供的 `get()` 方法，如果key不存在，可以返回 `None` ，或者自己指定的value：

```python
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1
```

注意：返回 `None` 的时候Python的交互环境不显示结果。

要删除一个key，用 `pop(key)` 方法，对应的value也会从dict中删除：

```python
>>> d.pop('Bob')
75
>>> d
{'Michael': 95, 'Tracy': 85}
```

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict 的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为 key。而list是可变的，就不能作为key。

```python
>>> key = [1, 2, 3]
>>> d[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

集合（set）和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以set中的元素不可重复。

要创建一个set，用 `{x,y,z,...}` 列出每个元素：

```python
>>> s = {1, 2, 3}
>>> s
{1, 2, 3}
```

或者提供一个list作为输入集合：

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

set是无序的，重复元素在set中自动被过滤。

通过 `add(key)` 方法可以添加元素到set中，可以重复添加，但不会有效果：

```python
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
```

通过 `remove(key)` 方法可以删除元素：

```python
>>> s.remove(4)
>>> s
{1, 2, 3}
```

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

```python
>>> s1 = {1, 2, 3}
>>> s2 = {2, 3, 4}
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```

对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

```python
>>> a = ['c', 'b', 'a']
>>> a.sort()
>>> a
['a', 'b', 'c']
```

对于不可变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。但是，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

```python
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc
```

## 二、函数

### 1. 调用函数

要调用一个函数，需要知道函数的名称和参数。

调用函数的时候，如果传入的参数数量不对，会报 `TypeError` 的错误，并且Python会明确地告诉你： `abs()` 有且仅有1个参数，但给出了两个：

```python
>>> abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
```

如果传入的参数数量是对的，但参数类型错了，也会报 `TypeError` 的错误，并且给出错误信息：

```python
>>> abs('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
```

### 2. 定义函数

定义函数时，需要确定函数名和参数个数，如下例：

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))
```

函数体内部的语句在执行时，一旦执行到 `return` 时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有 `return` 语句，函数执行完毕后也会返回结果，只是结果为 `None` 。 `return None` 可以简写为 `return` 。

如果有必要，可以先对参数的数据类型做检查；为什么要做参数检查？

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出 `TypeError` ：

```python
>>> my_abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_abs() takes 1 positional argument but 2 were given
```

但是，如果参数类型不对，Python解释器就无法帮我们检查：

```python
>>> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_abs
TypeError: unorderable types: str() >= int()
>>> abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
```

当传入了不恰当的参数时，内置函数 `abs` 会检查出参数错误，而我们定义的 `my_abs` 没有参数检查，会导致               `if` 语句出错，出错信息和 `abs` 不一样。所以，我们定义的这个函数还不够完善。

现在来修改一下 `my_abs` 的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数 `isinstance()` 实现：

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：

```python
>>> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in my_abs
TypeError: bad operand type
```

此外，函数还可以返回多个值，返回值是一个tuple。

```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
r = move(100, 100, 60, math.pi / 6)
print(r)	# (151.96152422706632, 70.0)
```

### 3. 函数的参数

- 位置参数。最常见的参数，按顺序传递。
- 默认参数。在定义函数时给参数设置默认值，调用时可省略。默认参数放在必选参数后面。默认参数必须指向不可变对象！
- 可变位置参数。用*收集任意个位置参数，传入函数时会打包成tuple。 
- 可变关键字参数。用**收集任意个关键字参数，传入函数时会打包成dict。

### 4. 递归函数

在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。例如：

```python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```

如果我们计算`fact(5)`，根据函数定义可以看到计算过程如下：

```
=> fact(5)
=> 5 * fact(4)
=> 5 * (4 * fact(3))
=> 5 * (4 * (3 * fact(2)))
=> 5 * (4 * (3 * (2 * fact(1))))
=> 5 * (4 * (3 * (2 * 1)))
=> 5 * (4 * (3 * 2))
=> 5 * (4 * 6)
=> 5 * 24
=> 120
```

递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

## 三、高级特性

在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

### 1. 切片

在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。基本语法是：

```python
sequence[start:stop:step]
```

参数说明：

- `start`：切片的起始索引（包含），默认是0。
- `stop`：切片的结束索引（不包含），默认是序列的长度。
- `step`：切片的步长（默认为1。

其特点为：

- 不会修改原序列，而是返回一个新的序列。
- 支持负索引。
- 灵活性很高，常用于反转、跳步取值、截取子串。

### 2. 迭代

通过for循环来依次访问可迭代对象里的元素，直到结束，这种遍历我们称为迭代。例如：

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...     print(key)
...
a
c
b
```

因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

默认情况下，dict迭代的是key。如果要迭代value，可以用 `for value in d.values()` ，如果要同时迭代key和value，可以用 `for k, v in d.items()` 。

如何判断一个对象是可迭代对象呢？

方法是通过 `collections.abc` 模块的 `Iterable` 类型判断：

```python
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

如果要对list实现类似Java那样的下标循环怎么办？

Python内置的 `enumerate` 函数可以把一个list变成”索引-元素“对，这样就可以在for循环中同时迭代索引和元素本身：

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
```

为什么要迭代？

- 代码简洁：不用手动处理下标。
- 节省内存：像生成器那样惰性迭代。
- 统一接口：不同类型（list、tuple、set）都可以用同样的for遍历。

### 3. 列表推导式

作用：用一行语句快速创建列表。

语法：

```python
[expression for item in iterable if condition]
```

- `expression`：生成元素的表达式
- `item`：可迭代对象中的元素
- `condition`：筛选条件（可选）

for循环其实可以同时使用两个甚至多个变量，比如dict的 `items()` 可以同时迭代key和value：

```python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '->', v)
...
y -> B
x -> A
z -> C
```

因此，列表生成式也可以使用两个变量来生成list：

```python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '->' + v for k, v in d.items()]
['y->B', 'x->A', 'z->C']
```

把一个list中所有的字符串变成小写：

```python
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
```

for后面的if不能加上else，因为这里的if是一个筛选条件。

for前面的if必须加上else，因为这里是一个表达式，它必须根据x计算出一个结果。

```python
>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
```

### 4. 生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

在Python中，一边循环一边计算，惰性生成的这种机制，称为生成器（generator）。

创建一个generator，第一种方法是使用生成器表达式。只要把一个列表推导式的 `[]` 改成 ` ()` ，就创建了一个generator。

```python
>>> L = [x * x for x in range(5)]
>>> L
[0, 1, 4, 9, 16]
>>> g = (x * x for x in range(5))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

`L` 是一个list，而 `g` 是一个generator。我们可以直接打印出 `L` 的每一个元素，但对于 `g` 需要通过 `next()` 函数获得generator的下一个返回值。

```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

generator保存的是算法，每次调用 `next(g)` ，就计算出 `g` 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 `StopIteration` 的错误。

当然，也可以使用 `for` 循环去获取generator的值。

```python
>>> g = (x * x for x in range(5))
>>> for n in g:
...     print(n)
... 
0
1
4
9
16
```

如果推算的算法比较复杂，比如斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
```

运行结果如下：

```python
>>> fib(5)
1
1
2
3
5
'done'	# 仅在交互式环境下才打印
```

上面的函数和generator仅一步之遥。要把 `fib` 函数变成generator函数，只需要把 `print(b)` 改为 `yield b` 就可以了：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b	# 多变量同时赋值, 新a=旧b & 新b=旧a+旧b 
        n = n + 1
    return 'done'
```

这就是定义generator的另一种方法。如果一个函数定义中包含 `yield` 关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator。

```python
>>> f = fib(5)
>>> f
<generator object fib at 0x104feaaa0>
```

普通函数用 `return` 返回值后就结束了，而生成器函数在 `yield` 时会“暂停”，下次再调用时继续从上一次暂停的位置执行。

调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。

```python
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

print(next(odd()))	
print(next(odd()))	
print(next(odd()))	
```

回到 `fib` 的例子，我们在循环过程中不断调用 `yield` ，就会不断中断。当然，要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。使用 `for` 循环来迭代，以便获取值。

```python
>>> for n in fib(5):
...     print(n)
...
1
1
2
3
5
```

可以发现，用 `for` 循环调用generator时，拿不到generator的 `return` 语句的返回值。如果想要拿到返回值，必须捕获 `StopIteration` 错误，返回值包含在 `StopIteration `的 `value` 中：

```python
>>> g = fib(5)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
Generator return value: done
```

### 5. 迭代器

首先，可以直接作用于for循环的对象统称为可迭代对象（Iterable）。 可以使用 `isinstance()` 判断一个对象是否是可迭代对象：

```python
>>> from collections.abc import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

其次，可以被 `next()` 函数调用并不断返回下一个值的对象称为迭代器（Iterator）。

```python
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

list、dict、str虽然是Iterable，却不是Iterator。 可以使用 `iter()` 函数把list、dict、str等变成Iterator：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter({}), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被 `next()` 函数调用并不断返回下一个数据，直到没有数据时抛出 `StopIteration` 错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过 `next()` 函数实现按需计算下一个数据，所以 `Iterator` 的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

## 四、函数式编程

### 1. 高阶函数

变量可以指向函数，函数名本身也是变量。

```python
>>> f = abs
>>> f(-10)
10
>>> abs = 10
>>> abs(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

```python
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))	# 11
```

Python内建了`map()`和`reduce()`函数。

- map函数

`map(func, iterable)`

对序列中的每个元素应用函数，返回Iterator。如下例：

```python
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

由于 `map()` 的结果是一个Iterator，是惰性序列，因此要通过 `list()` 函数让它把整个序列都计算出来并返回一个list。

- reduce函数

`reduce(func, iterable[, initializer])`

把序列“累积”成一个结果。如下例，写了一个自己的将str转换为int的函数（替代内置函数 `int()` ）：

```python
from functools import reduce

# char -> int
def char2int(x):
	return ord(x) - ord('0')
# str -> int
def str2int(s):
	return reduce(lambda x, y: x  * 10 + y, map(char2int, s))

print(type(str2int('12345')))	# <class 'int'>
print(str2int('12345') == 12345)	# True
```

- filter函数

`filter(func, iterable)`

用函数过滤序列，保留返回值为True的元素。

```python
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]
```

埃氏筛法计算素数：

```python
def get_prime(n): 
    nums = list(range(2, n + 1)) 
    prime = [] 
    while nums: 
        p = nums[0] p
        rime.append(p) 
        nums = list(filter(lambda x, p=p: x % p > 0, nums[1:])) 
    return prime 

print(get_prime(100))
```

- sorted函数

`sorted(iterable, key=func, reverse=False)`

通过 `key` 函数自定义排序规则。

```python
print(sorted(["apple", "watermelon", "cherry"], key=len))  
# ['apple', 'cherry', 'watermelon']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  
# ['Zoo', 'Credit', 'bob', 'about']
```

### 2. 返回函数

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

- 核心机制：依赖于闭包（Closure）

闭包就是内层函数引用了外层函数的局部变量。使用闭包时，如果要在内层函数里面对外层变量赋值，需要先使用nonlocal声明该变量不是当前函数的局部变量。

- 应用场景：函数工厂、延迟执行、装饰器等。

函数工厂：

```python
def power(exp):
    def inner(x):
        return x ** exp
    return inner

square = power(2)  # 返回一个平方函数
cube = power(3)    # 返回一个立方函数

print(square(5))  # 25
print(cube(2))    # 8
```

延迟计算：

```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
print(add5(10))  # 15
```

用于装饰器：

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def hello():
    print("Hello")

hello()
```

### 3. 装饰器

装饰器（decorator）是一个“包装”函数的函数，用来在不修改原函数代码的前提下，为函数添加额外功能，相当于是给函数套了一层外壳。

首先，decorator的本质是一个函数：

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # 执行前
        result = func(*args, **kwargs)
        # 执行后
        return result
    return wrapper
```

`decorator(func)` 返回的 `wrapper` 会替代 `func`。

返回的 `wrapper()` 函数名字就是 `'wrapper'` ，所以，需要把原始函数的 `__name__` 等属性复制到 `wrapper()` 函数中，否则，有些依赖函数签名的代码执行就会出错。使用内置装饰器 `@functools.wraps` 即可完成：

```python
import functools

def greet(fn):
    @functools.wraps(fn)   # 保留原函数名字
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print('nihao~~')
        return result
    return wrapper
```

其次，装饰器要能接收任意参数。使用 `*args` 和 `kwargs` 的参数，这样装饰器可用于任何函数。

另外，装饰器本身要接收参数时，需要多套一层函数。

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hi")
```

ps：语法糖（Syntactic Sugar）是编程语言里提供的一种写法，它不会增加新功能，只是让代码更简洁、更易读。

- 装饰器语法糖

```python
@log
def hello():
    print("Hello")
```

等价于：

```python
def hello():
    print("Hello")
hello = log(hello)
```

`@log` 就是语法糖，让代码更漂亮。

- 列表推导式

`squares = [x*x for x in range(5)]` 等价于：

```python
squares = []
for x in range(5):
    squares.append(x*x)
```

列表推导式就是for循环的语法糖。

- `with` 上下文管理

```python
with open("data.txt") as f:
    content = f.read()
```

等价于：

```python
f = open("data.txt")
try:
    content = f.read()
finally:
    f.close()
```

`with` 就是try/finally的语法糖。

## 五、面向对象编程

面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

### 1. 类和实例

面向对象最重要的概念就是类（Class）和实例（Instance），注意如下特点：

- 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

- 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

- 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

- 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```python
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```

### 2. 访问限制

值得一提的是，面向对象编程的一个重要特点就是数据封装。如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线 __ ，在Python中，实例的变量名如果以 __ 开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。

```python
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问 `实例变量.属性名` 了。 

```python
>>> bart = Student('Bart Simpson', 59)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
```

这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

那么问题来了，如果外部代码要获取甚至修改 `name` 怎么办？此时，可以给Student类增加 `get_name` 和 `set_score` 这样的方法。

```python
def get_name(self):
    return self.__name
def set_name(self,name):
    self.__name = name
```

有意义的一点是，在方法中，可以对参数做检查，避免传入无效的参数：

```python
class Student(object):
    ...

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
```

### 3. 继承和多态

在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

继承最大的好处是子类获得了父类的全部功能，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

当子类和父类都存在相同的方法时，我们说，子类的方法覆盖了父类的方法，在代码运行的时候，总是会调用子类的方法。这样，我们就获得了继承的另一个好处：多态。

对于一个变量，我们只需要知道它的父类，无需确切地知道它的子类，就可以放心地调用父类中方法，而具体调用的方法是作用在父类是子类对象上，由运行时该对象的确切类型决定。这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种子类时，只要确保其方法编写正确，不用管原来的代码是如何调用的。

### 4. 获取对象信息

- 使用 `Type()` 函数

基本类型都可以用 `type()` 判断，如果一个变量指向函数或者类，也可以判断。

```python
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>
```

- 使用 `isinstance()` 函数

`isinstance()` 判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

```python
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(h, Husky)
True
>>> isinstance(h, Dog)
True
>>> isinstance(h, Animal)
True
>>> isinstance(d, Husky)
False
```

能用 `type()` 判断的基本类型也可以用 `isinstance()` 判断。

```python
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
```

并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple。

```python
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

- 使用 `dir()` 函数

使用 `dir()` 函数，可以获得一个对象的所有属性和方法，它返回一个包含字符串的list。

```python
>>> dir('ABC')
['__add__', '__class__',..., '__subclasshook__', 'capitalize','casefold',..., 'zfill']
```

类似 `__xxx__` 的属性和方法在Python中都是有特殊用途的，比如 `__len__` 方法返回长度。在Python中，如果你调用 `len()` 函数试图获取一个对象的长度，实际上，在 `len()` 函数内部， 它自动去调用该对象的 `__len__()` 方法，所以，下面的代码是等价的：

```python
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

### 5. 实例属性和类属性

由于Python是动态语言，由类创建的示例可以任意绑定属性。

给实例绑定属性的方法，一是在内部通过self声明属性 `self.xxx = ...` ，二是在外部通过实例临时地绑定 `instance.xxx = ...` 。

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

```python
class Student(object):
    name = 'Student'
```

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。值得一提的是，实例属性的优先级要比类属性的高，如下：

```python
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```

实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

## 六、面向对象高级编程

数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。

### 1. 使用 `__slots__`

`__slots__` 是 Python 中类的一个高级特性，用于限制实例能绑定的属性，并且提供内存优化和性能提升的能力。

- 限制实例只能绑定指定属性

```python
class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = 'Tom'   # OK
p.age = 20       # OK
p.address = 'Beijing'  # ❌ AttributeError：不能添加新属性
```

使用 `__slots__` 后，实例不能随意增加属性，可以避免误操作。

- 节省内存

默认情况下，每个实例都有一个字典 `__dict__` ，属性名作为key，属性值为value，这个dict会占用比较大内存。 但使用 `__slots__` 后，将不会创建 `__dict__` ，属性存储在固定的结构里，在使用大量实例时可以显著减少内存，节省比例常能达到40%~60%。

值得一提的是，父类使用 `__slots__` 时，子类不会继承，必须重新声明。

### 2. 使用 `@property`

在给实例绑定属性的时候，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随意修改。

```python
s = Student()
s.score = 9999999
```

属性可以任意赋值，这显然不合逻辑。为了限制score的范围，可以通过一个 `set_score()` 方法来设置成绩，再通过一个 `get_score()` 来获取成绩，这样，在 `set_score()` 方法里，就可以进行参数检查：

```python
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

这是典型的Java式写法，但是，上面的调用方法还是略显复杂，没有直接用属性这么直接简单。

Python的 `@property` 把一个方法伪装成属性访问，并可加上验证逻辑，是最优雅的封装方式。

```python
class A:
    @property
    def x(self):
        return self._x   # getter

    @x.setter
    def x(self, value):
        self._x = value  # setter
```

注意：属性方法名和实例变量重名，会造成递归调用，导致栈溢出报错！

`x` 是公开属性名（让别人访问）
`_x` 是内部真正存储数据的变量（防止递归、保持封装）

值得一提的是，还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python
class Student:
    @property
    def age(self):
        return 18
```

调用如下：

```python
s = Student()
print(s.age)     # 20
s.age = 30       # ❌ 不能设置
```

### 3. Mixin

首先，Mixin（混入类）是一种“只提供功能，不单独使用”的类。

其特点是：

- 不用于单独实例化
- 只提供一些功能（方法）
- 通过多重继承组合到主类里
- 类名通常以 `Mixin` 结尾

例如：

```python
class JsonMixin:
    def to_json(self):
        ...
```

主类只需继承它：

```python
class User(JsonMixin):
    pass
```

Mixin的规则是：

- 小而专一（单一功能）
- 不依赖外部状态
- 不要有自己的 `__init__`
- 类名以 `XXXMixin` 结尾

Mixin是Python中最佳的可组合代码复用方案，常用于日志、序列化、权限、缓存等功能，通过多重继承让类“想要什么功能就混什么功能”。

### 4. 定制类

通过实现特殊方法（以 `__xxx__` 命名的“魔术方法”）来自定义类的行为，让你的对象像内置类型一样使用。

- `__str__` 和 `__repr__`

不做处理时，我们直接打印一个实例obj，会打印出形如 `<__main__.Student object at 0x109afb190>` 的信息。怎么才能打印得好看呢？

首先， `__str__` 方法，作用是定义“对象的非正式字符串表示”，主要用于用户友好的输出，其触发时机为 `print(obj)` 和 `str(obj)` 。

 ```python
 class Student(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return f'Student({self.name})'
 
 s = Student('JJLin')    
 print(s) # Student(JJLin)
 print(str(s)) # Student(JJLin)
 ```

其次， `__repr__` 方法，作用是定义“对象的官方字符串表示”，主要用于调试和开发 ，其触发时机为：

1. 在交互式解释器里直接输入实例对象名；
2. 调用 `repr(obj)` 时；
3. 没有实现 `__str__` 时，直接或间接使用`str(obj)` 会回退到 `__repr__`。

- `__iter__` 和 `__next__`

如果一个类想被用于for循环，类似list或tuple那样，就必须实现一个 `__iter__()` 方法，该方法返回一个可迭代对象，然后，Python的for循环就会不断调用该迭代对象的 `__next__()` 方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

以斐波那契数列为例，写一个Fib类如下：

```python
class MyFib(object):
    def __init__(self):
        self.a = 0
        self.b = 1 

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
```

- `__getitem__`

Fib实例对象虽然能作用于for循环，但并不能按照下标取出元素。要表现得像list那样按照下标取出元素，需要实现 `__getitem__()` 方法：

```python
class MyFib(object):
    def __init__(self):
        self.a = 0
        self.b = 1 

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
	
    def __getitem__(self, n):
        for _ in range(n):
            self.a, self.b = self.b, self.a + self.b
        return self.a
```

若要实现切片，则需做以下判断：

```python
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
```

此外，如果把对象看成 `dict` ， `__getitem__()` 的参数也可能是一个可以作key的object，例如`str`。与之对应的是 `__setitem__()` 方法，把对象视作list或dict来对集合赋值。最后，还有一个 `__delitem__()` 方法，用于删除某个元素。

总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

- `__getattr__`

`__getattr__` 是 Python 对象模型里一个非常重要的“动态属性访问钩子”，它允许你在访问一个不存在的属性时，自定义行为。

当访问 `obj.xxx`，而 `xxx` 这个属性不存在时，Python会自动调用 `obj.__getattr__` 。

当然，如果属性存在，则不会调用 `__getattr__`。

```python
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

s = Student()
print(s.name)	# Michael
print(s.score)	# 99
```

此外，任意调用如 `s.abc` 都会返回 `None` ，这是因为我们定义的 `__getattr__` 默认返回就是 `None` 。要让class只响应特定的几个属性，我们就要按照约定，抛出 `AttributeError` 的错误：

```python
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError(f"\'Student\' object has no attribute \'{attr}\'")
```

- `__call__`

定义一个 `__call__()` 方法，就可以直接对实例进行调用。

```python
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is {self.name}.')
        
s = Student('Michael')
s() # My name is Michael.
```

还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

怎判断一个对象是否能被调用，能被调用的对象就是一个 `Callable` 对象。

```python
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
```

### 5. 使用枚举类

定义枚举类如下，这样我们就获得了一个枚举类Month，可以直接使用 `Month.Jan` 来引用一个常量，或者枚举它的所有成员：

```python
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
```

其中， `Enum` 的第一个参数是枚举的类名，第二个参数是一个包含枚举成员名称的元组。`value` 属性是自动赋给成员的int常量，默认从1开始计数。输出结果是：

```python
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
```

如果需要更精确地控制枚举类型，可以从 `Enum` 派生出自定义类：

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

其中，`@unique` 装饰器可以帮助我们检查保证没有重复值。

## 七、错误、调试和测试

### 1. 错误处理

Python内置的 `try...except...` 用来捕获异常十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。 

- `else`：当 `try` 语句块里没有异常时执行

- `finally`：无论是否出错都会执行（常用于清理资源）

```python
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
```

程序也可以主动抛出异常，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因：

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b 不能为 0")
    return a / b

print(divide(10, 2))
print(divide(10, 0))  # 会触发 ValueError
```

换一种说法，捕获异常是“接住错误”，作用是防止程序崩溃，处理错误；抛出异常是“制造或传递错误”，作用是主动报告错误。

自定义异常类，继承内置 `Exception`，可以定义自己的业务逻辑错误类型：

```python
class MyError(Exception):
    pass

try:
    raise MyError("自定义错误")
except MyError as e:
    print("捕获到自定义异常：", e)
```

### 2. 调试

- print() 打印变量值
- assert 断言

如果断言成功，无事发生；而如果断言失败， `assert` 语句本身就会抛出 `AssertionError` ：

```python
D:\PythonProject\general>python tmp_code.py
Traceback (most recent call last):
  ...
AssertionError: n is zero!
```

- logging

把 `print()` 替换为 `logging` 是第3种方式，和 `assert` 比，`logging` 不会抛出错误，而且可以输出到文件：

```python
import logging

logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info(f'n = {n}')
print(10 / n)
```

运行后输出了：

```python
D:\PythonProject\general>python tmp_code.py
INFO:root:n = 0
Traceback (most recent call last):
  File "D:\PythonProject\general\tmp_code.py", line 8, in <module>
    print(10 / n)
          ~~~^~~
ZeroDivisionError: division by zero
```

`logging` 允许你指定记录信息的级别，有 `debug` ， `info` ， `warning` ， `error` 等几个级别，当我们指定 `level=INFO` 时， `logging.debug` 就不起作用了。同理，指定 `level=WARNING` 后， `debug` 和 `info` 就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。 

- IDE

如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。 

PyCharm：http://www.jetbrains.com/pycharm/ 

另外，Eclipse加上pydev插件也可以调试Python程序。

【小结】

写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

### 3. 单元测试

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。 

比如对函数 abs() ，我们可以编写出以下几个测试用例： 

1. 输入正数，比如 `1` 、 `1.2` 、 `0.99` ，期待返回值与输入相同； 
2. 输入负数，比如 `-1` 、 `-1.2` 、 `-0.99` ，期待返回值与输入相反；
3. 输入 `0` ，期待返回 `0` ；
4. 输入非数值类型，比如 `None` 、 `[]` 、 `{}` ，期待抛出 `TypeError` 。 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

先来写个待测试类， `my_dict.py` :

```python
class MyDict(dict):
    """支持点访问的字典"""
    
    def __init___(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Dict' object has no attribute '{key}'")

    def __setattr__(self,key,value):
        self[key] = value
```

然后写测试类， `my_dict_test.py` :

```python
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
```

一旦编写测试类，我们就可以运行单元测试。最简单的运行方式是在 `my_dict_test.py` 的最后加上两行代码，这样就可以把它当做正常的python脚本运行：：

```python
if __name__ == '__main__':
    unittest.main()
```

另一种方法是在命令行通过参数 `-m unittest` 直接运行单元测试，这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试：

```python
D:\PythonProject\general>python -m unittest my_dict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```

在开发阶段，很多时候，我们希望反复执行某一个测试方法，例如 `test_attr()` ，而不是每次都运行所有的测试方法，可以通过指定 `module.class.method` 来运行单个测试方法：

```python
D:\PythonProject\general>python -m unittest my_dict_test.TestDict.test_attr
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

其中， `module` 是文件名 `my_dict_test` （不含 .py ）， `class` 是测试类 `TestDict` ， `method` 是指定的测试方法名 `test_attr` 。

也可以在单元测试中编写两个特殊的 `setUp()` 和 `tearDown()` 方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

`setUp()` 和 `tearDown()` 方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以 在 `setUp()` 方法中连接数据库，在 `tearDown()` 方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

```python
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
```

【小结】

- 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。 
- 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
- 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
- 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

### 4. 文档测试

当我们编写注释时，如果写上这样的注释，无疑明确地告诉函数的调用者该函数的期望输入和输出：

```python
def abs(n):
 '''
 Function to get absolute value of number.

 >>> abs(1)
 1
 >>> abs(-1)
 1
 >>> abs(0)
 0
 '''
 return n if n >= 0 else (-n)
```

Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。doctest可以严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。

当模块正常导入时，doctest不会被执行。在命令行直接运行时：

```bash
python -m doctest -v xxx.py
```

在代码中运行时：

```python
if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)
```

运行结果为什么输出也没有，这说明我们编写的doctest运行都是正确的。

【小结】

doctest不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。

## 八、IO编程

### 1. 文件读写

首先是读文件，可以使用Python内置的 `open()` 函数，传入文件路径和标示符：

```python
>>> f = open('/Users/michael/test.txt', 'r')
```

其中，标示符 `'r'` 表示只读，这样就成功地打开了一个文件。

若文件不存在， `open()` 函数就会抛出一个 `IOError` 的错误：

```python
>>> f = open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory:'/Users/michael/notfound.txt'
```

如果文件打开成功，接下来我们可以调用 `read()` 方法，一次读取文件的全部内容，Python把内容读到内存，用一个 `str` 对象表示：

```python
>>> f.read()
'Hello, world!'
```

最后一步是调用 `close()` 方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的： 

```python
>>> f.close()
```

由于文件读写时都有可能产生 `IOError` ，一旦出错，后面的 `f.close()` 就不会调用。所以，为了保证每次都能关闭文件，我们可以使用 `with` 语句来自动帮我们调用 `close()` 方法：

```python
with open('/path/to/file', 'r') as f: 
    print(f.read())
```

值得一提的是，读取方式也有多种，可以根据需要决定怎么调用：

- 调用 `read()` 会一次性读取文件的全部内容
- 调用 `read(size)` 方法，每次最多读取size个字节的内容
- 调用 `readline()` 每次读取一行内容
- 调用 `readlines()` 一次读取所有内容并按行返回1个列表

如果文件很小， `read()` 一次性读取最方便；如果不能确定文件大小，反复调用 `read(size)` 比较保险；如果是配置文件，调用 `readlines()` 最方便。

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件 ，比如图片、视频等等，用 `'rb'` 模式打开文件即可：

```python
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

注意：每次调用 `f.read(size)` 都会从上次读取的位置继续往后读。操作文件指针位置的方法有：

- `f.tell()`：返回当前读取位置。

- `f.seek(offset)`：移动文件指针。

再来说说写文件，其与读文件是一样的，唯一区别是调用 `open()` 函数时，传入标示符 `'w'` 或者 `'wb'` 表示写文本文件或写二进制文件：

```python
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

你可以反复调用 `write()` 来写入文件，但是务必要调用 `f.close()` 来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用 `close()` 方法时，操作系统才保证把没有写入的数据全部写入磁盘，忘记调用 `close()` 的后果是数据可能只写了一部分到磁盘，剩下的丢失了。当然，使用with语句就没有这个顾虑了。

需要说明的是，以 `'w'` 模式写入文件时，如果文件已存在，会直接覆盖。如果我们希望追加到文件末尾，可以传入 `'a'` 以追加模式写入。

### 2. 操作文件和目录

操作文件和目录的函数一部分放在 `os` 模块中，一部分放在 `os.path` 模块中。查看、创建和删除目录如下：

```python
>>> import os

# 1.查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'

# 2.把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'

# 3.然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')

# 4.删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
```

注意，把两个路径合成一个时，不要直接拼字符串，而要通过 `os.path.join()` 函数，这样可以正确处理不同操作系统的路径分隔符。

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过 `os.path.split()` 函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

```python
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
```

`os.path.splitext()` 可以直接让你得到文件扩展名，返回一个元组，这在很多时候非常方便：

```python
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
```

注意，这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

利用Python的特性来过滤文件。比如我们要列出当前目录下的所有py文件，只需要一行代码：

```python
>>> [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
['xxx.py', ...]
```

### 3. 序列化

把内存中的对象转换成一种可存储或可传输的格式（如字节流、字符串、JSON 等）的过程，称之为序列化。

序列化主要解决三个问题：

1. 数据持久化，把对象保存到文件或数据库中；
2. 网络传输，在进程间、服务器之间传递对象；
3. 跨语言/跨平台交互，例如 JSON、Protocol Buffers。

Python中常见的序列化方式：

第一，`pickle` —— Python原生序列化。 

- 将Python对象序列化为二进制字节串

- 只能用于Python ↔ Python

- 不安全（不要反序列化不可信数据）

```python
import pickle

data = {"name": "Alice", "age": 20}

# 序列化（写入文件）
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# 反序列化（读取文件）
with open("data.pkl", "rb") as f:
    new_data = pickle.load(f)

print(new_data)
```

第二，`json` —— 最常用的通用序列化方式。

- 序列化为JSON 字符串

- 可跨语言

- 仅支持基本数据类型（dict, list, str, int, float, bool, None）

```python
import json

data = {"name": "Alice", "age": 20}

# 序列化为字符串
json_str = json.dumps(data)

# 反序列化为字典
new_data = json.loads(json_str)

# 文件操作
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

从上面的例子可以看出：

- `.dump()` 用于将对象序列化并直接写入文件对象；
- `.dumps()` 用于将对象序列化为字符串（或字节）并返回。

值得一提的是，对中文进行JSON序列化时， `json.dumps()` 提供了一个 `ensure_ascii` 参数，默认为True。因此，所有非ASCII字符（例如中文、表情符号等）都会被转义成 `\uXXXX` 的形式。如果你想让JSON中显示真正的中文，而不是Unicode转义，就可以设置：

```python
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
```

第三，自定义对象的 JSON 序列化。

Python的 `dict` 对象可以直接序列化为JSON的`{}`，不过，很多时候，我们更喜欢用 `class` 表示对象，比如定义`Student`类，然后序列化。但是，对象不是一个可序列化为JSON的对象，需要我们去做处理。

方法一：转成字典

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

u = User("Alice", 20)
json_str = json.dumps(u.__dict__)
```

方法二：自定义编码器

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def user2dict(u):
    return {
        'name': std.name,
        'age': std.age,
    }
   
u = User("Alice", 20)
json.dumps(u, default=user2dict)
```

【小结】

Python语言特定的序列化模块是 `pickle` ，但如果要把序列化搞得更通用、更符合Web标准， 就可以使用 `json` 模块。`json` 模块的 `dumps()` 和 `loads()` 函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。

## 九、正则表达式

### 1. 作用

正则表达式是一种强大的文本模式匹配工具，常用于：

- 字符串匹配
- 查找 / 提取文本
- 替换文本
- 校验格式（邮箱、手机号、身份证等）

Python 中正则主要通过 `re` 模块来使用。

### 2. 语法

| 符号    | 含义               |
| ------- | ------------------ |
| `.`     | 任意字符（除换行） |
| `\d`    | 数字               |
| `\D`    | 非数字             |
| `\w`    | 字母/数字/下划线   |
| `\W`    | 非 `\w`            |
| `\s`    | 空白字符           |
| `\S`    | 非空白             |
| `*`     | 0 次或多次         |
| `+`     | 1 次或多次         |
| `?`     | 0 或 1 次          |
| `{n}`   | 恰好 n 次          |
| `{n,m}` | n 到 m 次          |
| `^`     | 字符串开头         |
| `$`     | 字符串结尾         |

### 3. 常用函数

1. `re.search()` —— 查找是否存在

在字符串中查找第一个匹配的内容，找到返回Match对象，否则返回 `None`。

```python
import re

text = "My phone number is 13812345678 and 13800000001"

result = re.search(r"\d{11}", text)
if result:
    print(result.group())    # 13812345678
```

2. `re.findall()` —— 找出所有匹配

找出字符串中所有符合正则表达式的内容，并以列表形式返回

```python
import re

text = "原价998元，圣诞节折扣888元，元旦节折扣778元"

numbers = re.findall(r"\d+", text)
print(numbers)  # ['998', '888', '778']
```

3. `re.match()` —— 从字符串开头匹配

只能从字符串开头开始匹配。

```python
import re

a = re.match(r"\d+", "123abc")
b = re.match(r"\d+", "abc123")

print(a)    # <re.Match object; span=(0, 3), match='123'>
print(b)    # None
```

4. `re.sub()` —— 替换

用于字符串替换。

```python
import re

text = "手机号：13812345678"
new_text = re.sub(r"\d{11}", "***", text)
print(new_text)    # 手机号：***
```

5. `re.split()` —— 正则分割

相比于 `str.split()` 更加灵活。

```python
import re

text = "apple    banana,orange;;;grape"
result = re.split(r"[\s,;]+", text)
print(result)    # ['apple', 'banana', 'orange', 'grape']
```

### 4. 分组

1. 普通分组

```python
import re

text = "生日：1998-08-23"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

print(m.group(0))    # group(0)：整个正则匹配结果
print(m.group(1))    # group(1) 开始才是第1个括号
print(m.group(2))
print(m.group(3))
```

2. 命名分组

```python
import re

text = "生日：1998-08-23"
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)

print(m.group("year"))    # 可通过名称访问,提高可读性
print(m.groupdict())    # {'year': '1998', 'month': '08', 'day': '23'}
```

3. 非捕获分组

捕获分组要存内容，而非捕获分组只做结构匹配，这在复杂或大量匹配中有意义。

```python
import re

print(re.findall(r'ab',  'ababab'))    # group(0)
print(re.findall(r'(a)(b)', 'ababab'))    # group(1)
print(re.findall(r'(?:a)(?:b)', 'ababab'))    # group(0)
```

### 5. 贪婪匹配

需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。如下例：

```python
import re

m = re.match(r'^(\d+)(0*)$', '102300')
print(m.groups())    # ('102300', '')
```

由于 `\d+` 采用贪婪匹配，直接把后面的 `0` 全部匹配了，结果 `0*` 只能匹配空字符串了。

必须让 `\d+` 采用非贪婪匹配（也就是尽可能少匹配），才能把后面的 `0` 匹配出来：

```python
import re

m = re.match(r'^(\d+?)(0*)$', '102300')
print(m.groups())    # ('1023', '00')
```

### 6. 编译

当我们在Python中使用正则表达式时，re模块内部会干两件事情：

1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2. 用编译后的正则表达式去匹配字符串。

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

```python
import re

# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')    

# 使用：
print(re_telephone.match('010-12345').groups())    # ('010', '12345')
print(re_telephone.match('010-8086').groups())    # ('010', '8086')
```

编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

## 十、常用内建模块

### 1. datetime

`datetime` 是Python处理日期和时间的标准库。

- 获取当前日期和时间：

```python
>>> from datetime import datetime
>>> now = datetime.now() # 获取当前datetime
>>> print(now)
2025-10-10 15:55:00.006017
>>> print(type(now))
<class 'datetime.datetime'>
```

其中，`datetime.now()` 返回当前日期和时间，其类型是 `datetime` 。

- 获取指定日期和时间：

```python
>>> from datetime import datetime
>>> dt = datetime(2025, 11, 11, 11, 11) # 用指定日期时间创建datetime
>>> print(dt)
2025-11-11 11:11:00
```

- datetime转换为timestamp：

```python
from datetime import datetime

dt = datetime(2025, 10, 11, 10, 30, 0)
ts = dt.timestamp()
print(ts)
```

Python的timestamp是一个浮点数，整数位表示秒。 而某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数。

- timestamp转换为datetime：

方法 1（转换为本地时间）：`datetime.fromtimestamp(ts)`

方法 2（转换为UTC时间）：`datetime.fromtimestamp(ts, UTC)` 

```python
from datetime import datetime, UTC

ts = 1700000000

# 转本地时间
local_time = datetime.fromtimestamp(ts)
print(local_time)

# 转UTC时间
# utc_time = datetime.utcfromtimestamp(ts) # 此方法已被标记为弃用
utc_time = datetime.fromtimestamp(ts, UTC)
print(utc_time)
```

- str转换为datetime：

很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过 `datetime.strptime()` 实现，需要一个日期和时间的格式化字符串：

```python
>>> from datetime import datetime
>>> cday = datetime.strptime('2025-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
>>> print(cday)
2025-12-12 12:12:12
```

转换后的datetime是没有时区信息的，字符串 `'%Y-%m-%d %H:%M:%S'` 规定了日期和时间部分的格式。

- datetime转换为str：

如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过 `strftime()` 实现的，同样需要一个日期和时间的格式化字符串：

```python
>>> from datetime import datetime
>>> dt = datetime(2025, 10, 10, 10, 10, 10)
>>> print(dt.strftime('%Y-%m-%d %H:%M:%S'))
2025-10-10 10:10:10
```

- datetime加减

 第一种：`datetime` 加减 `timedelta`

```python
from datetime import datetime, timedelta

dt0 = datetime(2026, 1, 1, 0, 0, 0)
dt1 = dt0 + timedelta(days=2, hours=12)
dt2 = dt0 - timedelta(days=3, minutes=15)
print(f'原时间:{dt0}')
print(f'做加法后的时间:{dt1}')
print(f'做减法后的时间:{dt2}')
```

第二种：`datetime` 之间的减法

```python
from datetime import datetime

dt1 = datetime(2025, 10, 11, 14, 30, 0)
dt2 = datetime(2025, 10, 8, 10, 0, 0)
delta = dt1 - dt2
print(delta)
print(delta.days, "天")
print(delta.total_seconds(), "秒")
```

- 时区转换

第一步：给本地时间声名时区

```python
naive_dt = datetime(2026, 1, 1, 0, 0, 0)
dt_sh = dt.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
```

注意： `.replace(tzinfo=...)` 只是标记当前对象属于哪个时区，不改变时间数值。

第二步：转换时区

```python
dt_ny = dt_sh.astimezone(ZoneInfo("America/New_York"))
```

【小结】

`datetime` 表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储 `datetime` ，最佳方法是将其转换为时间戳再存储，因为时间戳的值与时区完全无关。

### 2. collections

`collections` 模块提供了一些有用的集合类，可以根据需要选用。

1. namedtuple

`namedtuple` 是Python中用于创建‌具名元组的工厂函数，它允许通过名称或索引来访问元组元素，从而提升代码可读性。‌

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)  # 1
print(p.y)  # 2
```

用 `namedtuple` 定义的数据类型，既具备tuple的不变性，又可以根据属性来引用，使用十分方便。

2. deque

使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

而 `deque` 是为了高效实现插入和删除操作的双向列表，其除了实现list的 `append() `和 `pop()` 外，还支持 `appendleft()` 和 `popleft()` ，这样就可以非常高效地往头部添加或删除元素。

```python
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)  # deque(['y', 'a', 'b', 'c', 'x'])
```

3. defaultdict

使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用 `defaultdict` ：

```python
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # 'abc'
print(dd['key2']) # 'N/A'
```

注意：默认值是调用函数返回的，而函数在创建 `defaultdict` 对象时传入。 除了在Key不存在时返回默认值， `defaultdict` 的其他行为跟dict是完全一样的。

4. Counter

`Counter` 是一个简单的计数器，实际上也是dict的一个子类，用来统计可哈希对象出现的次数。例如：

```python
from collections import Counter

c = Counter('programming')
print(c)  # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

nums = [1, 2, 2, 3, 3, 3]
c = Counter(nums)

print(c[3])   # 3
print(c[99])  # 0（不存在不会抛出KeyError）
```

### 3. argparse

使用 `argparse` 解析参数，只需定义好参数类型，就可以获得有效的参数输入，能大大简化获取命令行参数的工作。

假设我们想编写一个备份MySQL数据库的命令行程序，需要输入的参数如下：

- host参数：表示MySQL主机名或IP，不输入则默认为 localhost ；
- port参数：表示MySQL的端口号，int类型，不输入则默认为 3306 ；
- user参数：表示登录MySQL的用户名，必须输入；
- password参数：表示登录MySQL的口令，必须输入；
- gz参数：表示是否压缩备份文件，不输入则默认为 False ；
- outfile参数：表示备份文件保存在哪，必须输入。

其中， `outfile` 是位置参数，而其他则是类似 `--user root` 这样的“关键字”参数。 

用 `argparse` 来解析参数，一个完整的示例如下：

```python
import argparse

def main():
    # 定义 ArgumentParser 实例
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL database.',  # 描述
        epilog='Copyright (r), 2025'  # 说明信息
    )

    # 关键字参数
    parser.add_argument('--host', default='localhost', help="主机名或IP地址")
    parser.add_argument('--port', default=3306, type=int, help="端口号")
    parser.add_argument('-u', '--user', required=True, help="用户名")
    parser.add_argument('-p', '--password', required=True, help="密码")
    parser.add_argument('--database', required=True, help="数据库名称")
    parser.add_argument('-gz', '--gzcompress', action='store_true', help='是否压缩备份文件 (.gz 格式)')

    # 位置参数
    parser.add_argument('outfile', help="备份文件保存路径")

    # 解析参数
    args = parser.parse_args()

    # 打印一下命令行里所输入的参数
    print('Parsed arguments:')
    print(f'host        = {args.host}')
    print(f'port        = {args.port}')
    print(f'user        = {args.user}')
    print(f'password    = {args.password}')
    print(f'database    = {args.database}')
    print(f'gzcompress  = {args.gzcompress}')
    print(f'outfile     = {args.outfile}')

    
if __name__ == '__main__':
    main()
```

输入有效的参数，则程序能解析出所需的所有参数：

```
D:\PythonProject\python_learning_notes>python exercise26_Argparse.py --host 127.0.0.1 --port 114514 -u root -p 123456 --database my_db -gz backyp.sql
Parsed arguments:
host        = 127.0.0.1
port        = 114514
user        = root
password    = 123456
database    = my_db
gzcompress  = True
outfile     = backyp.sql
```

缺少必要的参数，或者参数不对，将报告详细的错误信息：

```
D:\PythonProject\python_learning_notes>python exercise26_Argparse.py -u root -p 123456 --database my_db -gz
usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile
backup: error: the following arguments are required: outfile
```

此外，如果输入 `-h` ，则打印帮助信息：

```
D:\PythonProject\python_learning_notes>python exercise26_Argparse.py -h
usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile

Backup MySQL database.

positional arguments:
  outfile               备份文件保存路径

options:
  -h, --help            show this help message and exit
  --host HOST           主机名或IP地址
  --port PORT           端口号
  -u, --user USER       用户名
  -p, --password PASSWORD
                        密码
  --database DATABASE   数据库名称
  -gz, --gzcompress     是否压缩备份文件 (.gz 格式)

Copyright (r), 2025
```

使用 `argparse` 后，解析参数的工作被大大简化了，我们可以专注于定义参数，然后直接获取到有效的参数输入。

### 4. base64

`Base64` 编码用于表示和传输二进制数据。这种编码方式常用于在电子邮件、URL以及其他需要处理文本格式数据的场景中，将图像、音频、视频等文件以文本形式传输。 `Base64` 编码不会改变数据内容，只是改变了数据的表现形式。

`Base64` 编码将每三个字节（24位）转换为四个字符。具体步骤如下：

1. 将每三个字节分为24位。
2. 将这24位数据分成四组，每组6位。
3. 每组6位的二进制数据转为一个对应的字符。`Base64` 编码表有64个字符（包括字母、数字和两个符号），每6位映射到其中一个字符。这个表包括：
   - A-Z（26个大写字母）
   - a-z（26个小写字母）
   - 0-9（10个数字）
   - '+'和'/'（2个符号）
4. 如果原始数据不是3的倍数，最后会添加"="符号来补充填充，以确保输出是4的倍数。

假设，我们需要对字符串 `"Man"` 进行Base64编码：

1. `"Man"` 的ASCII编码为：
   - M: 77
   - a: 97
   - n: 110
   - 合起来：`77 97 110`
2. 转为二进制表示：`01001101 01100001 01101110`。
3. 将24位二进制数据分为4组6位：
   - `010011 010110 000101 101110`
4. 转为Base64字符：
   - 010011 → 19 → T
   - 010110 → 22 → W
   - 000101 → 5 → F
   - 101110 → 46 → u

因此，`"Man"` 编码后的Base64结果是：`TWFu`。

Python内置的 `base64` 可以直接进行base64的编码和解码：

```python
import base64

original_data = "Man! What can I say? Manba out!"

encode_data = base64.b64encode(original_data.encode())
print(encode_data.decode())

decode_data = base64.b64decode(b'TWFuISBXaGF0IGNhbiBJIHNheT8gTWFuYmEgb3V0IQ==')
print(decode_data.decode())
```

### 5. hashlib

`hashlib` 模块提供了常见的哈希算法，如MD5，SHA1等等。

MD5是最常见的哈希算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示：

```python
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())	# d26a53750bc40b38b65a520292f69306
```

如果数据量很大，可以分块多次调用 `update()` ，最后计算的结果是一样的：

```python
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())	# d26a53750bc40b38b65a520292f69306
```

另一种常见的哈希算法是SHA1，调用SHA1和调用MD5完全类似：

```python
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())	# 2c76b57293ce30acef38d98f6046927161b46a44
```

SHA1的结果是160 bit/20字节，通常用一个40位的16进制字符串表示。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且哈希长度更长。

任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：

| **name** | **password** |
| -------- | ------------ |
| michael  | 123456       |
| bob      | abc789       |
| alice    | alice2025    |

如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。这些都会有安全隐患。 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的哈希，比如MD5：

| **name** | **password**                     |
| :------- | -------------------------------- |
| michael  | e10adc3949ba59abbe56e057f20f883e |
| bob      | 440cbbedf1e789ad49ac0969d2d8069a |
| alice    | 78d03b2810a74e5751c02db550798676 |

当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。

采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。考虑这么个情况，很多用户喜欢用”123456“，”888888“，”password“这些简单的口令。于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：

```python
hash_to_plain = {
 'e10adc3949ba59abbe56e057f20f883e': '123456',
 '21218cca77804d2ba1922c33e0151105': '888888',
 '5f4dcc3b5aa765d61d8327deb882cf99': 'password',
 '...': '...'
}
```

这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？ 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

```python
def calc_md5(password):
    return get_md5(password + 'the-Salt')
```

经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

### 6. hmac

HMAC算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。

此外，和我们自定义的加salt算法不同，hmac算法针对所有哈希算法都通用，无论是MD5还是SHA1。采用hmac算法替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

Python自带的 `hmac` 模块实现了标准的HMAC算法，下面我们来看看如何实现：

```python
import hmac

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest()  # 'fa4ee7d173f2d97ee79022d1a7355bcf'
```

可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str需要首先编码为bytes。
