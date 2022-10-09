x, y = map(int, input('Введите координаты точки через пробел: ').split())
if x == 0 and y == 0:
    print('Начало координат')
elif x == 0:
    print('На оси абцисс')
elif y == 0:
    print('На оси ординат')
elif x > 0 and y > 0:
    print('1-ая четверть')
elif x < 0 and y > 0:
    print('2-ая четверть')
elif x < 0 and y < 0:
    print('3-ая четверть')
else:
    print('4-ая четверть')
