
from random import randint


list1 = []
for i in range(10):
    list1.append(randint(1, 100))

list_asc = sorted(list1)
list_desc = sorted(list1, reverse=True)

max = max(list1)
min = min(list1)
average = sum(list1) / len(list1)

list_ahead = list1[:5]
list_behand = list1[5:]

list_insert = list1.copy()
for i in range(3):
    list_insert.insert(5, randint(1, 100))

list_remove = [x for x in list1 if x % 2 != 0]

print(list1)
print(list_asc)
print(list_desc)
print(max)
print(min)
print(average)
print(list_ahead)
print(list_behand)
print(list_insert)
print(list_remove)
