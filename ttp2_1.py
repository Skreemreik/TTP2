import numpy as nump

#I am Skreemerik
def matrix_input(matrix):
    size = int(input("Введите размер квадратной матрицы: "))
    matrix = []
    for i in range(size):
        row = input(f"Введите элементы {i + 1}-й строки через пробел:").split()
        matrix.append([int(element) for element in row])
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(element) for element in row]))


def matrix_random(matrix):
    size = int(input("Введите размер квадратной матрицы: "))
    matrix = nump.random.randint(-10, 10, size=(size, size))
    print("Сгенерированная матрица:")
    print_matrix(matrix)
    return matrix


def rotate_matrix_counterclockwise(matrix):
    # Определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем пустую матрицу соответствующего размера
    rotated_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            # Достаем элемент из исходной матрицы и помещаем его в новую матрицу
            rotated_matrix[j][rows - i - 1] = matrix[i][j]

    return rotated_matrix


def rotate_matrix_clockwise(matrix):
    # Определяем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем пустую матрицу соответствующего размера
    rotated_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            # Достаем элемент из исходной матрицы и помещаем его в новую матрицу
            rotated_matrix[cols - j - 1][i] = matrix[i][j]

    return rotated_matrix


def first_task(matrix):
    while True:
        print("\nДействия:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать случайным образом")
        print("3. Выполнить алгоритм")
        print("4. Вернуться в главное меню")
        sub_sub_choice = str(input("Введите пункт меню: "))
        if sub_sub_choice == "1":
            matrix = matrix_input(matrix)
        elif sub_sub_choice == "2":
            matrix = matrix_random(matrix)
        elif sub_sub_choice == "3":
            if matrix is None:
                print("Введите входные данные!")
                continue
            else:
                print("\nДействия:")
                print("1. Повернуть матрицу против часовой стрелке")
                print("2. Повернуть матрицу по часовой стрелки")
                matrix_choice = str(input("Введите пункт меню: "))
                if matrix_choice == "1":
                    rotated_matrix = rotate_matrix_clockwise(matrix)
                    print_matrix(rotated_matrix)
                elif matrix_choice == "2":
                    rotated_matrix = rotate_matrix_counterclockwise(matrix)
                    print_matrix(rotated_matrix)
        elif sub_sub_choice == "4":
            break
        else:
            print("\nНекорректный выбор. Пожалуйста, повторите попытку!")