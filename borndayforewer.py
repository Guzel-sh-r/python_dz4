"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def func_question(question, right_answer):
    answer = input(question)
    while answer != right_answer:
        print("Не верно")
        answer = input(question)

func_question('Ввведите год рождения А.С.Пушкина: ', '1799')
func_question('Ввведите день рождения Пушкина: ', '6')
print('Верно')
