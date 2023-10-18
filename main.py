import ttp2_1
import ttp2_2
import ttp2_3


def main():
    target = 0
    matrix = None
    array = []
    array1 = []
    array2 = []
    while True:
        print("\nМеню:")
        print("1. Перейти к списку заданий")
        print("2. Завершить работу программы")
        choice = str(input("Введите пункт меню: "))

        if choice == '1':
            print("\nЗадания:")
            print("1. Поворот матрицы")
            print("2. Сумма и разность массивов")
            print("3. Число и сумма подмассивов")
            print("4. Вернуться в главное меню")
            sub_choice = str(input("Введите пункт меню: "))
            if sub_choice == "1":
                ttp2_1.first_task(matrix)
            elif sub_choice == "2":
                ttp2_2.second_task(array1, array2)
            elif sub_choice == "3":
                ttp2_3.third_task(array, target)
            elif sub_choice == "4":
                continue
            else:
                print("\nНекорректный выбор. Пожалуйста, повторите попытку!")

        elif choice == '2':
            break

        else:
            print("\nНекорректный выбор. Пожалуйста, повторите попытку!")


if __name__ == '__main__':
    main()
