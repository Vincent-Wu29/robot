from unittest import result


user_input = input('输入：')

user_input = user_input.split(',')

oper_num1 = int(user_input[0])
oper_num2 = int(user_input[1])
oper_char = user_input[2][1]

match oper_char:
    case '+':
        result = oper_num1 + oper_num2
    case '-':
        result = oper_num1 - oper_num2
    case "*":
        result = oper_num1 * oper_num2
    case '/':
        result = oper_num1 / oper_num2

print(f"输出：{result}")


