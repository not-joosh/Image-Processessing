
# import numpy as np
# from disp import show_image
# from skimage.filters import sobel
# pip install scikit-image
from matplotlib import pyplot as plt
from disp import show_image
from skimage.filters import sobel
from skimage.color import rgb2gray
from disp import plot_comparison
egg_image = plt.imread('./assets/egg_img.png')

# =========== EDGE DETECTION   =========== #
# ### -- SOBEL METHOD
# # show_image(egg_image, 'Original Image')
# # gray_scale = rgb2gray(egg_image)
# edge_sobel = sobel(egg_image)
# # show_image(edge_sobel, 'Edge Detection - Sobel Method')
# plot_comparison(egg_image, edge_sobel, 'Original', 'Edges with Sobel')


# GAUSIAN SMOOTHING
from skimage.filters import gaussian
gaussian_image  = gaussian(egg_image) # True if the image is colored, false if not
plot_comparison(egg_image, gaussian_image, 'Original', 'Gaussian Smoothing')


