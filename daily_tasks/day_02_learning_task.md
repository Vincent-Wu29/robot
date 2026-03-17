# 🤖 机器人软件工程师学习计划 - 第2天任务

**日期**：_________2026.03.17____
**学习阶段**：第一阶段 - 第1-2周（编程基础强化）
**预计学习时间**：4-5小时
**当前进度**：第2天 / 第1周

---

## 🎯 今日学习目标
1. 掌握Python条件语句（if/elif/else）的使用
2. 掌握循环语句（for/while）的编写与控制
3. 理解函数的基本概念，能够定义和调用简单函数
4. 完成第一个LeetCode简单题目

---

## 📚 具体学习内容

### 1. 条件语句学习（1小时）
**学习资源**：
- **廖雪峰Python教程**：https://www.liaoxuefeng.com/wiki/1016959663602400
  - 第4章：Python基础 → 条件判断
- **或Python官方Tutorial**：https://docs.python.org/3/tutorial/
  - 4.1. `if` Statements

**重点掌握内容**：
- `if`、`elif`、`else`的语法结构
- 条件表达式：`and`、`or`、`not`的使用
- 嵌套条件判断
- 三元表达式：`x if condition else y`

**代码示例**：
```python
# 基础if语句
age = 20
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# 多条件判断
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 三元表达式
result = "通过" if score >= 60 else "不通过"
```

### 2. 循环语句学习（1.5小时）
**学习资源**：
- **廖雪峰Python教程**：
  - 第4章：Python基础 → 循环
- **Python官方Tutorial**：
  - 4.2. `for` Statements
  - 4.3. The `range()` Function
  - 4.4. `break` and `continue` Statements, and `else` Clauses on Loops
  - 4.5. `pass` Statements

**重点掌握内容**：
- `for`循环遍历列表、字符串、range
- `while`循环与循环条件控制
- `break`、`continue`、`pass`的使用
- 嵌套循环
- 循环中的`else`子句

**代码示例**：
```python
# for循环
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# while循环
count = 0
while count < 5:
    print(count)
    count += 1

# break和continue
for i in range(10):
    if i == 3:
        continue  # 跳过3
    if i == 7:
        break     # 循环终止
    print(i)
```

### 3. 函数基础学习（1小时）
**学习资源**：
- **廖雪峰Python教程**：
  - 第4章：Python基础 → 函数
- **Python官方Tutorial**：
  - 4.7. Defining Functions

**重点掌握内容**：
- 函数的定义与调用：`def function_name():`
- 函数参数：位置参数、默认参数
- 返回值：`return`语句
- 函数的作用域概念

**代码示例**：
```python
# 简单函数定义
def greet(name):
    return f"Hello, {name}!"

# 调用函数
message = greet("Alice")
print(message)  # 输出: Hello, Alice!

# 带默认参数的函数
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # 输出: 9 (3²)
print(power(3, 3))  # 输出: 27 (3³)
```

### 4. LeetCode入门（1小时）
**平台介绍**：
- LeetCode：https://leetcode.com/（国际版）或 https://leetcode.cn/（中文版）
- 注册账号，熟悉界面

**第一个题目**：
- **题目**：1. 两数之和（Two Sum）
- **难度**：简单
- **链接**：https://leetcode.com/problems/two-sum/

**解题思路引导**：
1. 理解题目要求：在数组中找到两个数，使它们的和等于目标值
2. 思考暴力解法：两层循环遍历所有组合
3. 学习使用LeetCode的代码模板
4. 提交代码，查看结果

---

## 💻 编程练习题目

### 必做练习（完成所有6题）

**练习1：成绩等级判断**
```python
# 要求：编写程序，根据输入的成绩(0-100)输出等级
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, 0-59: F
# 示例：
# 输入：85
# 输出：B
```

**练习2：猜数字游戏**
```python
# 要求：程序随机生成一个1-100的整数，用户有5次机会猜测
# 每次猜错后提示"太大"或"太小"
# 猜对显示"恭喜你，猜对了！"，用完机会显示"游戏结束，数字是X"
# 提示：使用random模块的randint函数
```

**练习3：乘法表生成**

```python
# 要求：使用嵌套循环生成9×9乘法表
# 输出格式：
# 1×1=1   1×2=2   ...   1×9=9
# 2×1=2   2×2=4   ...   2×9=18
# ...
# 9×1=9   9×2=18  ...   9×9=81
```

**练习4：素数判断函数**
```python
# 要求：编写一个函数is_prime(n)，判断n是否为素数
# 素数定义：大于1的自然数，除了1和它本身以外不再有其他因数
# 函数返回True或False
# 示例：
# is_prime(7) → True
# is_prime(10) → False
```

**练习5：列表统计函数**

```python
# 要求：编写函数list_stats(numbers)，接收一个数字列表
# 返回：最大值、最小值、平均值（元组形式）
# 示例：
# list_stats([1, 2, 3, 4, 5]) → (5, 1, 3.0)
```

**练习6：LeetCode两数之和**
```python
# 要求：在LeetCode上完成"两数之和"题目
# 至少实现暴力解法（两层循环）
# 提交代码并通过测试用例
```

### 挑战练习（可选）
```python
# 编写一个简单的计算器程序，支持+ - * /运算
# 要求：使用函数封装每种运算
# 菜单界面：
# 1. 加法
# 2. 减法
# 3. 乘法
# 4. 除法
# 5. 退出
# 用户选择后，输入两个数字，输出结果，然后返回菜单
```

