"""
Автомат обрабатывает натуральное число N по следующему алгоритму:

1. Строится двоичная запись числа N.
2. Складываются все цифры полученной двоичной записи.
   В конец записи (справа) дописывается остаток от деления полученной
   суммы на 2.
3. Предыдущий пункт повторяется для записи с добавленной цифрой.
4. Результат переводится в десятичную систему и выводится на экран.

Сколько различных чисел, меньших 80, могут появиться на экране в
результате работы автомата?
"""
