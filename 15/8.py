"""
Введём выражение M&K, обозначающее поразрядную конъюнкцию M и K
(логическое «И» между соответствующими битами двоичной записи).
Определите наименьшее натуральное число A, такое что выражение

(X & 107 = 0) → ((X & 55 ≠ 0) → (X & A ≠ 0))

тождественно истинно (то есть принимает значение 1 при любом
натуральном значении переменной X)?
"""
