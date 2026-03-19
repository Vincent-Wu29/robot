# 🤖 机器人软件工程师学习计划 - 第4天任务

**日期**：______2026.03.19_______
**学习阶段**：第一阶段 - 第1-2周（编程基础强化）
**预计学习时间**：4-5小时
**当前进度**：第4天 / 第1周

---

## 🎯 今日学习目标
1. 掌握Python四大核心数据结构：列表、元组、字典、集合
2. 熟练进行数据结构的增删改查操作
3. 理解不同数据结构的特点和应用场景
4. 学习数据结构之间的转换和组合
5. 完成LeetCode第13题：罗马数字转整数

---

## 📚 具体学习内容

### 1. 列表（List）深入学习（1小时）
**学习资源**：
- **廖雪峰Python教程**：https://www.liaoxuefeng.com/wiki/1016959663602400
  - 第2章：Python基础 → 使用list和tuple
- **Python官方Tutorial**：https://docs.python.org/3/tutorial/
  - 5.1. More on Lists

**重点掌握内容**：
- 列表的创建：`[]`、`list()`、列表推导式
- 基本操作：增(`append()`, `insert()`, `extend()`)、删(`remove()`, `pop()`, `del`)、改(索引赋值)、查(索引、切片)
- 列表方法：`sort()`, `reverse()`, `copy()`, `index()`, `count()`
- 列表切片：`list[start:end:step]`
- 列表与字符串的转换：`split()`, `join()`

**代码示例**：
```python
# 列表创建与基本操作
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')           # 增加
fruits.insert(1, 'grape')         # 插入
fruits.remove('banana')           # 删除
last_fruit = fruits.pop()         # 弹出最后一个

# 列表切片
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_three = numbers[:3]         # [0, 1, 2]
even_numbers = numbers[::2]       # [0, 2, 4, 6, 8]
reversed_numbers = numbers[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 列表方法
numbers.sort(reverse=True)        # 降序排序
numbers_copy = numbers.copy()     # 浅拷贝
count_3 = numbers.count(3)        # 计数
```

### 2. 元组（Tuple）与不可变性（30分钟）
**学习资源**：
- **廖雪峰Python教程**：
  - 第2章：Python基础 → 使用list和tuple
- **Python官方Tutorial**：
  - 5.3. Tuples and Sequences

**重点掌握内容**：
- 元组的创建：`()`、`tuple()`
- 元组的特点：不可变性、作为字典键、函数多返回值
- 元组与列表的异同
- 元组解包：`a, b, c = (1, 2, 3)`

**代码示例**：
```python
# 元组创建
point = (10, 20)
colors = ('red', 'green', 'blue')
single_tuple = (5,)  # 注意逗号，区别于(5)

# 元组解包
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

# 函数返回多个值
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
print(f"min={minimum}, max={maximum}")  # min=1, max=9

# 元组作为字典键
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
```

### 3. 字典（Dictionary）深入学习（1小时）
**学习资源**：
- **廖雪峰Python教程**：
  - 第2章：Python基础 → 使用dict和set
- **Python官方Tutorial**：
  - 5.5. Dictionaries

**重点掌握内容**：
- 字典的创建：`{}`、`dict()`
- 基本操作：增/改(`dict[key] = value`)、删(`del`, `pop()`)、查(`get()`, `in`)
- 字典方法：`keys()`, `values()`, `items()`, `update()`, `setdefault()`
- 字典推导式：`{key: value for item in iterable}`
- 字典视图对象的特点

**代码示例**：
```python
# 字典创建与操作
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# 增加/修改
student["grade"] = "A"           # 增加
student["age"] = 21              # 修改

# 查询与删除
name = student.get("name")       # 安全获取
if "major" in student:           # 检查键是否存在
    del student["major"]         # 删除
email = student.pop("email", "No email")  # 安全弹出

# 遍历字典
for key, value in student.items():
    print(f"{key}: {value}")

# 字典推导式
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 4. 集合（Set）与集合运算（30分钟）
**学习资源**：
- **廖雪峰Python教程**：
  - 第2章：Python基础 → 使用dict和set
- **Python官方Tutorial**：
  - 5.4. Sets

**重点掌握内容**：
- 集合的创建：`{}`、`set()`（注意空集合用`set()`）
- 集合的特点：无序、不重复、元素必须可哈希
- 集合运算：并集(`union()`或`|`)、交集(`intersection()`或`&`)、差集(`difference()`或`-`)、对称差集(`symmetric_difference()`或`^`)
- 集合方法：`add()`, `remove()`, `discard()`, `pop()`

**代码示例**：
```python
# 集合创建
fruits = {"apple", "banana", "cherry"}
numbers = set([1, 2, 3, 4, 5])

