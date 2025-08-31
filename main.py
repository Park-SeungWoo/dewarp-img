import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def show(image: np.ndarray) -> None:
    plt.figure()
    plt.imshow(image)
    plt.show()

def save(image: np.ndarray, filename: str) -> None:
    cv.imwrite(filename, image)

def sharpen(image: np.ndarray) -> np.ndarray:
    kernel: np.ndarray = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    return cv.filter2D(image, -1, kernel)

def crop(image: np.ndarray) -> np.ndarray:
    return image

def dewarp(image: np.ndarray) -> np.ndarray:
    return image


file_name:str = "report_1.jpg"
img: np.ndarray = cv.imread(f'datas/{file_name}', cv.IMREAD_COLOR_RGB)

img = sharpen(img)
img = crop(img)
img = dewarp(img)

# show(img)
save(img, f'results/{file_name}')