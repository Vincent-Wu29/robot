def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("输入："))
print(is_prime(num))