def add(a, b):
    return a + b

def sub(a, b):
    return a- b

def mult(a, b):
    return a * b

def dev(a, b):
    return a / b

def print_menu():
    print("菜单界面：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 退出")

while True:
    print_menu()

    oper = int(input())
    if oper == 5:
        break
    input_nums = input("输入(a,b)：").split(',')
    num1 = int(input_nums[0])
    num2 = int(input_nums[1])

    match oper:
        case 1:
            print(add(num1 ,num2))
        case 2:
            print(sub(num1, num2))
        case 3:
            print(mult(num1, num2))
        case 4:
            print(dev(num1, num2))