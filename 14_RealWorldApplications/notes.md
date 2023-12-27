# Blurring Phases of Group Image
```py
# Detect the faces
detected = detector.detect_multi_scale(img=group_image, 
                                       scale_factor=1.2, step_ratio=1, 
                                       min_size=(10, 10), max_size=(100, 100))
# For each detected face
for d in detected:  
    # Obtain the face rectangle from detected coordinates
    face = getFaceRectangle(d)
    
    # Apply gaussian filter to extracted face
    blurred_face = gaussian(face, multichannel=True, sigma = 8)
    
    # Merge this blurry face to our final image and show it
    resulting_image = mergeBlurryFace(group_image, blurred_face) 
show_image(resulting_image, "Blurred faces")
```

# Repairing Graduation Photo for sally
```py
# Import the necessary modules
from skimage.restoration import denoise_tv_chambolle, inpaint
from skimage import transform

# Transform the image so it's not rotated
upright_img = transform.rotate(damaged_image, 20)

# Remove noise from the image, using the chambolle method
upright_img_without_noise = denoise_tv_chambolle(upright_img,weight=0.1, multichannel=True)

# Reconstruct the image missing parts
def get_mask(image):
    mask = np.zeros(image.shape[:-1])
    mask[450:475, 470:495] = 1
    mask[320:355, 140:175] = 1
    mask[130:155, 345:370] = 1
    return mask

mask = get_mask(upright_img)
result =inpaint.inpaint_biharmonic(upright_img_without_noise, mask, multichannel=True)

show_image(result)
```
