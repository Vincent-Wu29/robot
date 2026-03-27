# 🤖 机器人软件工程师学习计划 - 第5天任务

**日期**：_________2026.03.20____
**学习阶段**：第一阶段 - 第1-2周（编程基础强化）
**预计学习时间**：5-6小时
**当前进度**：第5天 / 第1周

---

## 🎯 今日学习目标
1. 综合应用前4天学习的Python知识完成一个完整的项目
2. 掌握文件操作：读写文本文件、数据持久化
3. 学习异常处理：try/except/else/finally结构
4. 实践模块化编程：将项目拆分为多个模块
5. 完成LeetCode第14题：最长公共前缀

---

## 📚 具体学习内容

### 1. 文件操作基础（1小时）
**学习资源**：
- **廖雪峰Python教程**：https://www.liaoxuefeng.com/wiki/1016959663602400
  - 第7章：IO编程 → 文件读写
- **Python官方Tutorial**：https://docs.python.org/3/tutorial/
  - 7.2. Reading and Writing Files

**重点掌握内容**：
- 文件打开模式：`'r'`(读)、`'w'`(写)、`'a'`(追加)、`'b'`(二进制)
- 文件操作步骤：打开(`open()`)、读取/写入、关闭(`close()`)
- 使用`with`语句自动管理文件资源
- 文件读取方法：`read()`、`readline()`、`readlines()`
- 文件写入方法：`write()`、`writelines()`

**代码示例**：
```python
# 写入文件
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, World!\n")
    f.write("这是第二行\n")

# 读取文件
with open('data.txt', 'r', encoding='utf-8') as f:
    content = f.read()  # 读取全部内容
    print(content)

# 逐行读取
with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())  # 去除换行符

# 读取所有行到列表
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)  # ['Hello, World!\n', '这是第二行\n']
```

### 2. 异常处理（1小时）
**学习资源**：
- **廖雪峰Python教程**：
  - 第7章：IO编程 → 错误处理
- **Python官方Tutorial**：
  - 8. Errors and Exceptions

**重点掌握内容**：
- 异常处理结构：`try`、`except`、`else`、`finally`
- 捕获特定异常：`except ValueError`、`except FileNotFoundError`
- 捕获多个异常：`except (ValueError, TypeError)`
- 获取异常信息：`except Exception as e`
- 抛出异常：`raise`语句
- 自定义异常类

**代码示例**：
```python
# 基本异常处理
try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")
except ValueError:
    print("输入的不是有效数字!")
except ZeroDivisionError:
    print("不能除以零!")
except Exception as e:
    print(f"发生了未知错误: {e}")
else:
    print("计算成功!")
finally:
    print("程序执行完毕。")

# 文件操作中的异常处理
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在!")
except PermissionError:
    print("没有文件访问权限!")
except IOError as e:
    print(f"文件读写错误: {e}")

# 抛出异常
def validate_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄不能超过150")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"验证失败: {e}")
```

### 3. 模块与包（45分钟）
**学习资源**：
- **廖雪峰Python教程**：
  - 第6章：模块
- **Python官方Tutorial**：
  - 6. Modules

**重点掌握内容**：
- 模块导入：`import`、`from ... import`
- `__name__`变量的作用：判断模块是否作为主程序运行
- 创建自己的模块
- 包（package）的概念和结构
- 相对导入和绝对导入

**代码示例**：
```python
# math_utils.py 模块文件
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    # 测试代码，只有当直接运行此模块时执行
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(2, 3) = {multiply(2, 3)}")
    print(f"factorial(5) = {factorial(5)}")

# main.py 主程序文件
import math_utils as mu
from math_utils import add, multiply

# 使用模块
result1 = mu.add(10, 20)
result2 = multiply(10, 20)  # 直接使用导入的函数
result3 = mu.factorial(5)

print(f"加法结果: {result1}")
print(f"乘法结果: {result2}")
print(f"阶乘结果: {result3}")
```

### 4. 综合项目：学生信息管理系统（2小时）
**项目概述**：
开发一个完整的学生信息管理系统，包含以下功能：

