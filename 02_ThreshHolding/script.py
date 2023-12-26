
from matplotlib import pyplot as plt
import numpy as np
from disp import show_image
cat_image = plt.imread('./assets/cat.jpg')

# Declare threshhold value
# threshhold = 127 # Midpoint between 0 and 255

# Apply threshhold to image
# binary = cat_image > threshhold
# # show_image(cat_image, 'Original')
# # show_image(binary, 'Thresholded')


# # DEBUG
# # # Convert cat_image to float32 data type
# # cat_image = cat_image.astype(np.float32)

# # # Apply threshold to image
# # binary = cat_image > threshhold

# # # Convert binary array to uint8 data type
# # binary = binary.astype(np.uint8)

# # # show_image(cat_image, 'Original')
# # show_image(binary, 'Thresholded')


# # ----------- Inverted Thresholding ------------ #
# threshold = 127 

# # Applying the inverted Thresholding
# i_binary = cat_image <= threshold
# show_image(cat_image, "Original")
# show_image(i_binary, "Inverted Binary")


# Trying all thresh holding aglorithms
# from skimage.filters import try_all_threshold
# from disp import show_plot

# fig, ax = try_all_threshold(cat_image, verbose=False)
# show_plot(fig, ax)



# # ----------- Otsu's Method ------------ #

from skimage.filters import threshold_otsu
thresh = threshold_otsu(cat_image)

binary_global = cat_image > thresh

show_image(binary_global, "Global Thresholding")


