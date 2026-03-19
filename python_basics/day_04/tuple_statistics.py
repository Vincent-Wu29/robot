def analyze_numbers(numbers):
    """分析数字列表，返回统计元组"""
    if not numbers:
        return None
    
    # 排序用于计算中位数
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    # 最小值、最大值、平均值
    min_val = min(numbers)
    max_val = max(numbers)
    avg = sum(numbers) / n
    
    # 中位数
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        median = sorted_nums[mid]
    
    # 众数（出现次数最多的数）
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    mode = max(count, key=count.get)
    
    return (min_val, max_val, avg, median, mode)


def main():
    # 测试数据
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"数据: {numbers}")
    
    # 调用函数并解包返回值
    min_val, max_val, avg, median, mode = analyze_numbers(numbers)
    
    # 输出结果
    print(f"最小值: {min_val}")
    print(f"最大值: {max_val}")
    print(f"平均值: {avg:.2f}")
    print(f"中位数: {median}")
    print(f"众数: {mode}")


# 运行
main()