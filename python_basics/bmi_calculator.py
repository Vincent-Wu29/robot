weight = float(input("体重(kg)："))
height = float(input("身高(m)："))


bmi = weight / height**2

if bmi < 18.5:
    print(f"你的BMI：{bmi:.1f}，偏瘦")
elif bmi >= 18.5 and bmi < 24:
    print(f"你的BMI：{bmi:.1f}，正常")
elif bmi >= 24 and bmi < 28:
    print(f"你的BMI：{bmi:.1f}，超重")
else:
    print(f"你的BMI：{bmi:.1f}，肥胖")