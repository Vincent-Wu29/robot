# 🤖 机器人软件工程师学习计划 - 第3天任务

**日期**：______2026.03.18_______
**学习阶段**：第一阶段 - 第1-2周（编程基础强化）
**预计学习时间**：4-5小时
**当前进度**：第3天 / 第1周

---

## 🎯 今日学习目标
1. 掌握函数进阶：可变参数(*args)和关键字参数(**kwargs)
2. 理解递归函数概念，能够编写简单递归函数
3. 掌握列表推导式的高效写法
4. 学习字符串常用操作方法
5. 完成LeetCode第9题：回文数

---

## 📚 具体学习内容

### 1. 函数进阶：可变参数与关键字参数（1小时）
**学习资源**：
- **廖雪峰Python教程**：https://www.liaoxuefeng.com/wiki/1016959663602400
  - 第4章：Python基础 → 函数的参数
- **Python官方Tutorial**：https://docs.python.org/3/tutorial/
  - 4.7.2. Keyword Arguments
  - 4.7.3. Special parameters

**重点掌握内容**：
- 位置参数、默认参数、可变参数(*args)、关键字参数(**kwargs)
- 参数组合顺序规则：位置参数→默认参数→*args→**kwargs
- 解包参数：使用*和**传递列表/字典作为参数

**代码示例**：
```python
# 可变参数 *args：接收任意数量的位置参数
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))      # 输出: 6
print(sum_all(1, 2, 3, 4, 5)) # 输出: 15

# 关键字参数 **kwargs：接收任意数量的关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Beijing")

# 参数组合
def complex_func(a, b=10, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

complex_func(1, 2, 3, 4, 5, x=100, y=200)
```

### 2. 递归函数基础（1小时）
**学习资源**：
- **廖雪峰Python教程**：
  - 第4章：Python基础 → 递归函数
- **Python官方Tutorial**：
  - 递归相关概念

**重点掌握内容**：
- 递归定义：函数调用自身
- 递归三要素：基本情况、递归情况、向基本情况推进
- 递归调用栈概念
- 递归与循环的比较

**代码示例**：
```python
# 阶乘：n! = n × (n-1) × ... × 1
def factorial(n):
    if n == 0 or n == 1:  # 基本情况
        return 1
    else:                  # 递归情况
        return n * factorial(n-1)

print(factorial(5))  # 输出: 120

# 斐波那契数列：F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

### 3. 列表推导式（45分钟）
**学习资源**：
- **廖雪峰Python教程**：
  - 第2章：Python基础 → 列表生成式
- **Python官方Tutorial**：
  - 5.1.3. List Comprehensions

**重点掌握内容**：
- 基础语法：[expression for item in iterable]
- 条件过滤：[expression for item in iterable if condition]
- 嵌套循环：[expression for item1 in iterable1 for item2 in iterable2]
- 与map/filter函数的对比

**代码示例**：
```python
# 基础列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 嵌套循环的列表推导式
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # [(0,0), (0,1), (0,2), (1,0), ...]

# 字符串处理
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']
```

### 4. 字符串常用方法（45分钟）
**学习资源**：
- **廖雪峰Python教程**：
  - 第2章：Python基础 → 使用字符串
- **Python官方文档**：
  - https://docs.python.org/3/library/stdtypes.html#string-methods

**重点掌握内容**：
- 字符串分割与连接：split(), join()
- 大小写转换：upper(), lower(), title()
- 去除空白：strip(), lstrip(), rstrip()
- 查找与替换：find(), index(), replace()
- 判断方法：startswith(), endswith(), isdigit(), isalpha()

**代码示例**：
```python
text = "  Hello, World! Python is awesome.  "

# 去除空白
clean_text = text.strip()
print(clean_text)  # "Hello, World! Python is awesome."

# 分割字符串
words = clean_text.split()
print(words)  # ['Hello,', 'World!', 'Python', 'is', 'awesome.']

# 连接字符串
new_text = "-".join(words)
print(new_text)  # "Hello,-World!-Python-is-awesome."

# 查找与替换
position = clean_text.find("Python")
print(f"Python位置: {position}")  # 14

replaced = clean_text.replace("awesome", "fantastic")
print(replaced)  # "Hello, World! Python is fantastic."

# 判断方法
print("Hello".startswith("He"))  # True
print("123".isdigit())           # True
print("abc".isalpha())           # True
```

### 5. LeetCode第9题：回文数（1小时）
**题目信息**：
- **题目**：9. 回文数（Palindrome Number）
- **难度**：简单
- **链接**：https://leetcode.com/problems/palindrome-number/
- **中文链接**：https://leetcode.cn/problems/palindrome-number/

**题目描述**：
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例**：
```
输入：x = 121
输出：true

输入：x = -121
输出：false
解释：从左向右读为 -121，从右向左读为 121-，因此不是回文数。

