"""
File: shrink.py
name: HsuenChi Chiu

-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the original image
    :return img: SimpleImage, the smaller image
    """
    img=SimpleImage(filename)
    small_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(0,img.width, 2):
        for y in range(0, img.height,2):
            old_pixel = img.get_pixel(x,y)
            new_pixel = small_img.get_pixel(x//2,y//2)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    return small_img







def main():
    """
    the program helps resize the image and make it half of the original size.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
