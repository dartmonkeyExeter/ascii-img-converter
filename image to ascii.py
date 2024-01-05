from PIL import Image, ImageOps
from math import trunc

ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '%', '@', '#']

with Image.open("test.jpg") as img:
    size = list(img.size)
    size[0] = trunc(size[0] / 25)
    size[1] = trunc(size[1] / 25)
    ImageOps.cover(img, tuple(size)).save("resized.jpg")

# Open the image
im = Image.open("resized.jpg")

# Adjust the contrast of the image
im = ImageOps.autocontrast(im)

# Get a list of all the pixel values in the image
pixels = list(im.getdata())

# Create a 2D array to store the brightness of each pixel
brightness = [[0 for x in range(im.width)] for y in range(im.height)]

# Loop through each pixel and calculate its brightness
for i in range(len(pixels)):
    # Calculate the brightness of the pixel
    r, g, b = pixels[i]
    brightness[i // im.width][i % im.width] = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

final_output = []

for row in brightness:
    row_output = []
    for cell in row:
        if cell > 230:
            row_output.append("#")
        elif cell > 205:
            row_output.append("@")
        elif cell > 179:
            row_output.append("%")
        elif cell > 154:
            row_output.append("*")
        elif cell > 128:
            row_output.append("+")
        elif cell > 102:
            row_output.append("=")
        elif cell > 77:
            row_output.append("-")
        elif cell > 51:
            row_output.append(":")
        elif cell > 26:
            row_output.append(".")
        else:
            row_output.append (" ")
    final_output.append(row_output)


for i in final_output:
    print(" ".join(i))