1. 学生信息的增删改查
2. 成绩管理
3. 数据持久化（文件存储）
4. 异常处理
5. 模块化设计

**技术栈**：
- 数据结构：列表、字典
- 函数：模块化功能
- 文件操作：数据保存与加载
- 异常处理：输入验证和错误处理
- 控制结构：循环、条件判断

**系统架构**：
```
student_management_system/
├── main.py              # 主程序入口
├── student.py           # 学生类定义
├── database.py          # 数据持久化模块
├── utils.py             # 工具函数模块
└── data/
    └── students.json    # 数据文件
```

### 5. LeetCode第14题：最长公共前缀（1小时）
**题目信息**：
- **题目**：14. 最长公共前缀（Longest Common Prefix）
- **难度**：简单
- **链接**：https://leetcode.com/problems/longest-common-prefix/
- **中文链接**：https://leetcode.cn/problems/longest-common-prefix/

**题目描述**：
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 `""`。

**示例**：
```
输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```

**解题思路引导**：
1. 方法一：水平扫描法
   - 取第一个字符串作为初始前缀
   - 依次与后续字符串比较，不断缩短前缀
2. 方法二：垂直扫描法
   - 比较所有字符串的第一个字符，然后第二个字符，依此类推
   - 遇到不匹配的字符时停止
3. 方法三：分治法
   - 将问题分解为子问题
   - 分别求左半部分和右半部分的最长公共前缀
   - 合并结果

---

## 💻 编程练习题目

### 必做练习（完成所有4题）

**练习1：文件操作练习**
```python
# 要求：
# 1. 创建一个学生成绩文件（CSV格式），包含：学号,姓名,数学成绩,英语成绩,编程成绩
# 2. 编写函数读取文件内容，计算每个学生的平均分和总分
# 3. 将计算结果写入新的文件，格式：学号,姓名,平均分,总分,等级(A/B/C/D/F)
# 4. 统计各等级人数并输出
# 等级划分：90+ A, 80-89 B, 70-79 C, 60-69 D, <60 F
```

**练习2：异常处理练习**
```python
# 要求：编写一个安全的计算器程序
# 1. 实现加减乘除运算函数，每个函数都要进行参数验证
# 2. 使用异常处理处理以下情况：
#    - 输入非数字
#    - 除数为零
#    - 无效的操作符
#    - 文件读写错误（如果使用文件记录计算历史）
# 3. 添加日志功能，记录每次计算（成功或失败）
# 4. 实现重试机制：当输入错误时允许重新输入
```

**练习3：模块化编程练习**
```python
# 要求：将练习1和练习2的功能模块化
# 创建以下模块：
# 1. file_operations.py：文件读写相关函数
# 2. calculator.py：计算器功能函数
# 3. validation.py：输入验证函数
# 4. logger.py：日志记录函数
# 5. main.py：主程序，整合所有模块
# 使用if __name__ == "__main__": 确保模块可独立运行
```

**练习4：LeetCode最长公共前缀**
```python
# 要求：在LeetCode上完成"最长公共前缀"题目
# 1. 实现至少两种解法（水平扫描和垂直扫描）
# 2. 分析两种解法的时间复杂度和空间复杂度
# 3. 提交代码并通过所有测试用例
# 4. 尝试优化解法，减少不必要的比较
```

### 综合项目：学生信息管理系统
**项目要求**：

**步骤1：设计数据结构**
```python
# student.py
class Student:
    def __init__(self, student_id, name, age, gender):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.scores = {}  # 课程名: 成绩

    def add_score(self, course, score):
        self.scores[course] = score

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'scores': self.scores
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['student_id'], data['name'], data['age'], data['gender'])
        student.scores = data.get('scores', {})
        return student
```

**步骤2：实现数据持久化模块**
```python
# database.py
import json
import os

class StudentDatabase:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        # 从文件加载数据
        pass

    def save_data(self):
        # 保存数据到文件
        pass

    def add_student(self, student):
        # 添加学生
        pass

    def delete_student(self, student_id):
        # 删除学生
        pass

    def find_student(self, student_id):
        # 查找学生
        pass

    def update_student(self, student_id, **kwargs):
        # 更新学生信息
        pass
```

