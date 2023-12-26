import matplotlib.pyplot as plt
from scripts.img_show import show_image
from skimage import color



def gray_scale_testing(original):
    # print(original)
    grayscale = color.rgb2gray(original)
    show_image(grayscale, "Grayscale conversion")


original = plt.imread("assets/00_dog_blur.jpg")
gray_scale_testing(original)