"""
File: blur.py
name: HsuenChi Chiu

-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: The image before blurring process
    :return: the image after blurring for once
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            new_pixel = new_img.get_pixel(x, y)

            # (0,0)
            if x==0 and y== 0:
                origin_pixel = img.get_pixel(x,y)
                right_pixel = img.get_pixel(x + 1, y)
                down_pixel = img.get_pixel(x, y + 1)
                down_right_pixel = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (origin_pixel.red+right_pixel.red+down_pixel.red+down_right_pixel.red)/4
                new_pixel.green=(origin_pixel.green+right_pixel.green+down_pixel.green+down_right_pixel.green)/4
                new_pixel.blue=(origin_pixel.blue+right_pixel.blue+down_pixel.blue+down_right_pixel.blue)/4

            # (w,0) upper right
            elif x == img.width-1  and y == 0:
                origin_pixel = img.get_pixel(x,y)
                left_pixel = img.get_pixel(x - 1, y)
                down_pixel = img.get_pixel(x, y + 1)
                down_left_pixel = img.get_pixel(x - 1, y + 1)
                new_pixel.red = (origin_pixel.red+left_pixel.red+down_pixel.red+down_left_pixel.red)/4
                new_pixel.green = (origin_pixel.green+left_pixel.green+down_pixel.green+down_left_pixel.green)/4
                new_pixel.blue = (origin_pixel.blue+left_pixel.blue+down_pixel.blue+down_left_pixel.blue)/4

            # (0,h) lower left
            elif x ==0 and y == img.height-1:
                origin_pixel = img.get_pixel(x,y)
                up_pixel = img.get_pixel(x, y - 1)
                right_pixel = img.get_pixel(x + 1, y)
                upper_right_pixel = img.get_pixel(x + 1, y - 1)
                new_pixel.red = (origin_pixel.red+up_pixel.red+right_pixel.red+upper_right_pixel.red)/4
                new_pixel.green = (origin_pixel.green+up_pixel.green+right_pixel.green+upper_right_pixel.green)/4
                new_pixel.blue = (origin_pixel.blue+up_pixel.blue+right_pixel.blue+upper_right_pixel.blue)/4

            # (w,h) lower right
            elif x ==img.width-1 and y == img.height-1:
                origin_pixel = img.get_pixel(x,y)
                left_pixel = img.get_pixel(x - 1, y)
                up_pixel = img.get_pixel(x, y - 1)
                upper_left_pixel = img.get_pixel(x-1,y-1)
                new_pixel.red = (origin_pixel.red+left_pixel.red + up_pixel.red + upper_left_pixel.red) / 4
                new_pixel.green = (origin_pixel.green+left_pixel.green + up_pixel.green + upper_left_pixel.green) / 4
                new_pixel.blue = (origin_pixel.blue+left_pixel.blue + up_pixel.blue + upper_left_pixel.blue) / 4

            # the upper line
            elif y == 0:
                origin_pixel = img.get_pixel(x,y)
                left_pixel = img.get_pixel(x - 1, y)
                down_left_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)
                down_right_pixel = img.get_pixel(x + 1, y + 1)
                right_pixel = img.get_pixel(x + 1, y)
                new_pixel.red = (origin_pixel.red+left_pixel.red+down_left_pixel.red+down_pixel.red+down_right_pixel.red+right_pixel.red)/6
                new_pixel.green = (origin_pixel.green+left_pixel.green+down_left_pixel.green+down_pixel.green+down_right_pixel.green+right_pixel.green)/6
                new_pixel.blue =(origin_pixel.blue+left_pixel.blue+down_left_pixel.blue+down_pixel.blue+down_right_pixel.blue+right_pixel.blue)/6

            # the bottom line
            elif y == img.height-1:
                origin_pixel = img.get_pixel(x,y)
                left_pixel = img.get_pixel(x - 1, y)
                right_pixel = img.get_pixel(x + 1, y)
                upper_right_pixel = img.get_pixel(x + 1, y - 1)
                up_pixel = img.get_pixel(x, y - 1)
                upper_left_pixel = img.get_pixel(x-1,y-1)

                new_pixel.red = (origin_pixel.red+left_pixel.red+upper_left_pixel.red+up_pixel.red+upper_right_pixel.red+right_pixel.red)/6
                new_pixel.green = (origin_pixel.green+left_pixel.green+upper_left_pixel.green+up_pixel.green+upper_right_pixel.green+right_pixel.green)/6
                new_pixel.blue = (origin_pixel.blue+left_pixel.blue+upper_left_pixel.blue+up_pixel.blue+upper_right_pixel.blue+right_pixel.blue)/6

            # the line on the left
            elif x==0:
                origin_pixel = img.get_pixel(x,y)

                down_pixel = img.get_pixel(x, y + 1)
                down_right_pixel = img.get_pixel(x + 1, y + 1)
                right_pixel = img.get_pixel(x + 1, y)
                upper_right_pixel = img.get_pixel(x + 1, y - 1)
                up_pixel = img.get_pixel(x, y - 1)
                new_pixel.red = (origin_pixel.red+up_pixel.red+upper_right_pixel.red+right_pixel.red+down_right_pixel.red+down_pixel.red)/6
                new_pixel.green = (origin_pixel.green+up_pixel.green+upper_right_pixel.green+right_pixel.green+down_right_pixel.green+down_pixel.green)/6
                new_pixel.blue = (origin_pixel.blue+up_pixel.blue+upper_right_pixel.blue+right_pixel.blue+down_right_pixel.blue+down_pixel.blue)/6

            # the line on the right
            elif x == img.width-1:
                origin_pixel = img.get_pixel(x,y)

                left_pixel = img.get_pixel(x - 1, y)
                down_left_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)
                up_pixel = img.get_pixel(x, y - 1)
                upper_left_pixel = img.get_pixel(x-1,y-1)
                new_pixel.red = (origin_pixel.red+up_pixel.red+upper_left_pixel.red+left_pixel.red+down_left_pixel.red+down_pixel.red)/6
                new_pixel.green = (origin_pixel.green+up_pixel.green+upper_left_pixel.green+left_pixel.green+down_left_pixel.green+down_pixel.green)/6
                new_pixel.blue = (origin_pixel.blue+up_pixel.blue + upper_left_pixel.blue + left_pixel.blue + down_left_pixel.blue + down_pixel.blue) / 6

            # pixels in the middle
            else:
                origin_pixel = img.get_pixel(x,y)
                left_pixel = img.get_pixel(x - 1, y)
                down_left_pixel = img.get_pixel(x - 1, y + 1)
                down_pixel = img.get_pixel(x, y + 1)
                down_right_pixel = img.get_pixel(x + 1, y + 1)
                right_pixel = img.get_pixel(x + 1, y)
                upper_right_pixel = img.get_pixel(x + 1, y - 1)
                up_pixel = img.get_pixel(x, y - 1)
                upper_left_pixel = img.get_pixel(x-1,y-1)
                new_pixel.red = (origin_pixel.red+left_pixel.red+down_left_pixel.red+down_pixel.red+down_right_pixel.red+right_pixel.red+upper_right_pixel.red+up_pixel.red
                                 +upper_left_pixel.red)/9
                new_pixel.green = (origin_pixel.green+left_pixel.green + down_left_pixel.green + down_pixel.green + down_right_pixel.green + right_pixel.green + upper_right_pixel.green + up_pixel.green
                                            + upper_left_pixel.green) / 9
                new_pixel.blue = (origin_pixel.blue+left_pixel.blue + down_left_pixel.blue + down_pixel.blue + down_right_pixel.blue + right_pixel.blue + upper_right_pixel.blue + up_pixel.blue
                                              + upper_left_pixel.blue) / 9
    return new_img




def main():
    """
    The program helps making the image blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
