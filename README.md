# Ближайшие бары

Пргамма находит самый большой, самый маленький, и ближай к вам бар.

# Как запустить

Для того чтобы найти ближайший к вам бар нужно зайти на сайт [Yandex Location Tool](https://yandex.ru/map-constructor/location-tool/), найти свой адрес (или разрешить получать геолокацию сайту) и получить координаты (в формате: широта-долгота).

Есть три функции: 
+ get_biggest_bar - выводит самый большой бар
+ get_smallest_bar - выводит самый маленький бар
+ get_closest_bar - выводит ближайший бар

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

python bars.py get_closest_bar <latitude> <longitude> # possibly requires call of python3 executive 
Name of bar: Бар
Address: Ленинский проспект, дом 158 instead of just python

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
