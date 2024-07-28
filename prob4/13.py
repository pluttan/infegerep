"""
В терминологии сетей TCP/IP маской сети называется двоичное число,
которое показывает, какая часть IP-адреса узла сети относится к
адресу сети, а какая — к адресу самого узла в этой сети. Обычно
маска записывается по тем же правилам, что и IP-адрес, — в виде
четырёх байтов, причём каждый байт записывается в виде десятичного
числа. Сначала, в старших разрядах маски стоят единицы, а затем, с
некоторого разряда — нули. Адрес сети получается в результате
применения поразрядной конъюнкции к заданным IP-адресу узла и маске.

Например, если IP-адрес узла равен 77.88.55.242, а маска равна
255.255.255.240, то адрес сети равен 77.88.55.240.

Для узла с IP-адресом 20.24.110.42 адрес сети равен 20.24.96.0.
Каково наименьшее возможное количество единиц в разрядах маски?
"""
