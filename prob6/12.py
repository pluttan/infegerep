"""
Исполнитель Редактор получает на вход строку символов 
и преобразовывает её. Редактор может выполнять две 
команды, в обеих командах v и w обозначают цепочки символов.

А) заменить (v, w).

    Эта команда заменяет в строке первое слева вхождение 
    цепочки v на цепочку w. Например, выполнение команды
        заменить (111, 27)
    преобразует строку 05111150 в строку 0527150.

    Если в строке нет вхождений цепочки v, то выполнение команды
        заменить (v, w)
    не меняет эту строку.

Б) нашлось (v).

    Эта команда проверяет, встречается ли цепочка v в строке 
    исполнителя Редактор. Если она встречается, то команда 
    возвращает логическое значение «истина», в противном случае 
    возвращает значение «ложь». Строка исполнителя при этом не 
    изменяется.

Цикл
  ПОКА условие
  последовательность команд
  КОНЕЦ ПОКА
выполняется, пока условие истинно.

В конструкции
  ЕСЛИ условие
    ТО команда1
    ИНАЧЕ команда2
  КОНЕЦ ЕСЛИ
выполняется команда1 (если условие истинно) или 
команда2 (если условие ложно).

Дана программа для Редактора:

НАЧАЛО
ПОКА нашлось (4444) ИЛИ нашлось (844) ИЛИ нашлось (84)
    ЕСЛИ нашлось (4444)
        ТО заменить (4444, 884)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (844)
        ТО заменить (844, 488)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (84)
        ТО заменить (84, 3343)
    КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ

На вход приведённой выше программе поступает строка, 
начинающаяся с цифры «8», а затем содержащая n цифр «4» 
(3<n<10000).

Определите такое наименьшее значение N, 
что для всех натуральных n⩾N количество цифр в строке, 
получающейся в результате выполнения программы, будет 
больше либо равно 20.
"""