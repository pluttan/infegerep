"""
Полина хранит на компьютере картинки и видео, объёмы которых
различны. Она хочет сохранить часть из них на флэш-накопитель, объём
которого равен M, следующим образом:

1) Сначала она сохраняет самые маленькие видеозаписи до тех пор, пока они
   не займут не менее чем половину от общей памяти.

2) В оставшееся место Полина сохраняет как можно больше картинок, стремясь
   занять весь оставшийся объём.

Определите сначала, сколько свободного места останется на флеш-носителе,
затем общее количество элементов, которое в итоге удалось поместить.

Входные данные. В первой строке входного файла находятся два
числа: N - количество всех изображений и видео, M - объём
флеш-накопителя. N, M - натуральные числа, не превышающие 10^6.
В следующих N строках находятся значения объёмов картинок и видео
соответственно, эти объёмы указаны в Кбайтах. Каждая картинка
весит не более 100 Кбайт, видео - не менее 101 Кбайт. Запишите
в ответе два числа: сначала объём оставшегося свободного места,
затем общее количество картинок и видео, которые могут быть сохранены.

Пример входного файла:

8  150
20
101
15
400
5
900
10
9

При таких исходных данных можно сохранить 4 картинки (20+15+5+9 = 49)
и 1 видео объёмом 101, имеем: 150 - (49 + 101) = 0;
4 + 1 = 5 - элементов максимум можно сохранить.
Ответ: 0 5.
"""
