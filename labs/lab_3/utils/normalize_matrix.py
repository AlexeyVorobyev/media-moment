import numpy as np


def normalize_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Нормируем матрицу, чтобы сумма элементов была равна 1
    :param matrix: Исходная матрица
    :return: Нормализованная матрица
    """
    return matrix / np.sum(matrix)
