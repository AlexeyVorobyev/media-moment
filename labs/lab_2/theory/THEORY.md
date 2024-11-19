# Теория по лабораторной работе №2


## 1. Принципы фильтрации командой inRange

Команда inRange используется для фильтрации изображений на основе заданного диапазона значений цвета. Она принимает три аргумента: исходное изображение, нижнюю границу и верхнюю границу диапазона. Функция проверяет каждый пиксель изображения и сравнивает его значение с заданными границами. Если значение пикселя находится в пределах указанного диапазона, он становится белым (255) в выходном изображении; если нет — черным (0). Это позволяет выделять определенные объекты или области на изображении, основываясь на их цвете.

▎2. Команды erode и dilate

• Erode (эрозия): Эта операция уменьшает размеры объектов на изображении. Она работает путем замены каждого пикселя в изображении на минимальное значение среди всех пикселей в окне (или структурном элементе), которое его окружает. Это приводит к уменьшению яркости объектов и удалению мелких шумов.

• Dilate (дилатация): Эта операция, наоборот, увеличивает размеры объектов. Она заменяет каждый пиксель на максимальное значение среди всех пикселей в окне, которое его окружает. Это приводит к увеличению яркости объектов и может помочь заполнить небольшие дыры внутри них.

Обе операции основаны на математических преобразованиях изображений и применяются для изменения структуры объектов, что полезно в различных задачах обработки изображений, таких как удаление шумов и выделение объектов.

▎3. Морфологическое открытие и закрытие

• Морфологическое открытие: Это комбинация операций эрозии и дилатации, где сначала изображение эродируется, а затем дилатируется. Открытие используется для удаления мелких объектов и шумов из изображения, сохраняя при этом более крупные объекты.

• Морфологическое закрытие: Это обратная операция, где сначала выполняется дилатация, а затем эрозия. Закрытие помогает заполнять небольшие дыры и пробелы в объектах, сохраняя их форму.

Необходимость этих операций обусловлена тем, что они позволяют улучшить качество изображений, выделить объекты и подготовить их для дальнейшей обработки или анализа.

▎4. Моменты изображения

Моменты изображения — это статистические характеристики изображения, которые используются для описания его формы и других свойств. Они вычисляются на основе интенсивности пикселей и их координат. Моменты могут быть использованы для вычисления центра масс, ориентации, площади и других геометрических характеристик объекта на изображении.

▎5. Центроид объекта изображения

Центроид объекта изображения — это точка, которая представляет "среднее" положение всех пикселей объекта. Он может быть найден с использованием первых моментов изображения. Центроид рассчитывается как средневзвешенное положение всех пикселей объекта:

Cₓ = ∑ xᵢ ⋅ I(xᵢ) / ∑ I(xᵢ),   Cᵧ = ∑ yᵢ ⋅ I(yᵢ) / ∑ I(yᵢ)


где I(xᵢ) — это интенсивность пикселя в точке (xᵢ, yᵢ).

Центроид используется для анализа формы объекта, отслеживания движения объектов на видео и в других приложениях компьютерного зрения, где важно знать "центр" объекта для дальнейшей обработки или анализа.