输入：x = 10
输出：false
解释：从右向左读为 01，因此不是回文数。
```

**解题思路引导**：
1. 特殊情况处理：负数不是回文数，个位数是回文数
2. 方法一：转换为字符串，判断反转后是否相等
3. 方法二：数学方法，反转数字的一半进行比较
4. 思考：哪种方法更优？为什么？

---

## 💻 编程练习题目

### 必做练习（完成所有6题）

**练习1：可变参数计算器**

```python
# 要求：编写函数calculate(operation, *args)
# operation可以是："sum", "product", "average"
# *args接收任意数量的数字参数
# 根据operation计算并返回结果
# 示例：
# calculate("sum", 1, 2, 3, 4) → 10
# calculate("product", 2, 3, 4) → 24
# calculate("average", 10, 20, 30) → 20.0
```

**练习2：学生信息收集函数**
```python
# 要求：编写函数collect_student_info(**kwargs)
# 接收任意关键字参数作为学生信息
# 返回格式化的字符串：每行显示一个字段
# 示例：
# collect_student_info(name="Alice", age=20, major="CS")
# 输出：
# name: Alice
# age: 20
# major: CS
```

**练习3：递归实现列表求和**
```python
# 要求：使用递归实现列表求和函数recursive_sum(lst)
# 不使用循环，使用递归计算列表中所有元素的和
# 思路：
# 基本情况：空列表返回0
# 递归情况：返回第一个元素 + 剩余列表的和
# 示例：
# recursive_sum([1, 2, 3, 4]) → 10
```

**练习4：列表推导式应用**

```python
# 要求：使用列表推导式完成以下任务：
# 1. 生成1-20中所有奇数的平方列表
# 2. 从字符串列表["apple", "banana", "cherry", "date"]中提取长度大于5的单词
# 3. 生成两个列表[1,2,3]和['a','b','c']的所有组合对
# 4. 将字符串"hello world"转换为每个单词首字母大写的列表
```

**练习5：字符串处理函数**

```python
# 要求：编写函数process_text(text)
# 功能：
# 1. 去除两端空白
# 2. 将所有单词转换为小写
# 3. 统计单词数量
# 4. 返回处理后的文本和单词数量（元组形式）
# 示例：
# process_text("  Hello World! Python is GREAT.  ")
# 返回：("hello world! python is great.", 5)
```

**练习6：LeetCode回文数**
```python
# 要求：在LeetCode上完成"回文数"题目
# 实现至少两种解法：
# 1. 字符串反转法
# 2. 数学反转法（反转一半数字）
# 提交代码并通过所有测试用例
```

### 挑战练习（可选）
```python
# 汉诺塔问题（递归经典）
# 要求：编写函数hanoi(n, source, target, auxiliary)
# 打印移动步骤
# 参数：n-盘子数量，source-起始柱，target-目标柱，auxiliary-辅助柱
# 示例：
# hanoi(3, 'A', 'C', 'B')
# 输出：
# 移动 盘子1 从 A 到 C
# 移动 盘子2 从 A 到 B
# 移动 盘子1 从 C 到 B
# 移动 盘子3 从 A 到 C
# 移动 盘子1 从 B 到 A
# 移动 盘子2 从 B 到 C
# 移动 盘子1 从 A 到 C
```

---

## ⏰ 时间分配建议

| 时间段 | 活动 | 时长 | 具体任务 |
|--------|------|------|----------|
| **上午/开始** | 函数进阶学习 | 60分钟 | 学习*args/**kwargs，完成练习1-2 |
| | 递归函数学习 | 60分钟 | 理解递归概念，完成练习3 |
| **中午/休息后** | 列表推导式 | 45分钟 | 掌握推导式语法，完成练习4 |
| | 字符串方法 | 45分钟 | 学习常用字符串方法，完成练习5 |
| **下午/晚上** | LeetCode解题 | 60分钟 | 理解题目，完成练习6 |
| | 综合练习 | 60分钟 | 尝试挑战练习，整理代码 |
| | 总结整理 | 30分钟 | 整理学习笔记，准备明天学习 |

**高效学习建议**：
1. 递归学习要画图理解调用栈
2. 列表推导式要对比传统循环写法
3. 字符串方法多用help()或dir()查看
4. LeetCode题目先自己思考，再看题解

---

## 📦 预期产出物

### 1. 代码文件
在`c:\learn\robot\python_basics\day_03\`目录下创建以下文件：
```
python_basics/day_03/
├── calculator_args.py        # 练习1
├── student_info.py           # 练习2
├── recursive_list_sum.py     # 练习3
├── list_comprehensions.py    # 练习4
├── text_processor.py         # 练习5
└── hanoi_tower.py           # 挑战练习
```
在`c:\learn\robot\leetcode\`目录下更新：
```
leetcode/
├── two_sum.py               # 第2天题目
└── palindrome_number.py     # 第3天题目
```

### 2. 学习笔记
在`c:\learn\robot\learning_notes\`目录下更新：
```
learning_notes/
├── day_01_notes.md          # 第1天笔记
├── day_02_notes.md          # 第2天笔记
└── day_03_notes.md          # 第3天笔记
```
**第3天笔记内容应包括**：
- 可变参数与关键字参数的理解
- 递归函数的学习心得（调用栈理解）
- 列表推导式的优势与应用场景
- 字符串常用方法的记忆技巧
- LeetCode回文数解题思路
- 遇到的问题及解决方案

### 3. LeetCode进展
- [x] 完成"回文数"题目
- [x] 实现至少两种解法
- [x] 理解时间复杂度差异
- [x] 提交代码并通过测试

---

## 🔍 常见问题与解决方案

### Q1：递归深度错误
- **症状**：RecursionError: maximum recursion depth exceeded
- **解决**：
  1. 检查递归基本情况是否正确
  2. 确保每次递归都向基本情况推进
  3. Python默认递归深度1000，过大问题需优化算法

### Q2：列表推导式语法错误
- **症状**：SyntaxError: invalid syntax
- **解决**：
  1. 检查括号是否匹配
  2. 确保表达式在前，for/if在后
  3. 嵌套循环顺序要正确

### Q3：字符串方法忘记返回值
- **症状**：字符串方法调用后原始字符串未改变
- **解决**：字符串是不可变对象，方法返回新字符串
  ```python
  text = "hello"
  text.upper()      # 返回"HELLO"，但text仍是"hello"
  text = text.upper()  # 正确：重新赋值
  ```

### Q4：*args和**kwargs混淆
- **解决**：
  - *args：接收位置参数，在函数内是元组
  - **kwargs：接收关键字参数，在函数内是字典
  - 顺序：def func(a, b=1, *args, **kwargs)

### Q5：回文数数学解法思路
- **提示**：
  1. 反转整个数字：可能会溢出
  2. 反转一半数字：当原始数字小于等于反转数字时停止
  3. 注意处理以0结尾的数字（除了0本身）

---

## 📝 学习效果自查清单

今日学习结束时，检查以下项目：

### 知识掌握
- [x] 能够正确使用*args和**kwargs定义函数
- [x] 理解递归函数的基本原理
- [x] 能够编写简单的列表推导式
- [x] 掌握常用字符串方法（split/join/strip等）
- [x] 理解回文数的两种解法

### 技能应用
- [x] 完成全部6个必做练习
- [x] 实现可变参数计算器
- [x] 编写正确的递归求和函数
- [x] 在LeetCode上提交"回文数"代码
- [x] 理解每个练习的代码逻辑

### 习惯养成
- [x] 创建了第3天的代码目录
- [x] 更新了学习笔记
- [x] 记录了递归调用的理解
- [x] 整理了字符串方法速查表
- [x] 规划了明天学习重点

---

## 🎪 扩展资源（学有余力时使用）

1. **递归优化**：
   - 学习尾递归优化概念
   - 了解Python不支持尾递归优化
   - 使用循环或迭代器替代深度递归

2. **生成器表达式**：
   - 与列表推导式类似，但返回生成器
   - 更节省内存
   ```python
   # 列表推导式（立即计算）
   squares = [x**2 for x in range(1000000)]
   
   # 生成器表达式（惰性计算）
   squares_gen = (x**2 for x in range(1000000))
   ```

3. **f-string格式化**：
   - Python 3.6+的新特性
   - 更简洁的字符串格式化
   ```python
   name = "Alice"
   age = 25
   print(f"{name} is {age} years old.")
   ```

4. **LeetCode学习**：
   - 学习第13题：罗马数字转整数
   - 巩固字符串处理方法
   - 练习简单算法思维

---

## 🔜 明日预告

**第4天学习重点**：
- Python数据结构：列表、元组、字典、集合
- 列表的增删改查操作
- 字典的常用方法
- 集合运算
- 数据结构的综合应用练习

---

## 💪 鼓励的话

> "今天你学习了函数的高级特性、递归思维和高效的数据处理方式。递归是编程中重要的思维方式，虽然刚开始可能觉得绕，但一旦掌握，就能优雅地解决复杂问题。列表推导式和字符串方法让代码更简洁高效，这正是Python的魅力所在。LeetCode的回文数问题让你开始思考算法效率，这是成为优秀工程师的重要一步！"

**完成今日任务后**，请：
1. 在本文档顶部填写日期
2. 勾选学习效果自查清单
3. 更新TASKS_INDEX.md中的进度
4. 准备开始第4天的学习

---
**生成时间**：2026-03-17
**下次任务生成**：完成第3天学习后，请求生成第4天任务