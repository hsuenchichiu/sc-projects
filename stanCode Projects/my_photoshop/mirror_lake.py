"""
File: mirror_lake.py
name: HsuenChi Chiu

----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: original image
    :return: the original image and the vertically flipped image
    """
    img = SimpleImage(filename)
    # create new image
    new_img = SimpleImage.blank(img.width, img.height*2)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x,y)
            new_pixel1 = new_img.get_pixel(x,y)
            # find the vertically reflect pixel
            new_pixel2 = new_img.get_pixel(x,new_img.height-1-y)

            new_pixel1.red = img_pixel.red
            new_pixel1.green = img_pixel.green
            new_pixel1.blue = img_pixel.blue

            new_pixel2.red = img_pixel.red
            new_pixel2.green = img_pixel.green
            new_pixel2.blue = img_pixel.blue
    return new_img


def main():
    """
    the program helps reflect the original image vertically.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
