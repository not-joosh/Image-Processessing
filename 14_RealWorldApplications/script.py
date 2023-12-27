
# import numpy as np
# from disp import show_image
# from skimage.filters import sobel
# pip install scikit-image
from matplotlib import pyplot as plt
from disp import show_detected_face, show_image, show_img_with_corners
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
# ================================ NOISE ================================ #
from skimage.util import random_noise
from skimage.restoration import denoise_tv_chambolle
from skimage.restoration import denoise_bilateral

# ================================ Segmentation ================================ #
from skimage.segmentation import slic # Unsupervised Segmentation
from skimage.color import label2rgb

# ================================ Contours ================================ #
from skimage import measure

# ================================ Canny Edge Detection ================================ #
from skimage.feature import canny

# ================================ Corner  Detection ================================ #
from skimage.feature import corner_harris, corner_peaks

# ================================ Face Detection ================================ #
from skimage.feature import Cascade
from skimage import data

# print("test0")
# # This method needs an XML file for the training data
# trained_file = data.lbp_frontal_face_cascade_filename()
# print("test1")

# # initialize the detector
# detector = Cascade(trained_file)
# print("test2")
# # Actual face detection mechanism
# detected = detector.detect_multi_scale(img=my_favorite_people, 
#                                         scale_factor=1.2, 
#                                         step_ratio=1, 
#                                         min_size=(10, 10), 
#                                         max_size=(200, 200))
# print("test3")
# show_detected_face(my_favorite_people, detected)
# print("test4")


# ================================ APPLICATIONS | PRIVACY PROTECTION ================================ #
# cat_image = plt.imread('./assets/cat.jpg')
# old_picture = plt.imread('./assets/old_picture.png')
# mountain_picture = plt.imread('./assets/mountain.jpg')

# Firstly Detect the  faces
from skimage import data
from skimage.feature import Cascade
from skimage.filters import gaussian
from face_detection import getFace, mergeBlurryFace
my_favorite_people = plt.imread('./assets/cpe.jpg')
# Lets import the training data
trained_file = data.lbp_frontal_face_cascade_filename()
# Initialize the detector
detector = Cascade(trained_file)
# Detect the faces
detected = detector.detect_multi_scale(img=my_favorite_people, 
                                        scale_factor=1.2, 
                                        step_ratio=1, 
                                        min_size=(50, 50), 
                                        max_size=(100, 100))
# For each detected face
for detected_face in detected:
    # Obtain the face coordinates
    face = getFace(detected_face, my_favorite_people)
    
    # Apply gaussian filter to extracted face
    blurred_face = gaussian(face, sigma=10)
    print("Phase # is done!")

    # Merge this blurry face to our final image and show it
    merged = mergeBlurryFace(my_favorite_people, blurred_face, detected_face)

# Finally print the final modified image and also print the original with plot comparison
# show_image(my_favorite_people, "Original Image")
# show_image(merged, "Blurred Image")
plot_comparison(my_favorite_people, merged, "Original vs Blurred")