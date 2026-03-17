list = [1, 2, 3, 7, 5]

sum = 0
for num in list:
    sum += num

print(f"总和：{sum}")
average = sum / len(list)
print(f"平均值：{average:.2f}")