# 集合运算
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2           # 并集: {1, 2, 3, 4, 5, 6, 7, 8}
intersection_set = set1 & set2    # 交集: {4, 5}
difference_set = set1 - set2      # 差集: {1, 2, 3}
symmetric_diff = set1 ^ set2      # 对称差集: {1, 2, 3, 6, 7, 8}

# 集合方法
fruits.add("orange")              # 添加
fruits.remove("banana")           # 删除（不存在会报错）
fruits.discard("grape")           # 安全删除（不存在不报错）
```

### 5. 数据结构综合应用（1小时）
**重点掌握内容**：
- 列表、元组、字典、集合的嵌套使用
- 数据结构的相互转换
- 选择合适数据结构的原则
- 实际应用场景分析

**代码示例**：
```python
# 嵌套数据结构
students = [
    {"name": "Alice", "scores": (85, 90, 88), "courses": {"Math", "Physics"}},
    {"name": "Bob", "scores": (78, 92, 85), "courses": {"Chemistry", "Biology"}},
    {"name": "Charlie", "scores": (95, 88, 91), "courses": {"Math", "Computer Science"}}
]

# 数据转换
names = [student["name"] for student in students]  # 列表推导式提取名字
name_set = set(names)                              # 转换为集合去重
name_dict = {name: i for i, name in enumerate(names)}  # 字典推导式

# 复杂数据处理
# 找出所有选修Math的学生
math_students = [s["name"] for s in students if "Math" in s["courses"]]
print(f"Math students: {math_students}")  # ['Alice', 'Charlie']
```

### 6. LeetCode第13题：罗马数字转整数（1小时）
**题目信息**：
- **题目**：13. 罗马数字转整数（Roman to Integer）
- **难度**：简单
- **链接**：https://leetcode.com/problems/roman-to-integer/
- **中文链接**：https://leetcode.cn/problems/roman-to-integer/

**题目描述**：
罗马数字包含以下七种字符: I, V, X, L, C, D 和 M。
```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
例如，罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做 XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
- I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
- X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
- C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

