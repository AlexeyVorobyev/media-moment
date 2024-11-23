# Лабораторная работа №5

## Выявление движения на видео

1. Реализовал метод, который читает
видеофайл и записывает в один файл только ту часть видео, где в кадре было
движение

<hr/>

Функция **cv2.absdiff** в OpenCV используется 
для вычисления абсолютной разности двух изображений или массивов. 
Определяет, насколько пиксели одного изображения отличаются от соответствующих пикселей другого изображения.

**src1** - изображение 1

**src2** - изображение 2

**diff** - разница между изображениями 

```python
diff = cv2.absdiff(src1, src2)
```

<hr/>

Функция **cv2.threshold** в OpenCV используется для преобразования изображения в бинарное или полутона на основе заданного порога. 
Она анализирует каждый пиксель изображения и применяет указанный порог, чтобы преобразовать его значение.

**src** - исходное изображение

**threshold** - пороговое значение

**maxval** - значение, присваимое пикселям прошедшим порог

**type** - тип пороговой обработки, для бинаризации используем cv2.THRESH_BINARY

**retval** - Фактически использованное значение порога, используется для подбора лучшего порогу с использованием OTSU, TRIANGLE

**thresholded_image** - Результирующее изображение после применения пороговой обработки.

```python
retval, thresholded_image = cv2.threshold(src, threshold, maxval, type)
```

<hr/>

Параметры:

**image** - Входное изображение.
- Должно быть бинарным (например, после cv2.threshold или cv2.Canny).
- Обычно это изображение в градациях серого, где объекты имеют белый цвет, а фон — чёрный.

**mode** - Режим обнаружения контуров. Возможные значения
- cv2.RETR_EXTERNAL: Извлекает только внешние контуры (внешняя граница каждого объекта).
- cv2.RETR_TREE: Извлекает все контуры и строит иерархию (связи между контурами, например, "родитель-ребёнок").
- cv2.RETR_LIST: Извлекает все контуры без создания иерархии.
- cv2.RETR_CCOMP: Извлекает все контуры и строит иерархию в виде 2-уровневой структуры (внешние и внутренние контуры).

**method** - Метод аппроксимации контуров. Возможные значения:

- cv2.CHAIN_APPROX_NONE: Сохраняет все точки контура. Полный набор точек.
- cv2.CHAIN_APPROX_SIMPLE: Убирает избыточные точки, упрощая контур (например, для прямых линий сохраняет только конечные точки).
- cv2.CHAIN_APPROX_TC89_L1 и cv2.CHAIN_APPROX_TC89_KCOS


Возвращаемые значения:

**contours** - Список найденных контуров. Каждый контур — это массив точек (координат) в виде numpy.ndarray.
**hierarchy** - Информация об иерархии контуров. Это массив, описывающий связь между контурами (родители, потомки, соседи).

```python
contours, hierarchy = cv2.findContours(image, mode, method)
```

<hr/>

**contour** -  Один контур, представленный массивом точек (обычно получен из cv2.findContours).

Например, контур — это массив вида [[x1, y1], [x2, y2], ...], упакованный в формат numpy.ndarray.

area - полученное значение

```python
area = cv2.contourArea(contour)
```

<hr/>

**Алгоритм детекции движения на фрейме:**

1. Считываем n изображение
2. Переводим n изображение в черно-белый формат
3. Для n изображения проводим размытие по гауссу
4. Считываем n + 1 изображение
5. Переводим n + 1 изображение в черно-белый формат
6. Для n + 1 изображения проводим размытие по гауссу
7. Находим разницу между n и n + 1  с помощью cv2.absdiff
8. Бинаризируем по пороговому значению с помощью cv2.threshold
9. Находим внешние контуры с помощью cv2.findContours
10. Затем для каждого контура вычисляем площадь, с помощью cv2.contourArea, и если оно больше чем заданное значение то фрейм - с движением
11. Повторить со следующей парой n + 1 и n + 2

```python
    def process_video(
            self,
            input_path: str,
            output_path: str
    ):
        video_ifstream = cv2.VideoCapture(input_path)
        
        ret, frame = video_ifstream.read()

        if not ret:
            logging.error('Не удалось открыть видеофайл.')
            return

        # Читаем первый кадр в чб, применяем размытие Гаусса
        processed_frame = self.__prepare_frame(frame)

        # Подготовка файла для записи нового видео
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        frame_width = int(video_ifstream.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video_ifstream.get(cv2.CAP_PROP_FRAME_HEIGHT))

        video_ofstream = cv2.VideoWriter(output_path, fourcc, 24, (frame_width, frame_height))

        logging.info(f"Видео будет сохранено по адресу: {output_path}")

        while True:
            previous_frame = processed_frame.copy()

            ret, frame = video_ifstream.read()

            if not ret:
                break

            # Преобразование текущего кадра в оттенки серого и размытие
            processed_frame = self.__prepare_frame(frame)

            # Вычисление разницы между текущим и предыдущим кадром
            frame_difference = cv2.absdiff(previous_frame, processed_frame)

            # Проводим операцию двоичного разделения:
            # проводим бинаризацию изображения по пороговому значению (оставляем либо 255, либо 0)
            _, thresholded_frame = cv2.threshold(frame_difference, self._threshold, 255, cv2.THRESH_BINARY)

            # Поиск контуров объектов
            contours, _ = cv2.findContours(thresholded_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:

                contour_area = cv2.contourArea(contour)

                if contour_area < self._contour_area: # Ищем контур больше заданного значения
                    continue

                # Запись исходного кадра, если найдены значимые изменения
                video_ofstream.write(frame)
                break

            # Прерывание по нажатию клавиши 'Esc'
            if cv2.waitKey(1) & 0xFF == 27:
                break

        video_ifstream.release()
        video_ofstream.release()
        logging.info("Видео успешно записано")
        cv2.destroyAllWindows()
```
