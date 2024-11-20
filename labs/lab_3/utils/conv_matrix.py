import numpy as np

from . import gauss

def conv_matrix(matrix_size: int, ms_deviation: float | int) -> np.ndarray:
    """
    Создание и заполнение матрицы свёртки
    :param matrix_size: Размер матрицы
    :param ms_deviation: Среднеквадратичное отклонение
    :return: Матрица numpy
    """
    matrix = np.zeros((matrix_size, matrix_size))  # Инициализируем матрицу нулями
    a = b = matrix_size // 2  # Считаем математическое ожидание двумерной случайной величины

    # Заполяем матрицу свёртки
    for y in range(matrix_size):
        for x in range(matrix_size):
            print(y, x)
            matrix[y, x] = gauss.gauss(x, y, ms_deviation, a, b)

    return matrix
