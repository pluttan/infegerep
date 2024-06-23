"""
Пусть S — последовательность из N целых чисел, пронумерованных подряд
начиная с 1. Обозначим S(L, R) подпоследовательность, состоящую из
идущих подряд элементов, входящих в S, начиная с элемента с номером L
и заканчивая элементом с номером R.

Требуется найти такие значения номеров элементов L, M, R,
где 0 < L < M < R-1 (т. е. между элементами с номерами M и R есть ещё
как минимум один элемент), чтобы разность суммы элементов
подпоследовательноcти S(M+1, R) и суммы элементов подпоследовательности
S(L, М) была максимальна.
В ответе укажите максимальное значение разности подобных сумм.

Входные данные
Дано два входных файла (файл А и файл В), каждый из которых в первой
строке содержит число N (5 < N < 10 000 000) - количество целых чисел.
Каждая из следующих N строк содержит одно целое число, значение которого
по модулю не превышает 1000.

В ответе укажите два числа: сначала значение искомой величины
для файла A, затем — для файла В.

Типовой пример организации данных во входном файле
7
20
4
-2
13
-1
2
-10

При таких входных данных L=2, M=3, R=6. Искомая максимальная
разность равна (13 + (-1) + 2) - (4 + (-2)) = 12.
Подпоследовательность "2 13 -1" разбить на две подпоследовательности
требуемого вида невозможно.
Ответом является число 12.

Типовой пример имеет иллюстративный характер. Для выполнения задания
используйте данные из прилагаемых файлов.
Предупреждение: для обработки файла В не следует использовать переборный
алгоритм, вычисляющий разность для всех возможных вариантов, поскольку
написанная по такому алгоритму программа будет выполняться слишком долго.
"""