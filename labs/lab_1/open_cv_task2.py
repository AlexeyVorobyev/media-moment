import cv2

config = {
    "first": {
        "file": "files/2.jpg",
        "imread_flag": cv2.IMREAD_GRAYSCALE,
        "window_flag": cv2.WINDOW_GUI_NORMAL
    },
    "second": {
        "file": "files/2.png",
        "imread_flag": cv2.IMREAD_COLOR,
        "window_flag": cv2.WARP_INVERSE_MAP
    },
    "third": {
        "file": "files/2.webp",
        "imread_flag": cv2.IMREAD_REDUCED_COLOR_8,
        "window_flag": cv2.WINDOW_GUI_EXPANDED
    }
}

for key, value in config.items():
    image = cv2.imread(value["file"], flags=value["imread_flag"])
    cv2.namedWindow(key, value["window_flag"])
    cv2.imshow(key, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
