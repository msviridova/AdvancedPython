import functools
from datetime import datetime, timedelta

'''1. Написать декоратор, который будет печатать на экран время работы функции (пользуемся datetime)'''


def func_time_decorator(func):
    def wrapper():
        start_time = datetime.now()
        func()
        print(datetime.now() - start_time)
    return wrapper()


@func_time_decorator
def first_function():
    print("Эта функция совершенно ничего не делает, кроме того, что пишет эти несколько слов")


'''2. Написать функцию для вычислений ряда чисел Фибоначчи (можно через цикл, можно через рекурсию).'''


def fibonacci(num):
    fib_row = [num, (num-1) + num]
    while len(fib_row) < 10:
        fib_num_1 = fib_row[-1]
        fib_num_2 = fib_row[-2]
        fib_row.append(fib_num_1 + fib_num_2)

    print(*fib_row, sep=", ")


print(fibonacci(0))


'''Реализовать функцию, которая принимает три позиционных аргумента и возвращает сумму наибольших двух из них 
(если вы решили сравнивать все 3 числа между собой вручную - это очень плохая идея 🙂 )'''


def max_two(a, b, c):
    return sum([a, b, c]) - min(a, b, c)


print(max_two(2, 4, 9))


