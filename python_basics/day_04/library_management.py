import datetime

# 数据存储
books = {}           # {书号: {书名: "", 作者: "", 借阅状态: True/False}}
borrowed_set = set() # 已借阅图书的书号
records = []         # [(书号, 借阅时间, 归还时间)]


def add_book():
    """添加新书"""
    book_id = input("请输入书号: ").strip()
    if book_id in books:
        print("❌ 该书号已存在！")
        return
    
    name = input("请输入书名: ").strip()
    author = input("请输入作者: ").strip()
    
    books[book_id] = {
        "书名": name,
        "作者": author,
        "借阅状态": False  # False=未借出, True=已借出
    }
    print(f"✅ 图书《{name}》添加成功！")


def borrow_book():
    """借阅图书"""
    book_id = input("请输入书号: ").strip()
    
    if book_id not in books:
        print("❌ 图书不存在！")
        return
    
    if books[book_id]["借阅状态"]:
        print("❌ 该书已被借出！")
        return
    
    # 更新状态
    books[book_id]["借阅状态"] = True
    borrowed_set.add(book_id)
    
    # 添加借阅记录（归还时间为空）
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    records.append((book_id, now, None))
    print(f"✅ 成功借阅《{books[book_id]['书名']}》，借阅时间: {now}")


def return_book():
    """归还图书"""
    book_id = input("请输入书号: ").strip()
    
    if book_id not in books:
        print("❌ 图书不存在！")
        return
    
    if not books[book_id]["借阅状态"]:
        print("❌ 该书未被借出！")
        return
    
    # 更新状态
    books[book_id]["借阅状态"] = False
    borrowed_set.discard(book_id)
    
    # 更新借阅记录
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    for i, (bid, borrow_time, return_time) in enumerate(records):
        if bid == book_id and return_time is None:
            records[i] = (bid, borrow_time, now)
            break
    
    print(f"✅ 成功归还《{books[book_id]['书名']}》，归还时间: {now}")


def query_book():
    """查询图书信息"""
    book_id = input("请输入书号: ").strip()
    
    if book_id not in books:
        print("❌ 图书不存在！")
        return
    
    info = books[book_id]
    status = "已借出" if info["借阅状态"] else "可借阅"
    print(f"\n书号: {book_id}")
    print(f"书名: {info['书名']}")
    print(f"作者: {info['作者']}")
    print(f"状态: {status}")


def show_borrowed():
    """显示已借阅图书"""
    if not borrowed_set:
        print("当前没有借出的图书")
        return
    
    print("\n📚 已借阅图书列表:")
    for book_id in borrowed_set:
        info = books[book_id]
        print(f"  {book_id} - 《{info['书名']}》by {info['作者']}")


def most_borrowed():
    """统计借阅次数最多的图书"""
    if not records:
        print("暂无借阅记录")
        return
    
    # 统计每本书的借阅次数
    count = {}
    for book_id, _, _ in records:
        count[book_id] = count.get(book_id, 0) + 1
    
    # 找出最大值
    max_count = max(count.values())
    most_books = [bid for bid, c in count.items() if c == max_count]
    
    print(f"\n🏆 借阅次数最多的图书（{max_count}次）:")
    for bid in most_books:
        print(f"  {bid} - 《{books[bid]['书名']}》")


def show_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("      📖 图书馆管理系统")
    print("=" * 40)
    print("  1. 添加新书")
    print("  2. 借阅图书")
    print("  3. 归还图书")
    print("  4. 查询图书信息")
    print("  5. 显示已借阅图书")
    print("  6. 统计最热门图书")
    print("  0. 退出")
    print("=" * 40)


def main():
    """主函数"""
    while True:
        show_menu()
        choice = input("请选择: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            query_book()
        elif choice == "5":
            show_borrowed()
        elif choice == "6":
            most_borrowed()
        elif choice == "0":
            print("👋 再见！")
            break
        else:
            print("❌ 无效选择！")


# 预置一些测试数据
books["001"] = {"书名": "Python编程", "作者": "张三", "借阅状态": False}
books["002"] = {"书名": "数据结构", "作者": "李四", "借阅状态": False}
books["003"] = {"书名": "算法导论", "作者": "王五", "借阅状态": False}

if __name__ == "__main__":
    main()