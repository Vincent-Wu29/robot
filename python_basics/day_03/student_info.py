def collect_student_info(**kwargs):
    result = ""
    for k, v in kwargs.items():
        result += f"{k}：{v}\n"

    return result

print(collect_student_info(name="Alice", age=20, major="cs"))