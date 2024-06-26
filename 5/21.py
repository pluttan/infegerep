"""
Алгоритм получает на вход натуральное число N > 1 и строит
по нему новое число R следующим образом:

1) Если исходное число кратно 3, оно делится на 3, иначе из
   него вычитается 1.

2) Если полученное на предыдущем шаге число кратно 5, оно
   делится на 5, иначе из него вычитается 1.

3) Если полученное на предыдущем шаге число кратно 11, оно
   делится на 11, иначе из него вычитается 1.

4) Число, полученное на шаге 3, считается результатом
   работы алгоритма.

Сколько существует различных натуральных чисел N, при обработке
которых получится R = 8?
"""