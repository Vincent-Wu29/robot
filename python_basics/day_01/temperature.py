temperature_f = input('输入(华氏温度)：')
temperature_f = float(temperature_f)

temperature_c = (temperature_f - 32) * 5 / 9
print(f"输出(摄氏温度)：{temperature_c:0.1f}")