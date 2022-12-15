""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    Пример: - для k = 8 список будет выглядеть так:
            [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]                 """

n = int(input('Enter a number: '))
fib = lambda x: fib(x - 1) + fib(x - 2) if x > 2 else fib(x + 2) - fib(x + 1) if x < 1 else 1
result = [fib(i) for i in range(-n, n + 1)]
print(result)

# def fib(x):
#     if x in [1, 2]:
#         return 1
#     elif x <= 0:
#         return fib(x + 2) - fib(x + 1)
#     else:
#         return fib(x - 1) + fib(x - 2)
#
#
# n = int(input('Enter a number: '))
# lst = []
#
# for i in range(-n, n + 1):
#     lst.append(fib(i))
# print(lst)



