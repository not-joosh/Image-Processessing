
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
cat_image = plt.imread('./assets/cat.jpg')
old_picture = plt.imread('./assets/old_picture.png')
# ================================ NOISE ================================ #
from skimage.util import random_noise
from skimage.restoration import denoise_tv_chambolle
from skimage.restoration import denoise_bilateral


# ================================ Segmentation ================================ #
from skimage.segmentation import slic # Unsupervised Segmentation
from skimage.color import label2rgb

# ================================ Contours ================================ #
grayed_image = rgb2gray(cat_image)
thresh = threshold_otsu(grayed_image)
threshhold_image = grayed_image > thresh 
# Find contours
from skimage import measure
contours = measure.find_contours(threshhold_image, 0.8)
# plot_comparison(cat_image, contours,'ContourS', 'Image with Contours')