**步骤3：实现用户界面和业务逻辑**
```python
# main.py
import sys
from student import Student
from database import StudentDatabase

class StudentManagementSystem:
    def __init__(self):
        self.db = StudentDatabase()

    def run(self):
        while True:
            self.show_menu()
            choice = input("请选择操作: ")
            # 根据选择调用相应功能
            pass

    def show_menu(self):
        print("\n=== 学生信息管理系统 ===")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 查找学生")
        print("4. 更新学生信息")
        print("5. 添加成绩")
        print("6. 显示所有学生")
        print("7. 按平均分排序")
        print("8. 保存数据")
        print("9. 退出系统")
```

**步骤4：添加异常处理和输入验证**
```python
# utils.py
def validate_student_id(student_id):
    # 验证学号格式
    pass

def validate_age(age):
    # 验证年龄
    pass

def validate_score(score):
    # 验证成绩
    pass

def get_valid_input(prompt, validation_func, error_msg):
    # 获取有效输入
    pass
```

**完整功能列表**：
- [ ] 学生信息的增删改查
- [ ] 成绩管理（添加、修改、删除成绩）
- [ ] 数据统计（平均分、最高分、最低分）
- [ ] 数据排序（按学号、姓名、平均分）
- [ ] 数据持久化（JSON格式）
- [ ] 输入验证和异常处理
- [ ] 友好的用户界面

---

## ⏰ 时间分配建议

| 时间段 | 活动 | 时长 | 具体任务 |
|--------|------|------|----------|
| **上午/开始** | 文件操作学习 | 60分钟 | 学习文件读写，完成练习1 |
| | 异常处理学习 | 60分钟 | 学习异常处理，完成练习2 |
| **中午/休息后** | 模块化编程 | 45分钟 | 学习模块导入，完成练习3 |
| | LeetCode解题 | 60分钟 | 理解题目，完成练习4 |
| **下午/晚上** | 综合项目设计 | 60分钟 | 设计学生信息管理系统结构 |
| | 项目实现 | 90分钟 | 实现核心功能模块 |
| | 测试与调试 | 60分钟 | 测试系统功能，修复bug |
| **总结整理** | 复习总结 | 45分钟 | 整理学习笔记，准备明天学习 |

**高效学习建议**：
1. 先完成基础练习，再开始综合项目
2. 项目开发遵循"设计-实现-测试"流程
3. 多使用异常处理提高程序健壮性
4. 模块化设计让代码更清晰

---

## 📦 预期产出物

### 1. 代码文件
在`c:\learn\robot\python_basics\day_05\`目录下创建以下文件：
```
python_basics/day_05/
├── file_operations.py       # 练习1
├── safe_calculator.py       # 练习2
├── modular_programming/     # 练习3
│   ├── file_operations.py
│   ├── calculator.py
│   ├── validation.py
│   ├── logger.py
│   └── main.py
└── student_management_system/ # 综合项目
    ├── student.py
    ├── database.py
    ├── utils.py
    ├── main.py
    └── data/
        └── students.json
