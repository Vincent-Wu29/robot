task1 = [x**2 for x in range(1,21) if x % 2 != 0]

lst1 = ["apple", "banana", "cherry", "date"]
task2 = [x for x in lst1 if len(x) > 5]

lst2 = [1,2,3]
lst3 = ['a','b','c']
task3 = [str(a)+b for a in lst2 for b in lst3]

string = "hello world".split()
task4 = [s[0].upper()+s[1:] for s in string]

print(task1)
print(task2)
print(task3)
print(task4)