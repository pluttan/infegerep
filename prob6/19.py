"""
Два игрока, Петя и Ваня, играют в следующую игру. 
Перед игроками лежат две кучи камней. Игроки ходят по 
очереди, первый ход делает Петя. За один ход игрок может:

- увеличить количество камней в одной куче на количество 
  камней, которые находятся в другой куче
- уравнять количество камней в двух кучах, добавив 
  в меньшую столько камней, чтобы количество камней совпало. 
  Если в кучах уже одинаковое количество камней, то их 
  количество не меняется
  
Для того чтобы делать ходы, у каждого игрока есть 
неограниченное количество камней.

Игра завершается в тот момент, когда суммарное количество 
камней в кучах становится не менее 189. Победителем 
считается игрок, сделавший последний ход, т. е. первым 
получивший такую позицию, при которой в кучах будет 189 
или больше камней.

В начальный момент в первой куче было 5 камней, во 
второй куче — S камней; 1 ≤ S ≤ 183.

Будем говорить, что у игрока выигрышная стратегия, 
если он может выиграть при любых ходах противника.

Известно, что Ваня выиграл своим первым ходом после 
НЕУДАЧНОГО первого хода Пети. Укажите минимальное 
значение S, когда такая ситуация возможна.
"""