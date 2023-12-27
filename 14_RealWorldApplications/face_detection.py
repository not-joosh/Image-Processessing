

def getFace(d, image):
    '''Extracts the face rectangle from the image using the coordinates
    of the detected.'''
    # X and Y starting points of the face rectangle     
    x, y  = d['r'], d['c']

    # The width and height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']

    # Extract the detected face
    face = image[x:width, y:height]
    return face

def mergeBlurryFace(original_img, gaussian_face, d):
    # X and Y starting points of the face rectangle
    x, y  = d['r'], d['c']

    # The width and height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']

    # Merge this blurry face to our final image and show it
    original_img[x:width, y:height] = gaussian_face
    return original_img