""" В текстовом файле посчитать количество строк, а также для каждой
    отдельной строки определить количество в ней символов и слов."""

file = open('file.txt', 'r', encoding='UTF-8')
data = file.read().split('\n')
out = list(enumerate(map(lambda x: x + " -> In " + str(len(x.split())) + " words " + str(len(x)) + " symbols", data)))
print(f"Количество строк в файле {file.name} -> {out[-1][0] + 1}")
for i in out:
    print(str(i[0] + 1) + '. ' + i[1])
file.close()


# for s in file.readlines():
#     print(s, end='')
#     print(f'Количество символов = {len(s)}')
#     print(f"Количество слов = {len(s.split())}")
#     print()



