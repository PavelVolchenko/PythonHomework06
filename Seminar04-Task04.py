""" Задана натуральная степень k. Сформировать случайным образом
    список коэффициентов (значения от 0 до 100) многочлена и записать
    в файл многочлен степени k.
    Пример:
        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0   """
from random import randint

k = int(input('Введите натуральную степень k: '))
poly = [str(randint(0, 100)) for i in range(k + 1)]
degree = [str(i) for i in range(k + 1)]
symbol_degree = lambda x: 'x^' if x > 1 else 'x' if 0 < x else '0'
symbol_degree = [symbol_degree(i) for i in range(k + 1)]
poly = list(map(list, zip(poly, symbol_degree[::-1], degree[::-1])))
poly = list(map(lambda x: ''.join(x).replace('0', '') if int(x[2]) <= 0
                else ''.join(x).removeprefix('0').removesuffix('1').replace('1x', 'x'), poly))
if not poly[-1]:
    poly.pop()[:-1]
result_poly = ' + '.join(poly) + ' = 0'
print(result_poly)
with open(f'poly.txt', 'w', encoding='utf-8') as file:
         file.write(result_poly)



