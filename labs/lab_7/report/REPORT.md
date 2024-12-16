# Лабораторная работа №7

Процесс обучения TESSERACT:

1. Требуется использование утилиты tesstrain, которую можно скачать по [ссылке](https://github.com/tesseract-ocr/tesstrain.git) в виде репозитория.

2. Создаём датасет данных для обучения в папке data/ground-truth

3. Необходимо сопоставить каждому фото файл .gt.txt содержащий информацию о корректных данных

4. Адские танцы с бубном

5. make training MODEL_NAME=custom_eng START_MODEL=eng - команда для дообучения на основе eng модели

6. make training MODEL_NAME=custom - команда для обучения сырой модели
