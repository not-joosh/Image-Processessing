
# import numpy as np
# from disp import show_image
# from skimage.filters import sobel
# pip install scikit-image
from matplotlib import pyplot as plt
from disp import show_image
from disp import plot_comparison
from skimage.transform import rotate, rescale, resize
from skimage import morphology
import numpy as np

from skimage.filters import sobel
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
# ================================ Image Restoration ================================ #
from restoration import get_mask
from skimage.restoration import inpaint
# ================================ NOISE ================================ #
from skimage.util import random_noise
from skimage.restoration import denoise_tv_chambolle
from skimage.restoration import denoise_bilateral

# ================================ Segmentation ================================ #
from skimage.segmentation import slic # Unsupervised Segmentation
from skimage.color import label2rgb

# ================================ Contours ================================ #
from skimage import measure

# ================================ Canny Edge Detection ================================ #
from skimage.feature import canny
cat_image = plt.imread('./assets/cat.jpg')
old_picture = plt.imread('./assets/old_picture.png')

gray_image = rgb2gray(cat_image)

# Apply Gausian Filter
canny_edges = canny(gray_image, sigma=0.1) # The lower, the more edges, the higher the less edges because more noise or something hahaha

# print(canny_image)
plot_comparison(gray_image, canny_edges, "Orioginal", "Canny")
# show_image(canny_image, "Canny Edge Detection")
