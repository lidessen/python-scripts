def process_photo(file):
    """convert image to jpg format"""
    from PIL import Image
    image = Image.open(file)
    width, height = image.size
    image = image.crop((0, 0, width, width / 290 * 418))
    image.thumbnail((290, 418))
    image.save("./export.jpg", "JPEG", quality=90)


import sys

process_photo(sys.argv[1])
