# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

list_1= list()
n = int(input("Введите количество элементов в первом множестве N: "))
for _ in range(n):
    list_1.append(int(input("Введите числа множества N: ")))

list_2= list()
m = int(input("Введите количество элементов во втором множестве M: "))
for _ in range(m):
    list_2.append(int(input("Введите числа множества M: ")))

list_1=set(list_1)
list_2=set(list_2)

finish_list = list_1.intersection(list_2)
print(finish_list)
