# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет



n = int(input('Введите цифру, обозначающую день недели, чтобы проверить является ли этот день выходным: '))
if n == 6 or n == 7:
    print('Да')
elif 0 < n < 6:
    print('Нет')
else:
    print('Ошибка')