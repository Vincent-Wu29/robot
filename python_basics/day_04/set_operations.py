# 课程学生集合管理

# 初始化两个课程的学生集合
math_students = {"张三", "李四", "王五", "赵六", "孙七"}
physics_students = {"李四", "赵六", "周八", "吴九", "张三"}


def show_results():
    """显示集合运算结果"""
    print("=" * 40)
    print("数学课学生:", math_students)
    print("物理课学生:", physics_students)
    print("=" * 40)
    
    # 1. 同时选修两门课的学生（交集）
    both = math_students & physics_students
    print(f"\n📚 同时选修两门课的学生（交集）:")
    print(f"   学生: {both}")
    print(f"   人数: {len(both)}人")
    
    # 2. 只选修一门课的学生（对称差集）
    one_only = math_students ^ physics_students
    print(f"\n📖 只选修一门课的学生（对称差集）:")
    print(f"   学生: {one_only}")
    print(f"   人数: {len(one_only)}人")
    
    # 3. 所有选修课的学生（并集）
    all_students = math_students | physics_students
    print(f"\n👥 所有选修课的学生（并集）:")
    print(f"   学生: {all_students}")
    print(f"   人数: {len(all_students)}人")
    
    # 4. 从数学课转去物理课的学生（差集：只在数学，不在物理）
    # 理解为：原本在数学课，现在只在物理课（即离开数学的）
    math_to_physics = math_students - physics_students
    print(f"\n🔄 只在数学课不在物理课的学生（差集）:")
    print(f"   学生: {math_to_physics}")
    print(f"   人数: {len(math_to_physics)}人")
    
    # 反向差集：只在物理课不在数学课
    physics_only = physics_students - math_students
    print(f"\n🔄 只在物理课不在数学课的学生（差集）:")
    print(f"   学生: {physics_only}")
    print(f"   人数: {len(physics_only)}人")
    
    print("=" * 40)


# 运行
show_results()