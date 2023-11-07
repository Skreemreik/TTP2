import random
import itertools


def filter_values(in_array,target):
    if in_array <= target:
       return True
    else:
       return False


def array_input():
    array_text = input("Введите массив чисел, разделенных пробелом: ").split()
    array = [int(num) for num in array_text]
    return array


def array_random():
    while True:
        try:
            size = int(input("Введите размер массива: "))
            break
        except ValueError as a:
            print("Введён неверный символ, повторите попытку")
    array = []
    for i in range(size):
        array.insert(i, random.randint(1, 100))
    print(array)
    return array


def count_subarrays(array, target):
    count = 0
    for L in range(len(array) + 1):
        for subset in itertools.combinations(array, L):
            if sum(subset) == target:
                count += 1
    return count


def third_task(array,target):
    while True:
        print("\nДействия:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать случайным образом")
        print("3. Выполнить алгоритм")
        print("4. Вернуться в главное меню")
        sub_sub_choice = str(input("Введите пункт меню: "))
        if sub_sub_choice == "1":
            array = array_input()
            target = int(input("Введите число для проверки: "))
            out_filter = filter(lambda x: filter_values(x,target), array)
            array = list(out_filter)
        elif sub_sub_choice == "2":
            array = array_random()
            target = random.randint(1, 100)
            print(target)
            out_filter = filter(lambda x: filter_values(x, target), array)
            array = list(out_filter)
        elif sub_sub_choice == "3":
            if array == [] or target == 0:
                print("Введите входные данные!")
                continue
            else:
                result = count_subarrays(array, target)
                print(f"Количество подмассивов, дающих сумму {target}: {result}")
        elif sub_sub_choice == "4":
            break
        else:
            print("\nНекорректный выбор. Пожалуйста, повторите попытку!")
