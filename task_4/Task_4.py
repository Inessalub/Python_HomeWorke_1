# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa = int(input('Введите координату x первой точки: '))
ya = int(input('Введите координату y первой точки: '))
xb = int(input('Введите координату x второй точки: '))
yb = int(input('Введите координату y второй точки: '))
ac = ya-yb
bc = xa-xb
print(round((ac ** 2 + bc ** 2) ** 0.5,2))
