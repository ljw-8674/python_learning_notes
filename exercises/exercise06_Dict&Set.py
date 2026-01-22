d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)

# Add
d['Adam'] = 67
d['Tmp'] = 99
print(d)

# Delete
d.pop('Tmp')
print(d)
del d['Adam']
print(d)

# Modify
d['Tracy'] = 60
print(d)

# Search
print('Thomas' in d)
print(d.get('Thomas',-1))



s = set([1, 1, 2, 2, 3])
print(s)

# Add
s.add(3)
s.add(4)
s.add('666')
print(s)

# Delete
try:
    n = 666
    s.remove(n)
except KeyError:
    print(f'no element: {n}')
print(s)
s.discard(n)
print(s)

s.discard('666')
print(s)

# Intersection
s2 = {3, 4}
print(s & s2)

# union
s3 = {5, 6}
print(s | s3)

