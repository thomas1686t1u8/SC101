"""
File: best_photoshop_award.py
Name: Thomas
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


THRESHOLD = 1.15  # Controls the threshold of detecting green screen pixel.


BLACK_PIXEL = 50  # Controls the upper bound for black pixel.


def main():
    """
    創作理念：
    Escape 逃
    人生就是不斷地逃
    逃歸逃
    別忘了帶著貓貓一起逃

    This program photoshop two image together!
    """
    fg = SimpleImage('image_contest/photo2.jpg')
    bg = SimpleImage('image_contest/background.jpg')
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(background, front):
    for y in range(front.height):  # Loop over the image.
        for x in range(front.width):
            pixel_front = front.get_pixel(x, y)
            avg = (pixel_front.red + pixel_front.blue + pixel_front.green) // 3
            total = pixel_front.red + pixel_front.blue + pixel_front.green
            if pixel_front.green > avg * THRESHOLD and total > BLACK_PIXEL:  # Judge whether the pixel is green enough.
                pixel_bg = background.get_pixel(x, y)  # Replace the green pixel.
                pixel_front.red = pixel_bg.red
                pixel_front.blue = pixel_bg.blue
                pixel_front.green = pixel_bg.green
    return front


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
