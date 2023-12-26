
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
# # ======= NOISY IMAGE, HOW TO MESS IT UP ======= #
# noisy_image = random_noise(cat_image)
# plot_comparison(cat_image, noisy_image, "Original Image", "Noise Image")





# ================================ HOW TO CLEAN UP NOISE ================================ #
# # ====== Total Variation (TV) Denoising Type ====== #
# denoised_image = denoise_tv_chambolle(old_picture, weight=0.1)
# plot_comparison(old_picture, denoised_image, "Original Image", "TV Denoised Image")



# ====== Billateral Denoising Type ====== #
# print(old_picture.shape)
# denoised_image = denoise_bilateral(cat_image)


#  Wavelet Denoising Type is another tpye #