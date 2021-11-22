def fibonacci_func(num: int):
    if not isinstance(num, int):
        raise TypeError
    fib_row = [num, (num - 1) + num]
    if num in (0, 1):
        fib_row = [0, 1]
    while len(fib_row) < 10:
        fib_num_1 = fib_row[-1]
        fib_num_2 = fib_row[-2]
        fib_row.append(fib_num_1 + fib_num_2)

    return list(fib_row)


print(fibonacci_func(0))
# print(fibonacci_func(5))
# print(fibonacci_func(10))
# print(fibonacci_func("str"))


def max_two(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


print(max_two(2, 4, 9))
print(max_two(7, 12, 25))
print(max_two(45, 289, 400))
print(max_two(0, 0, 1))


