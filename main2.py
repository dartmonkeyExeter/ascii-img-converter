import cv2
from PIL import Image, ImageOps
from math import trunc
import os
from time import sleep

ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '%', '@', '#']

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) and frame count of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop through all frames in the video
    for frame_number in range(frame_count):
        # Read the frame
        ret, frame = cap.read()

        # Save the frame as an image
        frame_filename = f"{output_folder}/frame_{frame_number:04d}.jpg"
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()

# Example usage
video_path = 'C:/Users/aaron/Desktop/bad apple/video.mp4'
output_folder = 'C:/Users/aaron/Desktop/bad apple/frames'
extract_frames(video_path, output_folder)

files = os.listdir(output_folder)

for file_name in files:
    file_path = os.path.join(output_folder, file_name)
    if os.path.isfile(file_path):
        with Image.open(file_path) as img:
            size = list(img.size)
            size[0] = trunc(size[0] / 25)
            size[1] = trunc(size[1] / 25)
            ImageOps.cover(img, tuple(size)).save("resized.jpg")
        im = Image.open("resized.jpg")
        im = ImageOps.autocontrast(im)
        pixels = list(im.getdata())

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
        sleep(0.016)
# Your logic for processing each frame goes inside the loop
