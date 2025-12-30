import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()

if input_ext not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
if output_ext not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid output")
if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size
photo = ImageOps.fit(input_image, size)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])
