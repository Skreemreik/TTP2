import random

def filter_numbers(in_array):
   if isinstance(in_array, int):
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
        array.insert(i, random.randint(1, 9))
    print(array)
    return array


def add_arrays(array1, array2):
    out_filter = filter(filter_numbers, array1)
    array1_temp = list(out_filter)
    out_filter = filter(filter_numbers, array2)
    array2_temp = list(out_filter)
    sum_array = []
    carry = 0
    while len(array1_temp) > 0 or len(array2_temp) > 0:
        if len(array1_temp) > 0:
            digit1 = array1_temp.pop()
        else:
            digit1 = 0
        if len(array2_temp) > 0:
            digit2 = array2_temp.pop()
        else:
            digit2 = 0
        temp_sum = digit1 + digit2 + carry
        sum_array.insert(0, temp_sum % 10)
        carry = temp_sum // 10
    if carry > 0:
        sum_array.insert(0, carry)
    return sum_array


def subtract_arrays(array1, array2):
    out_filter = filter(filter_numbers, array1)
    array1_temp = list(out_filter)
    out_filter = filter(filter_numbers, array2)
    array2_temp = list(out_filter)
    for i, obj in enumerate(array1):
        array1_temp.insert(i, obj)
    for i, obj in enumerate(array2):
        array2_temp.insert(i, obj)
    result_array = []
    borrow = 0
    while len(array1_temp) > 0 or len(array2_temp) > 0:
        if len(array1_temp) > 0:
            digit1 = array1_temp.pop()
        else:
            digit1 = 0
        if len(array2_temp) > 0:
            digit2 = array2_temp.pop()
        else:
            digit2 = 0
        digit1 -= borrow
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        result_array.insert(0, digit1 - digit2)
    return result_array


def second_task(array1, array2):
    while True:
        print("\nДействия:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать случайным образом")
        print("3. Выполнить алгоритм")
        print("4. Вернуться в главное меню")
        sub_sub_choice = str(input("Введите пункт меню: "))
        if sub_sub_choice == "1":
            array1 = array_input()
            array2 = array_input()
        elif sub_sub_choice == "2":
            array1 = array_random()
            array2 = array_random()
        elif sub_sub_choice == "3":
            if array1 == [] or array2 == []:
                print("Введите входные данные!")
                continue
            else:
                print("\nДействия:")
                print("1. Вывести сумму массивов")
                print("2. Вывести разность массивов")
                arrays_choice = str(input("Введите пункт меню: "))
                if arrays_choice == "1":
                    sum_result = add_arrays(array1, array2)
                    print(sum_result)
                elif arrays_choice == "2":
                    subtract_result = subtract_arrays(array1, array2)
                    print(subtract_result)
        elif sub_sub_choice == "4":
            break
        else:
            print("\nНекорректный выбор. Пожалуйста, повторите попытку!")