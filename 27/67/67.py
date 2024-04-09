"""
Набор данных представляет собой последовательность натуральных чисел.

Необходимо выбрать такую подпоследовательность подряд идущих чисел,
чтобы их сумма была максимальной и делилась на 1000.
В ответе укажите её сумму.

Гарантируется, что такая подпоследовательность существует.

Входные данные.

Даны два входных файла,
каждый из которых содержит в первой строке количество чисел
N (2 ≤ N ≤ 10⁸).
Каждая из следующих N строк содержит натуральное число,
не превышающее 10000.

Пример входного файла:
6
997
3
4
12
88
1900

В этом наборе можно выбрать последовательности 997+3 (сумма 1000)
и 12+88+1900 (сумма 2000).
Наибольшую сумму имеет вторая из этих последовательностей.
Ответ: 2000

В ответе укажите два числа:
сначала искомое значение для файла А,
затем для файла B.
"""