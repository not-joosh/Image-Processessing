import matplotlib.pyplot as plt
def show_image(image_in, message):
    plt.imshow(image_in)
    plt.title(message)
    plt.show()