```
在`c:\learn\robot\leetcode\`目录下更新：
```
leetcode/
├── two_sum.py              # 第2天题目
├── palindrome_number.py    # 第3天题目
├── roman_to_integer.py     # 第4天题目
└── longest_common_prefix.py # 第5天题目
```

### 2. 学习笔记
在`c:\learn\robot\learning_notes\`目录下更新：
```
learning_notes/
├── day_01_notes.md         # 第1天笔记
├── day_02_notes.md         # 第2天笔记
├── day_03_notes.md         # 第3天笔记
├── day_04_notes.md         # 第4天笔记
└── day_05_notes.md         # 第5天笔记
```
**第5天笔记内容应包括**：
- 文件操作的关键点和注意事项
- 异常处理的最佳实践
- 模块化设计的好处和方法
- 综合项目的架构设计思路
- LeetCode最长公共前缀解题思路
- 遇到的问题及解决方案

### 3. LeetCode进展
- [ ] 完成"最长公共前缀"题目
- [ ] 实现至少两种解法
- [ ] 分析算法复杂度
- [ ] 提交代码并通过测试

---

## 🔍 常见问题与解决方案

### Q1：文件编码问题
- **症状**：UnicodeDecodeError: 'gbk' codec can't decode byte
- **解决**：指定正确的编码，如`open('file.txt', 'r', encoding='utf-8')`
- **最佳实践**：始终明确指定文件编码

### Q2：文件路径问题
- **症状**：FileNotFoundError: [Errno 2] No such file or directory
- **解决**：
  1. 使用绝对路径或相对路径
  2. 检查文件是否存在：`os.path.exists('file.txt')`
  3. 创建目录：`os.makedirs('data', exist_ok=True)`

### Q3：异常处理过度
- **解决**：
  - 只捕获可能发生的异常
  - 不要使用过于宽泛的`except:`（会隐藏错误）
  - 将异常处理放在合适的层级

### Q4：模块循环导入
- **症状**：ImportError: cannot import name 'xxx' from partially initialized module
- **解决**：
  1. 重新设计模块依赖关系
  2. 将导入语句放在函数内部
  3. 使用延迟导入

### Q5：最长公共前缀算法
- **提示**：
  1. 处理空数组的情况
  2. 以第一个字符串为基准进行比较
  3. 使用`zip(*strs)`可以同时遍历所有字符串的对应字符
  4. 注意边界条件

---

## 📝 学习效果自查清单

今日学习结束时，检查以下项目：

### 知识掌握
- [ ] 能够进行文件的读写操作
- [ ] 掌握异常处理的基本结构
- [ ] 理解模块化编程的优势
- [ ] 能够设计简单的类结构
- [ ] 理解数据持久化的概念
- [ ] 理解最长公共前缀算法

### 技能应用
- [ ] 完成全部4个必做练习
- [ ] 实现学生信息管理系统核心功能
- [ ] 正确使用异常处理提高程序健壮性
- [ ] 在LeetCode上提交"最长公共前缀"代码
- [ ] 理解模块之间的依赖关系

### 习惯养成
- [ ] 创建了第5天的代码目录
- [ ] 更新了学习笔记
- [ ] 整理了项目架构图
- [ ] 记录了异常处理的最佳实践
- [ ] 规划了明天学习重点

---

## 🎪 扩展资源（学有余力时使用）

1. **JSON模块深入**：
   - `json.dump()`和`json.load()`处理文件
   - 自定义JSON编码解码器
   - 处理复杂对象序列化

2. **日志模块（logging）**：
   - 替代print进行调试
   - 配置日志级别和格式
   - 日志文件轮转

3. **配置文件**：
   - 使用`configparser`读取配置文件
   - 环境变量管理
   - 敏感信息处理

4. **单元测试**：
   - 使用`unittest`模块
   - 编写测试用例
   - 测试驱动开发（TDD）概念

5. **LeetCode学习**：
   - 学习第20题：有效的括号
   - 巩固栈数据结构的应用
   - 练习字符串匹配算法

---

## 🔜 明日预告

**第6天学习重点**：
- C++基础语法入门
- Python与C++语法对比
- C++在机器人开发中的优势
- 简单C++程序编写练习

---

## 💪 鼓励的话

> "今天是第一周的收尾，你将前面4天学习的所有知识整合到一个完整的项目中。文件操作和异常处理是实际开发中必不可少的技能，它们让你的程序更加健壮和可靠。模块化设计是大型项目的基石，良好的架构能让代码更易维护和扩展。学生信息管理系统虽然简单，但包含了真实软件开发的完整流程，这是你迈向专业开发者的重要一步！"

**完成今日任务后**，请：
1. 在本文档顶部填写日期
2. 勾选学习效果自查清单
3. 更新TASKS_INDEX.md中的进度
4. 准备开始第6天的学习

---
**生成时间**：2026-03-19
**下次任务生成**：完成第5天学习后，请求生成第6天任务