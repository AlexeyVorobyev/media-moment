import numpy as np


def gauss(x: int, y: int, sigma: float | int, a: float | int, b: float | int) -> float:
    """
    Функция Гаусса
    :param x: Первый индекс матрицы
    :param y: Второй индекс матрицы
    :param sigma: Среднеквадратичное отклонение
    :param a: Мат. ожидание двумерной случайной величины
    :param b: Мат. ожидание двумерной случайной величины
    :return: Значение гауссовой функции
    """
    double_sigma_squared = 2 * sigma * sigma
    return np.exp(-((x - a) ** 2 + (y - b) ** 2) / double_sigma_squared) / (np.pi * double_sigma_squared)
