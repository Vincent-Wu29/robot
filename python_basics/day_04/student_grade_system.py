# 学生成绩管理系统

# 数据存储结构：{学号: {姓名: "", 成绩: []}}
students = {}


def add_student():
    """添加学生"""
    student_id = input("请输入学号: ").strip()
    
    if student_id in students:
        print(f"❌ 学号 {student_id} 已存在！")
        return
    
    name = input("请输入姓名: ").strip()
    if not name:
        print("❌ 姓名不能为空！")
        return
    
    students[student_id] = {
        "姓名": name,
        "成绩": []
    }
    print(f"✅ 学生 {name}（学号：{student_id}）添加成功！")


def delete_student():
    """删除学生"""
    student_id = input("请输入要删除的学号: ").strip()
    
    if student_id not in students:
        print(f"❌ 学号 {student_id} 不存在！")
        return
    
    name = students[student_id]["姓名"]
    del students[student_id]
    print(f"✅ 学生 {name}（学号：{student_id}）已删除！")


def query_student():
    """查询学生信息"""
    student_id = input("请输入学号: ").strip()
    
    if student_id not in students:
        print(f"❌ 学号 {student_id} 不存在！")
        return
    
    info = students[student_id]
    scores = info["成绩"]
    avg = sum(scores) / len(scores) if scores else 0
    
    print(f"\n{'='*40}")
    print(f"学号: {student_id}")
    print(f"姓名: {info['姓名']}")
    print(f"成绩: {scores if scores else '暂无成绩'}")
    print(f"平均分: {avg:.2f}")
    print(f"{'='*40}")


def add_score():
    """添加成绩"""
    student_id = input("请输入学号: ").strip()
    
    if student_id not in students:
        print(f"❌ 学号 {student_id} 不存在！")
        return
    
    try:
        score = float(input("请输入成绩: "))
        if not (0 <= score <= 100):
            print("❌ 成绩必须在 0-100 之间！")
            return
    except ValueError:
        print("❌ 请输入有效的数字！")
        return
    
    students[student_id]["成绩"].append(score)
    name = students[student_id]["姓名"]
    print(f"✅ 已为 {name} 添加成绩 {score}！")


def calculate_average():
    """计算每个学生的平均分"""
    if not students:
        print("暂无学生数据！")
        return
    
    print(f"\n{'='*50}")
    print(f"{'学号':<10}{'姓名':<10}{'成绩':<20}{'平均分':<10}")
    print("-" * 50)
    
    for student_id, info in students.items():
        scores = info["成绩"]
        avg = sum(scores) / len(scores) if scores else 0
        scores_str = str(scores) if scores else "[]"
        print(f"{student_id:<10}{info['姓名']:<10}{scores_str:<20}{avg:<10.2f}")
    
    print(f"{'='*50}")


def find_highest_average():
    """找出平均分最高的学生"""
    if not students:
        print("暂无学生数据！")
        return
    
    max_avg = -1
    top_students = []
    
    for student_id, info in students.items():
        scores = info["成绩"]
        if not scores:
            continue
        avg = sum(scores) / len(scores)
        
        if avg > max_avg:
            max_avg = avg
            top_students = [(student_id, info["姓名"], avg)]
        elif avg == max_avg:
            top_students.append((student_id, info["姓名"], avg))
    
    if not top_students:
        print("暂无学生有成绩记录！")
        return
    
    print(f"\n{'='*40}")
    print("🏆 平均分最高的学生：")
    for student_id, name, avg in top_students:
        print(f"   学号: {student_id}")
        print(f"   姓名: {name}")
        print(f"   平均分: {avg:.2f}")
    print(f"{'='*40}")


def show_menu():
    """显示菜单"""
    print(f"\n{'='*40}")
    print("      📚 学生成绩管理系统")
    print(f"{'='*40}")
    print("   1. 添加学生")
    print("   2. 删除学生")
    print("   3. 查询学生信息")
    print("   4. 添加成绩")
    print("   5. 计算每个学生的平均分")
    print("   6. 找出平均分最高的学生")
    print("   0. 退出系统")
    print(f"{'='*40}")


def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请选择操作（0-6）: ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            query_student()
        elif choice == "4":
            add_score()
        elif choice == "5":
            calculate_average()
        elif choice == "6":
            find_highest_average()
        elif choice == "0":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 无效选择，请重新输入！")


# 运行程序
if __name__ == "__main__":
    main()