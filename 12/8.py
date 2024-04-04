"""
Исполнитель Редактор получает на вход строку цифр и
преобразовывает её. Редактор может выполнять две команды,
в обеих командах v и w обозначают цепочки символов.

заменить (v, w)
нашлось (v)

Первая команда заменяет в строке первое слева вхождение
цепочки v на цепочку w. Если цепочки v в строке нет, эта
команда не изменяет строку. Вторая команда проверяет,
встречается ли цепочка v в строке исполнителя Редактор.

Дана программа для Редактора:

НАЧАЛО
    ПОКА нашлось(11)
       ЕСЛИ нашлось(112)
          ТО заменить(112, 7)
          ИНАЧЕ заменить(11,3)
       КОНЕЦ ЕСЛИ
    КОНЕЦ ПОКА
КОНЕЦ

Исходная строка содержит 12 единиц и 4 двойки, других
цифр нет, точный порядок расположения цифр неизвестен.
Какую наибольшую сумму цифр может иметь строка,
которая получится после выполнения программы?
"""
