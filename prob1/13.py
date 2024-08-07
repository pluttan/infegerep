"""
В терминологии сетей TCP/IP маска сети – это двоичное число,
меньшее 2³²; в маске сначала (в старших разрядах) стоят единицы,
а затем с некоторого места нули. Маска определяет, какая часть
IP-адреса узла сети относится к адресу сети, а какая – к адресу
самого узла в этой сети.

Обычно маска записывается по тем же правилам, что и IP-адрес –
в виде четырёх байт, причём каждый байт записывается в виде
десятичного числа. Адрес сети получается в результате применения
поразрядной конъюнкции к заданному IP-адресу узла и маске.

Например, если IP-адрес узла равен 131.32.255.131, а маска равна
255.255.240.0, то адрес сети равен 131.32.240.0.

Для узла с IP-адресом 192.75.64.98 адрес сети равен 192.75.64.0.
Найдите наименьшее возможное количество единиц в двоичной записи
маски подсети.
"""
