# count e um contado infinto que e importado pelo itertools
# exemplo de como e o "count"
from itertools import count

c1 = count(start=9, step=9)
r1 = range(9, 100, 9)
print("c1", hasattr(c1, '__iter__'))
print("c1", hasattr(c1, '__next__'))
print("r1", hasattr(r1, '__iter__'))
print("r1", hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)
