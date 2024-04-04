"""
Исполнитель Чертёжник перемещается на координатной плоскости,
оставляя след в виде линии. Чертёжник может выполнять команду
Сместиться на (a,b) (где a, b — целые числа), перемещающую
Чертёжника из точки с координатами (x, y) в точку с
координатами (x+a, y+b). Если числа a, b положительные,
то значение соответствующей координаты увеличивается, если
отрицательные — уменьшается. Например, если Чертёжник находится
в точке с координатами (4, 2), то команда Сместиться на (2,-3)
переместит Чертёжника в точку (6,-1). Запись

Повтори k раз
    Команды
конец

означает, что последовательность Команд повторится k раз.
Чертёжнику был дан для исполнения следующий алгоритм:

Повтори 5 раз
    Сместиться на (6,8)
    Сместиться на (-8,4)
    Сместиться на (2,-12)
конец

Определите, периметр фигуры, которая будет получена в результате
выполнения данного алгоритма. В ответе укажите только целую часть
полученного значения.
"""
