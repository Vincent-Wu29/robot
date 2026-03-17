import math
import numbers


def list_stats(numbers):
    max, min, sum = 0, 1000, 0
    for num in numbers:
        if (num > max):
            max = num
        if (num < min):
            min = num
        sum += num
    return (max, min, sum / len(numbers))

print(list_stats([1, 2, 3, 4, 5]))