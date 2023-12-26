
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

# ================================ Image Restoration ================================ #
# ======= Image Restoration/Reconstruction ======= #
# Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image.
# Image reconstruction is the operation of taking a set of images and combining them in a way that improves the quality of the resulting image.
mask = get_mask(cat_image)
# print(mask)
restored_image = inpaint.inpaint_biharmonic(cat_image, mask)
show_image(restored_image, 'Restored Image')
