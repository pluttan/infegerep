"""
Алгоритм вычисления функции F(n), где n – целое число, задан
следующими соотношениями:

F(n) = n,           при n >= 10 000,
F(n) = n + F(n/3),  при n <  10 000 и делится на 3,
F(n) = 2n + F(n+3), при n <  10 000 и не делится на 3.

Определите значение F(999)−F(46).
"""
