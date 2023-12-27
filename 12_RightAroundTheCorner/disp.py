import matplotlib.pyplot as plt

def show_image(image_in, message):
    plt.imshow(image_in)
    plt.title(message)
    plt.show()


def show_plot(fig, ax):
    plt.show(block=True)

def plot_comparison(image1, image2, message1, message2):
    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(image1)
    ax[0].set_title(message1)
    ax[1].imshow(image2)
    ax[1].set_title(message2)
    plt.show()
    
def show_img_with_corners(image, coords, title="Corners detected"):
    # plt.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
    plt.imshow(image, interpolation='nearest', cmap = 'gray')
    plt.title(title)
    plt.plot(coords[:, 1], coords[:, 0], '+r', markersize=15)
    plt.axis('off')
    plt.show()
