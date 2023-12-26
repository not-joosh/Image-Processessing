
# import numpy as np
# from disp import show_image
# from skimage.filters import sobel
# pip install scikit-image
from matplotlib import pyplot as plt
from disp import show_image
from skimage.filters import sobel
from skimage.color import rgb2gray
from disp import plot_comparison
from skimage.transform import rotate, rescale, resize
cat_image = plt.imread('./assets/cat.jpg')

# ================================ TRANSFORMATION ================================ #
# ======= ROTATING AN IMAGE ======= #
# image_rotated = rotate(cat_image, 180)
# show_image(image_rotated, "Image Rotated")

# ======= RESCALING AN IMAGE ======= #
# Rescaling the image to be 4 times smaller
# image_rescaled = rescale(cat_image, 1.0 / 4.0, anti_aliasing = True)
# show_image(image_rescaled, "Image Rescaled")
# When Aliasing = False, it will be pixelated, with True = Smoother

# ======= RESIZING AN IMAGE ======= #
# height = 480
# width = 500

# image_resized = resize(cat_image, (height, width), anti_aliasing = True)
# show_image(image_resized, "Image Resized")