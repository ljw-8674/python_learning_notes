import re

def is_valid_email(addr):
    pattern = r'^[A-Za-z.#]+@[A-Za-z]+\.com$'  # []里的.不用转义
    return re.match(pattern, addr)

def name_of_email(addr):
    pattern = r'(?:<([^>]+)>\s)?([A-Za-z]+)@'  # 1.^出现在字符类的前面表示取反 2.用非捕获分组避免group编号混乱
    m = re.search(pattern, addr)
    if m:
        return m.group(1) if m.group(1) else m.group(2)

# 测试1:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# 测试2:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
