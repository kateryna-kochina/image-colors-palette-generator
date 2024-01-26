from collections import Counter
from PIL import Image


def get_top_colors(image_path, num_colors=10):
    # Load the image
    image = Image.open(image_path)

    # Convert image to RGB (if not already in RGB mode)
    image = image.convert('RGB')

    # Get the image pixels
    pixels = list(image.getdata())

    # Count the occurrences of each color
    color_counts = Counter(pixels)

    # Get the top 10 colors
    top_colors = color_counts.most_common(num_colors)

    return top_colors
