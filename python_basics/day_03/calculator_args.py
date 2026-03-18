def calculate(operation, *args):
    result = 0
    match operation:
        case "sum":
            for x in args:
                result += x
        case "product":
            result = 1
            for x in args:
                result *= x
        case "average":
            for x in args:
                result += x
            result = result / len(args)
    
    return result

print(calculate("sum", 1, 2, 3, 4))
print(calculate("product", 2, 3, 4))
print(calculate("average", 10, 20, 30))
