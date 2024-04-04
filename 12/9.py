"""
Исполнитель Редактор получает на вход строку цифр и
преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки символов.

1. заменить (v, w)
2. нашлось (v)

Первая команда заменяет в строке первое слева вхождение
цепочки v на цепочку w. Если цепочки v в строке нет, эта
команда не изменяет строку. Вторая команда проверяет,
встречается ли цепочка v в строке исполнителя Редактор.

Дана программа для исполнителя Редактор:

НАЧАЛО
    ПОКА нашлось(999) ИЛИ нашлось(22)
       ЕСЛИ нашлось(999)
          ТО заменить(999, 12)
          ИНАЧЕ заменить(22, 1)
       КОНЕЦ ЕСЛИ
    КОНЕЦ ПОКА
КОНЕЦ
Какое наибольшее количество единиц получится в результате
применения приведённой программы к строке, состоящей из
100 цифр 9, 14 цифр 1, 48 цифр 2, идущих в произвольном порядке?
В ответе запишите количество единиц в полученной строке.
"""
