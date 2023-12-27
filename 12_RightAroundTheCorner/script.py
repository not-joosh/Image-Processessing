
# import numpy as np
# from disp import show_image
# from skimage.filters import sobel
# pip install scikit-image
from matplotlib import pyplot as plt
from disp import show_image, show_img_with_corners
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

# ================================ Corner  Detection ================================ #
from skimage.feature import corner_harris, corner_peaks

cat_image = plt.imread('./assets/cat.jpg')
old_picture = plt.imread('./assets/old_picture.png')
mountain_image = plt.imread('./assets/mountain.jpg')
# point of interest (corner or edges). Corners are intersection of two edges
gray_image = rgb2gray(mountain_image)
measure_image = corner_harris(gray_image)
coords = corner_peaks(corner_harris(gray_image), min_distance=5)
print("A total of {} corners were detected.".format(len(coords)))
show_img_with_corners(mountain_image, coords)
# plot_comparison(gray_image, measure_image, 'Original', 'Corners')
