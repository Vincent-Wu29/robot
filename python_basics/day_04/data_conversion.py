# 数据转换处理

# ========== 字符串处理 ==========
text = "apple,banana,apple,orange,banana,grape"

# 1. 单词列表（去除重复）
word_list = list(set(text.split(",")))
print("1. 单词列表（去重）:", word_list)

# 2. 单词出现次数字典
word_count = {}
for word in text.split(","):
    word_count[word] = word_count.get(word, 0) + 1
print("2. 单词出现次数:", word_count)

# 3. 按单词长度分组
len_group = {}
for word in set(text.split(",")):
    length = len(word)
    if length not in len_group:
        len_group[length] = []
    len_group[length].append(word)
print("3. 按长度分组:", len_group)


# ========== 嵌套列表处理 ==========
nested = [[1, 2], [3, 4], [5, 6]]

# 1. 扁平列表
flat_list = []
for sub in nested:
    flat_list.extend(sub)
print("\n4. 扁平列表:", flat_list)

# 2. 转换为字典
dict_result = {}
for sub in nested:
    dict_result[sub[0]] = sub[1]
print("5. 转换字典:", dict_result)