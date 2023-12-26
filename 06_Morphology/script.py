
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
cat_image = plt.imread('./assets/cat.jpg')

# ================================ Morphology ================================ #
# ======= Shapes ======= #
# square = morphology.square(4)
# rectangle = morphology.rectangle(4, 6)


# ======= Erosion & Dialation======= #
# '''
selem = morphology.rectangle(12, 6)

eroded_image = morphology.binary_erosion(cat_image)
dialed_image = morphology.binary_dilation(cat_image)
show_image(cat_image, 'Original')
show_image(eroded_image, 'Erosion')
# plot_comparison(cat_image, eroded_image, '', 'Erosion')
# '''
