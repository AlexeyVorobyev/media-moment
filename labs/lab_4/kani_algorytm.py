import enum

import cv2
import numpy as np

class ImageShowKaniAlgorythmEnum(enum.Enum):
    GRAYSCALE = 0
    GAUSSIAN = 1

class KaniAlgorythm:

    _image_size: (int, int)
    _deviation: float
    _kernel_size: int
    _image_show_list: list[ImageShowKaniAlgorythmEnum] = [
        ImageShowKaniAlgorythmEnum.GRAYSCALE,
        ImageShowKaniAlgorythmEnum.GAUSSIAN,
    ]

    def __init__(
            self,
            image_size: (int, int) = (500, 500),
            deviation: float = 1,
            kernel_size: int = 5,
            image_show_list=None
    ):
        """
        Инициализация класса
        :param image_size: размер изображения
        :param deviation: отклонение
        :param kernel_size: размерность ядра
        :param image_size: размер изображения
        :param image_show_list: настройка отображения
        """
        if image_show_list is None:
            self._image_show_list = [
                ImageShowKaniAlgorythmEnum.GRAYSCALE,
                ImageShowKaniAlgorythmEnum.GAUSSIAN,
            ]
        self._image_size = image_size
        self._deviation = deviation
        self._kernel_size = kernel_size

    def __preprocess_image(self, path_to_image: str) -> np.ndarray:
        """
        Провести предобработку изображения, считать из файла, привести к оттенкам серого, изменить размер
        :param path_to_image:
        :return:
        """
        img = cv2.imread(path_to_image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, self._image_size)

        if ImageShowKaniAlgorythmEnum.GRAYSCALE in self._image_show_list:
            cv2.imshow("GrayScale", img)

        img = cv2.GaussianBlur(img, (self._kernel_size, self._kernel_size), self._deviation)

        if ImageShowKaniAlgorythmEnum.GAUSSIAN in self._image_show_list:
            cv2.imshow("Gaussian", img)

        return img

    def process_image(
            self,
            image_path: str
    ):
        """
        Провести обработку алгоритмом Канни
        :param image_path:
        :return:
        """
        self.__preprocess_image(image_path)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
