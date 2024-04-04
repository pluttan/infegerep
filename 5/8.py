"""
На вход алгоритма подаётся натуральное число N. Алгоритм строит
по нему новое число R следующим образом.

1) Строится двоичная запись числа 2N.

2) К этой записи дописываются справа ещё два разряда по следующему
   правилу:

   а) складываются все цифры двоичной записи числа 2N, и остаток
      от деления суммы на 2 дописывается в конец числа (справа).
      Например, запись 10000 преобразуется в запись 100001;

   б) над этой записью производятся те же действия – справа
      дописывается остаток от деления суммы её цифр на 2.

Полученная таким образом запись (в ней на три разряда больше,
чем в записи исходного числа N) является двоичной записью искомого
числа R. Укажите такое наименьшее число N, для которого результат
работы данного алгоритма больше числа 1017. В ответе это число
запишите в десятичной системе счисления.
"""