**示例**：
```
输入: "III"
输出: 3

输入: "IV"
输出: 4

输入: "IX"
输出: 9

输入: "LVIII"
输出: 58
解释: L = 50, V = 5, III = 3.

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

**解题思路引导**：
1. 创建罗马数字到整数的映射字典
2. 遍历字符串，比较当前字符与下一个字符的值
3. 如果当前字符值小于下一个字符值，则减去当前值（如IV中的I）
4. 否则，加上当前值
5. 注意处理最后一个字符

---

## 💻 编程练习题目

### 必做练习（完成所有6题）

**练习1：列表操作综合练习**
```python
# 要求：
# 1. 创建包含10个随机整数的列表（1-100）
# 2. 对列表进行排序（升序和降序）
# 3. 找出列表中的最大值、最小值、平均值
# 4. 将列表拆分为前半部分和后半部分
# 5. 在列表中间插入三个新元素
# 6. 删除所有偶数元素
# 提示：使用random模块生成随机数
```

**练习2：学生成绩管理系统（字典应用）**

```python
# 要求：编写程序管理学生成绩
# 1. 使用字典存储学生信息：{学号: {姓名: "", 成绩: []}}
# 2. 实现功能：
#    - 添加学生
#    - 删除学生
#    - 查询学生信息
#    - 添加成绩
#    - 计算每个学生的平均分
#    - 找出平均分最高的学生
# 3. 使用菜单驱动界面
```

**练习3：集合运算应用**
```python
# 要求：
# 1. 创建两个课程集合：数学课学生和物理课学生
# 2. 找出：
#    - 同时选修两门课的学生（交集）
#    - 只选修一门课的学生（对称差集）
#    - 所有选修课的学生（并集）
#    - 从数学课转去物理课的学生（差集）
# 3. 输出结果并统计人数
```

**练习4：数据转换与处理**
```python
# 要求：
# 1. 将字符串 "apple,banana,apple,orange,banana,grape" 转换为：
#    - 单词列表（去除重复）
#    - 单词出现次数字典
#    - 按单词长度分组的字典
# 2. 将嵌套列表 [[1, 2], [3, 4], [5, 6]] 转换为：
#    - 扁平列表 [1, 2, 3, 4, 5, 6]
#    - 字典 {1: 2, 3: 4, 5: 6}
```

**练习5：元组与函数返回值**
```python
# 要求：
# 1. 编写函数analyze_numbers(numbers)，接收数字列表
# 2. 返回一个元组包含：(最小值, 最大值, 平均值, 中位数, 众数)
# 3. 在主函数中调用并解包返回值
# 4. 使用元组解包分别获取各个统计值
```

**练习6：LeetCode罗马数字转整数**
```python
# 要求：在LeetCode上完成"罗马数字转整数"题目
# 1. 使用字典映射罗马数字到整数
# 2. 实现两种解法：从左到右遍历和从右到左遍历
# 3. 提交代码并通过所有测试用例
# 4. 分析两种解法的时间复杂度和空间复杂度
```

### 挑战练习（可选）
```python
# 图书馆管理系统（综合应用）
# 要求：
# 1. 使用字典存储图书信息：{书号: {书名: "", 作者: "", 借阅状态: True/False}}
# 2. 使用集合存储已借阅图书的书号
# 3. 使用列表存储借阅记录[(书号, 借阅时间, 归还时间)]
# 4. 实现功能：
#    - 添加新书
#    - 借阅图书
#    - 归还图书
#    - 查询图书信息
#    - 统计借阅次数最多的图书
# 5. 使用函数封装每个功能
```

---

## ⏰ 时间分配建议

| 时间段 | 活动 | 时长 | 具体任务 |
|--------|------|------|----------|
| **上午/开始** | 列表深入学习 | 60分钟 | 学习列表操作，完成练习1 |
| | 元组学习 | 30分钟 | 理解元组特点，结合练习5 |
| **中午/休息后** | 字典深入学习 | 60分钟 | 掌握字典方法，完成练习2 |
| | 集合学习 | 30分钟 | 学习集合运算，完成练习3 |
| **下午/晚上** | 数据结构综合 | 60分钟 | 学习嵌套结构，完成练习4 |
| | LeetCode解题 | 60分钟 | 理解题目，完成练习6 |
| | 挑战练习 | 60分钟 | 尝试综合应用，整理代码 |
| **总结整理** | 复习总结 | 30分钟 | 整理学习笔记，准备明天学习 |

**高效学习建议**：
1. 每种数据结构都要动手创建、操作、遍历
2. 理解不同数据结构的适用场景
3. 多使用字典推导式、列表推导式
4. LeetCode题目先画图理清思路

---

## 📦 预期产出物

### 1. 代码文件
在`c:\learn\robot\python_basics\day_04\`目录下创建以下文件：
```
python_basics/day_04/
├── list_operations.py          # 练习1
├── student_grade_system.py     # 练习2
├── set_operations.py           # 练习3
├── data_conversion.py          # 练习4
├── tuple_statistics.py         # 练习5
└── library_management.py       # 挑战练习
```
在`c:\learn\robot\leetcode\`目录下更新：
```
leetcode/
├── two_sum.py                  # 第2天题目
├── palindrome_number.py        # 第3天题目
└── roman_to_integer.py         # 第4天题目
```

### 2. 学习笔记
在`c:\learn\robot\learning_notes\`目录下更新：
```
learning_notes/
├── day_01_notes.md             # 第1天笔记
├── day_02_notes.md             # 第2天笔记
├── day_03_notes.md             # 第3天笔记
└── day_04_notes.md             # 第4天笔记
```
**第4天笔记内容应包括**：
- 四种数据结构的核心特点对比
- 常用操作和方法记忆技巧
- 数据结构选择原则（何时用列表vs字典vs集合）
- 嵌套数据结构的访问和处理
- LeetCode罗马数字解题思路
- 遇到的问题及解决方案

### 3. LeetCode进展
- [ ] 完成"罗马数字转整数"题目
- [ ] 实现至少两种解法
- [ ] 理解字典在算法中的应用
- [ ] 提交代码并通过测试

---

## 🔍 常见问题与解决方案

### Q1：列表修改时索引错误
- **症状**：IndexError: list index out of range
- **解决**：
  1. 使用`len(list)`检查列表长度
  2. 避免在遍历列表时修改列表（可以创建副本）
  3. 使用`enumerate()`同时获取索引和值

### Q2：字典键不存在错误
- **症状**：KeyError: 'key_name'
- **解决**：
  1. 使用`dict.get(key, default)`安全获取
  2. 使用`key in dict`检查键是否存在
  3. 使用`dict.setdefault(key, default)`设置默认值

### Q3：集合与列表混淆
- **解决**：
  - 列表：有序、可重复、用`[]`
  - 集合：无序、不重复、用`{}`或`set()`
  - 空集合必须用`set()`，`{}`是空字典

### Q4：元组"不可变"的理解
- **症状**：尝试修改元组元素时报错
- **解决**：
  - 元组本身不可变，但元组内的可变对象（如列表）可以修改
  ```python
  t = ([1, 2], 3)
  t[0].append(3)  # 可以，修改的是元组内的列表
  t[0] = [4, 5]   # 错误，不能修改元组元素
  ```

### Q5：罗马数字转换思路
- **提示**：
  1. 建立映射字典：`{'I': 1, 'V': 5, ...}`
  2. 遍历字符串，比较当前字符与下一个字符
  3. 注意处理边界条件（最后一个字符）

---

## 📝 学习效果自查清单

今日学习结束时，检查以下项目：

### 知识掌握
- [x] 能够熟练进行列表的增删改查操作
- [x] 理解元组的不可变性和适用场景
- [x] 掌握字典的常用方法和遍历方式
- [x] 理解集合运算（并交差对称差）
- [x] 能够选择合适的数据结构解决问题
- [x] 理解LeetCode罗马数字转换算法

### 技能应用
- [x] 完成全部6个必做练习
- [x] 实现学生成绩管理系统
- [x] 正确使用集合运算解决实际问题
- [x] 在LeetCode上提交"罗马数字转整数"代码
- [x] 理解每种数据结构的应用场景

### 习惯养成
- [x] 创建了第4天的代码目录
- [x] 更新了学习笔记
- [x] 整理了数据结构对比表
- [x] 记录了选择数据结构的思考过程
- [x] 规划了明天学习重点

---

## 🎪 扩展资源（学有余力时使用）

1. **collections模块**：
   - `defaultdict`：带默认值的字典
   - `Counter`：计数器，统计元素出现次数
   - `deque`：双端队列，高效的头尾操作

2. **数据结构性能对比**：
   - 列表：随机访问O(1)，插入/删除O(n)
   - 字典：查找/插入/删除平均O(1)
   - 集合：成员测试O(1)
   - 根据操作需求选择合适的数据结构

3. **深拷贝与浅拷贝**：
   - 浅拷贝：`copy()`，只复制一层
   - 深拷贝：`copy.deepcopy()`，递归复制所有层
   - 对于嵌套数据结构要注意拷贝方式

4. **LeetCode学习**：
   - 学习第14题：最长公共前缀
   - 巩固字符串和列表操作
   - 练习简单算法思维

---

## 🔜 明日预告

**第5天学习重点**：
- 文件操作：读写文本文件、CSV文件
- 异常处理：try/except/else/finally
- 模块与包：导入自定义模块
- 综合项目：学生信息管理系统

---

## 💪 鼓励的话

> "数据结构是程序的骨架，算法是程序的灵魂。今天你学习了Python四大核心数据结构，这是构建复杂程序的基础。列表、元组、字典、集合各有其用，就像工具箱里的不同工具，选择合适的工具能让编程事半功倍。LeetCode的罗马数字转换问题让你练习了字典的应用和算法的思考，这正是实际工作中常见的问题类型。"

**完成今日任务后**，请：
1. 在本文档顶部填写日期
2. 勾选学习效果自查清单
3. 更新TASKS_INDEX.md中的进度
4. 准备开始第5天的学习

---
**生成时间**：2026-03-18
**下次任务生成**：完成第4天学习后，请求生成第5天任务