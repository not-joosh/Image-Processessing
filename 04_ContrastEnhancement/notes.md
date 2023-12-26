# Calculating the Image's Contrast max() - min() pixel range => contrast
```py
In [1]:
np.max(clock_image)
Out[1]:
247
In [2]:

In [2]:
np.min(clock_image)
Out[2]:
99
In [3]:
contrast = np.max(clock_image) - np.min(clock_image)
In [4]:
print(contrast)
148
```


# Improving an Xray Image to have more contrast so that we can see details
```py
# Import the required module
from skimage import exposure

# Show original x-ray image and its histogram
show_image(chest_xray_image, 'Original x-ray')

plt.title('Histogram of image')
plt.hist(chest_xray_image.ravel(), bins=256)
plt.show()

# Use histogram equalization to improve the contrast
xray_image_eq =  exposure.equalize_hist(chest_xray_image)

# Show the resulting image
show_image(xray_image_eq, 'Resulting image')
```

# Aerial Image enhancement to see the aerial view (birds-view) better
```py
# Import the required module
from skimage import exposure

# Use histogram equalization to improve the contrast
image_eq =  exposure.equalize_hist(image_aerial)

# Show the original and resulting image
show_image(image_aerial, 'Original')
show_image(image_eq, 'Resulting image')

```

# PROMPT:
    Import the module that includes the Contrast Limited Adaptive Histogram Equalization (CLAHE) function.
    
    Obtain the image you'll work on, with a cup of coffee in it, from the module that holds all the images for testing purposes.
    
    From the previously imported module, call the function to apply the adaptive equalization method on the original image and set the clip limit to 0.03.
```py
# Import the necessary modules
from skimage import data, exposure

# Load the image
original_image = data.coffee()

# Apply the adaptive equalization on the original image
adapthist_eq_image = exposure.equalize_adapthist(original_image, clip_limit=0.03)

# Compare the original image to the equalized
show_image(original_image)
show_image(adapthist_eq_image, '#ImageProcessingDatacamp')
```