from skimage import color
# I will import the original from a random image link online
# original = data.rocket()
original = data.rocket()
grayscale = color.rgb2gray(original)
rgb = color.gray2rgb(grayscale)