"""
По каналу связи передаются шифрованные сообщения, содержащие
только 10 букв: А, Б, Е, И, К, Л, Р, С, Т, У; для передачи
используется неравномерный двоичный код. Для девяти букв
слова известны.

А --   11,
Б -- 0011,
Е --    ?,
И --  100,
К -- 0100,
Л -- 0010,
Р -- 0101,
С -- 0001,
Т -- 0000,
У --  011.

Укажите кратчайшее кодовое слово для буквы Е, при котором
код будет удовлетворять условию Фано. Если таких кодов несколько,
укажите код с наибольшим числовым значением.

Примечание: Условие Фано означает, что никакое кодовое слово не
является началом другого кодового слова.
"""