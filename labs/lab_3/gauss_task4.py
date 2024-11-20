import cv2

from utils.gauss_blur import gauss_blur

initial_image = cv2.imread('files/1.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)

cv2.imshow("INITIAL", initial_image)

blur_params = {
    "KER: 5, DEV: 0.5": (5, 0.5),
    "KER: 9, DEV: 0.5": (9, 0.5),
    "KER: 5, DEV: 1": (5, 1),
    "KER: 9, DEV: 1": (9, 1),
}

# Перебор параметров и отображение результатов
for title, (kernel_size, sigma) in blur_params.items():
    blurred_image = gauss_blur(initial_image, kernel_size, sigma)
    cv2.imshow(title, blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
