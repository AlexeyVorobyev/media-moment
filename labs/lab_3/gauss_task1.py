import logging

import cv2
import numpy as np

from utils.conv_matrix import conv_matrix
from utils.normalize_matrix import normalize_matrix

logging.root.setLevel(logging.INFO)

ms_deviation = 0.4

for matrix_size in (3, 5, 7):
    logging.log(logging.INFO, f'\nРазмер матрицы: {matrix_size}')
    logging.log(logging.INFO, f'Среднеквадратичное отклонение: {ms_deviation}')

    matrix = conv_matrix(matrix_size, ms_deviation)

    logging.log(logging.INFO, "Без нормализации:\n")
    logging.log(logging.INFO, matrix)

    cv2.imshow('MATRIX', cv2.resize(matrix, (300, 300)))

    matrix = normalize_matrix(matrix)

    cv2.imshow('MATRIX normalized', cv2.resize(matrix, (300, 300)))

    logging.log(logging.INFO, "Нормализована:\n")
    logging.log(logging.INFO, matrix)

    logging.log(logging.INFO, f'Сумма элементов матрицы: {np.sum(matrix)}')

    cv2.waitKey(0)

    cv2.destroyAllWindows()
