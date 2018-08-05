from skimage import io
import numpy as np

img = io.imread('Einstein.bmp')


def mul_noise(o_img, standard_deviation):
    gaussian_noise = np.random.normal(loc=0, scale=standard_deviation, size=o_img.shape)
    r = o_img.shape[0]
    c = o_img.shape[1]
    noisy_img = np.zeros((r, c), dtype=np.uint8)
    for i in range(r):
        for j in range(c):
            # apply noise for every pixel
            noise = o_img[i, j] * (1 + gaussian_noise[i, j])
            if noise < 0:
                noise = 0
            elif noise > 255:
                noise = 255
            noisy_img[i, j] = noise
    # calculate total variance
    print('Image with standard deviation of', standard_deviation, "has total variance =", calculate_total_variance(noisy_img) )

    # return the result image
    return noisy_img


def calculate_total_variance(image):
    r = image.shape[0]
    c = image.shape[1]
    brightness = mij = total_variance = n = 0
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            for t in range(2):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if t == 0:
                            brightness += image[i + k, j + l]
                            if k == 1 and l == 1:
                                mij = brightness / float(9)
                                brightness = 0
                        else:
                            n += (image[i + k, j + l] - mij) ** 2
            total_variance += (1 / float(9)) * n
            n = 0
    return total_variance


def show_img(im):
    io.imshow(im)
    io.show()


def save_img(im, name):
    io.imsave(name, im)


# question 1 tests
manipulated_img = mul_noise(img, 0.1)
show_img(manipulated_img)
save_img(manipulated_img, 'Einstein_0_1.bmp')

manipulated_img = mul_noise(img, 0.5)
show_img(manipulated_img)
save_img(manipulated_img, 'Einstein_0_5.bmp')

manipulated_img = mul_noise(img, 1)
show_img(manipulated_img)
save_img(manipulated_img, 'Einstein_1.bmp')