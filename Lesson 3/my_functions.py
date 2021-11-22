def fibonacci(num):
    fib_row = [num, (num-1) + num]
    while len(fib_row) < 10:
        fib_num_1 = fib_row[-1]
        fib_num_2 = fib_row[-2]
        fib_row.append(fib_num_1 + fib_num_2)

    return list(fib_row)


print(fibonacci(1))


def max_two(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


print(max_two(2, 4, 9))