---

## ⏰ 时间分配建议

| 时间段 | 活动 | 时长 | 具体任务 |
|--------|------|------|----------|
| **上午/开始** | 条件语句学习 | 60分钟 | 学习if/elif/else，完成练习1 |
| | 循环语句学习 | 60分钟 | 学习for/while，完成练习2-3 |
| **中午/休息后** | 函数基础学习 | 60分钟 | 学习函数定义，完成练习4-5 |
| | LeetCode入门 | 60分钟 | 注册账号，理解题目，尝试练习6 |
| **下午/晚上** | 综合练习 | 60分钟 | 完成所有练习，尝试挑战练习 |
| | 总结整理 | 30分钟 | 整理代码，记录学习笔记 |

**高效学习建议**：
1. 先理解概念，再动手写代码
2. 对于每个练习，先自己思考解法，再参考提示
3. LeetCode题目不要怕困难，先实现暴力解法
4. 函数练习要注重参数传递和返回值

---

## 📦 预期产出物

### 1. 代码文件
在`c:\learn\robot\python_basics\`目录下创建以下文件：
```
python_basics/
├── day_02/
│   ├── grade_check.py       # 练习1
│   ├── guess_number.py      # 练习2
│   ├── multiplication_table.py # 练习3
│   ├── prime_checker.py     # 练习4
│   ├── list_statistics.py   # 练习5
│   └── calculator_menu.py   # 挑战练习
└── leetcode/
    └── two_sum.py           # 练习6
```

### 2. 学习笔记
在`c:\learn\robot\learning_notes\`目录下更新：
```
learning_notes/
├── day_01_notes.md          # 第1天笔记
└── day_02_notes.md          # 第2天笔记
```
**第2天笔记内容应包括**：
- 条件语句的关键点和易错点
- 循环控制的理解（break/continue区别）
- 函数定义的心得体会
- LeetCode初体验感受
- 遇到的问题及解决方案

### 3. LeetCode进展
- [x] 注册LeetCode账号
- [x] 完成"两数之和"题目
- [x] 理解题目描述和测试用例
- [x] 提交第一次代码（无论是否通过）

---

## 🔍 常见问题与解决方案

### Q1：条件语句缩进错误
- **症状**：IndentationError: expected an indented block
- **解决**：确保if/elif/else后面的代码有4个空格的缩进

### Q2：无限循环
- **症状**：while循环无法终止
- **解决**：检查循环条件是否会被改变，确保有退出机制

### Q3：函数返回值问题
- **症状**：函数似乎没有返回预期值
- **解决**：
  1. 检查是否使用了`return`语句
  2. 检查返回值是否被正确接收
  3. 使用print调试函数内部状态

### Q4：LeetCode环境不熟悉
- **解决**：
  1. 先阅读题目描述和示例
  2. 查看讨论区其他语言的解法思路
  3. 从暴力解法开始，不要追求最优解

### Q5：随机数生成问题
```python
# 正确导入和使用
import random
secret_number = random.randint(1, 100)
```

---

## 📝 学习效果自查清单

今日学习结束时，检查以下项目：

### 知识掌握
- [x] 能够正确编写if/elif/else条件判断
- [x] 掌握for循环遍历列表和range
- [x] 理解while循环与循环控制
- [x] 能够定义带参数的函数
- [x] 理解函数的返回值概念

### 技能应用
- [x] 完成全部6个必做练习
- [x] 实现猜数字游戏功能完整
- [x] 编写出正确的素数判断函数
- [x] 在LeetCode上提交"两数之和"代码
- [x] 理解每个练习的代码逻辑

### 习惯养成
- [x] 创建了第2天的代码目录
- [x] 更新了学习笔记
- [x] 注册了LeetCode账号
- [x] 记录了遇到的问题
- [x] 规划了明天学习重点

---

## 🎪 扩展资源（学有余力时使用）

1. **Python条件表达式进阶**：
   - 学习列表推导式中的条件过滤
   ```python
   # 示例：筛选偶数
   even_numbers = [x for x in range(10) if x % 2 == 0]
   ```

2. **循环技巧**：
   - `enumerate()`函数：同时获取索引和值
   - `zip()`函数：同时遍历多个列表

3. **LeetCode学习路线**：
   - LeetCode新手村：从简单题目开始
   - 推荐题目序列：1, 9, 13, 14, 20

4. **调试技巧**：
   - 使用`print()`语句调试
   - 分步测试函数功能

---

## 🔜 明日预告

**第3天学习重点**：
- 函数进阶：可变参数、关键字参数
- 递归函数概念
- 列表推导式
- 字符串常用方法
- LeetCode第9题：回文数

---

## 💪 鼓励的话

> "编程就像搭积木，条件、循环、函数是最基础的积木块。今天你学习了这三种重要的控制结构，这是编程思维的核心。当你能熟练组合这些积木时，就能构建出复杂的程序。LeetCode的'两数之和'是很多人的第一道算法题，完成它意味着你正式开始了算法学习之旅！"

**完成今日任务后**，请：

1. 在本文档顶部填写日期
2. 勾选学习效果自查清单
3. 更新TASKS_INDEX.md中的进度
4. 准备开始第3天的学习

---
**生成时间**：2026-03-17
**下次任务生成**：完成第2天学习后，请求生成第3天任务