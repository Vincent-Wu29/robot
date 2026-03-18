def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"移动 盘子1 从 {source} 到 {target}")
        return

    hanoi(n - 1, source, auxiliary, target)

    print(f"移动 盘子{n} 从 {source} 到 {target}")

    hanoi(n - 1, auxiliary, target , source)

hanoi(5, 'A', 'C', 'B')