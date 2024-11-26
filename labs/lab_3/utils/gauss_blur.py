import numpy as np
import cv2

from . import conv_matrix as convm, normalize_matrix as nm


def conv_operation(
        item_x: int,
        item_y: int,
        image: np.ndarray,
        kernel: np.ndarray,
        kernel_size: int
) -> float:
    """
    Проводит операцию свёртки

    :param item_x: Индекс элемента исходной матрицы по горизонтали
    :param item_y: Индекс элемента исходной матрицы по вертикали
    :param image: Изображение
    :param kernel: Ядро свёртки
    :param kernel_size: Размер ядра свёртки
    :return:
    """
    value = 0
    half_size = int(kernel_size // 2)
    for k in range(-half_size, half_size + 1):
        for l in range(-half_size, half_size + 1):
            value += image[item_y + k, item_x + l] * kernel[k + half_size, l + half_size]

    return value


def gauss_blur(
        image: np.ndarray,
        kernel_size: int,
        deviation: float
) -> np.ndarray:
    """
        Осуществляет блюр изображения с помощью матрицы свёртки и распределения по гауссу.

        :param: image: Изображение
        :param: kernel_size: Размерность ядра, должно быть нечётным
        :param: deviation: Стандартное отклонение для гаусса

        :return: Обработанное изображение
        """

    if kernel_size % 2 == 0:
        raise Exception('Kernel size must be odd.')

    kernel = nm.normalize_matrix(
        convm.conv_matrix(kernel_size, deviation)
    )

    blurred_image = image.copy()

    kernel_shift = kernel_size // 2

    bordered_image_with_borders = cv2.copyMakeBorder(
        blurred_image, kernel_shift, kernel_shift, kernel_shift, kernel_shift,
        cv2.BORDER_CONSTANT,
        value=[0, 0, 0]
    )

    h, w = image.shape[:2]
    half_kernel_size = int(kernel_size // 2)

    for x in range(half_kernel_size, w - half_kernel_size):  # Проход по матрице горизонтально
        for y in range(half_kernel_size, h - half_kernel_size):  # Проход по матрице вертикально
            # Операция свёртки
            blurred_val = conv_operation(x, y, image, kernel, kernel_size)

            bordered_image_with_borders[y, x] = blurred_val

    return bordered_image_with_borders
