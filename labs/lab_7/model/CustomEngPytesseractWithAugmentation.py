from collections import Counter

import pytesseract
import cv2

from .BaseModel import BaseModel


class CustomEngPytesseractWithAugmentation(BaseModel):

    def image_to_string(self, image, **params):
        texts = []
        for angle in range(-20, 21):  # от -20 до 20 градусов (включительно)
            # Поворот изображения
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated_image = cv2.warpAffine(image, M, (w, h))

            # Распознавание текста
            text = pytesseract.image_to_string(
                image,
                config="--oem 1 --psm 6 -l custom_eng",
            )
            texts.append(text)

        # Удаляем пустые ответы
        texts = filter(lambda text: text.strip() != '', texts)
        # Подсчет наиболее часто встречающегося текста
        most_common_text = Counter(texts).most_common(1)
        if most_common_text:
            return most_common_text[0][0]  # Возвращаем наиболее частое распознанное значение
        return None  # Если ничего не найдено
