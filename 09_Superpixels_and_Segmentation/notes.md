# Calculating the amount of pixels on the screen
```py
In [1]:
face_image.shape
Out[1]:
(265, 191, 3)
In [2]:
total_pixels = face_image.shape[0] * face_image.shape[1]
In [3]:
print(total_pixels)
50615
In [4]:

```

# Segmenting a picture of a person
```py
# Import the slic function from segmentation module
from skimage.segmentation import slic

# Import the label2rgb function from color module
from skimage.color import label2rgb

# Obtain the segmentation with 400 regions
segments = slic(face_image, n_segments= 400)

# Put segments on top of original image to compare
segmented_image = label2rgb(segments, face_image, kind='avg')

# Show the segmented image
show_image(segmented_image, "Segmented image, 400 superpixels")
```