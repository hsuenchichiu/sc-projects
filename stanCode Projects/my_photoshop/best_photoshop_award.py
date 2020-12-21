"""
File: best_photoshop_award.py
name: HsuenChi Chiu
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage
THRESHOLD = 1.25
BLACK_PIXEL = 125



def main():
    """
    I want to live in a pineapple under the sea.
    """
    fg = SimpleImage('image_contest/me.jpg')
    bg = SimpleImage('image_contest/house.png')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()

def combine(back, me):
    """
    : param1 back: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels background image
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


if __name__ == '__main__':
    main()
