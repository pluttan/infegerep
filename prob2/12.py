"""
Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают
цепочки цифр.

А) заменить (v, w).
    Эта команда заменяет в строке первое слева вхождение цепочки v
    на цепочку w. Например, выполнение команды заменить (111, 27) преобразует
    строку 05111150 в строку 0527150. Если в строке нет вхождений цепочки v,
    то выполнение команды заменить (v, w) не меняет эту строку.
Б) нашлось (v).
    Эта команда проверяет, встречается ли цепочка v в строке исполнителя
    Редактор. Если она встречается, то команда возвращает логическое
    значение «истина», в противном случае возвращает значение «ложь».
    Строка исполнителя при этом не изменяется.

Какая строка получится в результате применения приведённой ниже
программы к строке, состоящей из 100 идущих подряд
цифр 9? В ответе запишите полученную строку.

НАЧАЛО
ПОКА нашлось (33333) ИЛИ нашлось (999)
  ЕСЛИ нашлось (33333)
    ТО заменить (33333, 99)
    ИНАЧЕ заменить (999, 3)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
"""
