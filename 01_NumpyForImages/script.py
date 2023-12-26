
from matplotlib import pyplot as plt
import numpy as np
from disp import show_image
cat_image = plt.imread('./assets/cat.jpg')
# print(type(cat_image))


# ----- COLORS ----- #
# # Getting Red Intensity of cat_image
# red = cat_image[:, :, 0]

# # Getting Green Intensity of cat_image
# green = cat_image[:, :, 1]

# # Getting Blue Intensity of cat_image
# blue = cat_image[:, :, 2]

# fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# axs[0].imshow(red, cmap='gray')
# axs[0].set_title('Red Intensity')

# axs[1].imshow(green, cmap='gray')
# axs[1].set_title('Green Intensity')

# axs[2].imshow(blue, cmap='gray')
# axs[2].set_title('Blue Intensity')

# plt.show()

# ----- SHAPE ----- #
print(cat_image.shape, cat_image.size)

# Flipping the image vertically
vertically_flipped = np.flipud(cat_image)
# show_image(vertically_flipped, "Vertically flipped image")

# Horizontally flipping the image
horizontally_flipped = np.fliplr(cat_image)
# show_image(horizontally_flipped, "Horizontally flipped image")


# Histogram of an image: the graphical representation of the intensity distribution of an image, 0 (black), 255(white)
#Making a histogram of original cat_image
# plt.hist(cat_image.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')
# plt.title('Histogram of original image')
# plt.show()


red = cat_image[:, :, 0]
plt.hist(red.ravel(), bins = 256)
plt.title('Red Histogram')
plt.show()

blue = cat_image[:, :, 0]
plt.hist(red.ravel(), bins = 256)
plt.title('Red Histogram')
plt.show()

