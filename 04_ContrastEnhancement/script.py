
# import numpy as np
# from disp import show_image
# from skimage.filters import sobel
# pip install scikit-image
from matplotlib import pyplot as plt
from disp import show_image
from skimage.filters import sobel
from skimage.color import rgb2gray
from disp import plot_comparison
cat_image = plt.imread('./assets/cat.jpg')

# ================================ CONTRAST ENHANCEMENT ================================ #
# ======= HISTORGRAM EQUALIZED ======= #
# from skimage import exposure
# # Obtain the equalized image
# image_eq = exposure.equalize_hist(cat_image)
# plot_comparison(cat_image, image_eq, "Original", "Histogram Equalized")



# ======= ADAPTIVE HISTORGRAM EQUALIZED ======= #
from skimage import exposure
image_adaptive_eq = exposure.equalize_adapthist(cat_image, clip_limit=0.03) # Clip Limit normalize 0 to 1, higher values give more contrast
plot_comparison(cat_image, image_adaptive_eq, "Original", "Adaptive Histogram Equalized")





