import cv2

# ip телефона
ip = str(input("Enter IP address: "))

# URL-адрес камеры телефона
url = f'http://{ip}:8080/video'

cap = cv2.VideoCapture(url)

# Устанавливаем размер окна
window_width = 640
window_height = 480

while True:
    # Считывание кадра с камеры телефона
    ret, frame = cap.read()

    # Уменьшаем размер кадра
    frame = cv2.resize(frame, (window_width, window_height))

    # Отображение кадра
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
