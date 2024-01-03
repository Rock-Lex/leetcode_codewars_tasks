"""
Fibonacci
"""


def fib(fib_num):
    if fib_num == 1:
        return 0
    elif fib_num == 2:
        return 1
    else:
        fibonacci = fib(fib_num-1) + fib(fib_num-2)
        return fibonacci


if __name__ == "__main__":
    fib_num = 14
    print(fib(fib_num))