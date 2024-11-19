import cv2


def begin():
    return cv2.VideoCapture(0)


def process_stream(cap, process_frame_callback=lambda x:x):
    while True:
        ret, frame = cap.read()  # Чтение текущего кадра
        if not ret:  # Проверка на успешное чтение кадра
            break

        process_frame_callback(frame)

        # Ожидание 20 мс и проверка нажатия клавиши 'Esc' (код 27)
        if cv2.waitKey(20) & 0xFF == 27:
            break


def end(cap):
    cap.release()
    cv2.destroyAllWindows()
