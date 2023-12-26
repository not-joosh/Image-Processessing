
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
from skimage import morphology
import numpy as np

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
# Simple Lienar Iterative Clustering (SLIC)
segments = slic(cat_image, n_segments=200, compactness=10)
# print('SLIC number of segments: {}'.format(len(np.unique(segments))))

segmented_image = label2rgb(segments, image=cat_image, kind='avg')
plot_comparison(cat_image, segmented_image, 'Original', 'Segmented Image')
