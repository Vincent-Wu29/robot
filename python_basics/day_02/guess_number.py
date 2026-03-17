from random import randint

number = randint(1, 100)

for i in range(5):
    guess_number = int(input("输入："))
    if (guess_number > number):
        print("太大")
    elif (guess_number < number):
        print("太小")
    else:
        print("恭喜你猜对了")
        break
    
    if i == 4:
        print(f"游戏结束，数字是{number}")