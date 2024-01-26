from collections import Counter
from PIL import Image
from operator import itemgetter

def rgb_to_hex(rgb):
    # Convert RGB to hexadecimal
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
    return hex_color


def get_top_colors(image_path, num_colors=10):
    # Load the image
    image = Image.open(image_path)

    # Convert image to RGB
    image = image.convert('RGB')

    # Get the image pixels
    pixels = list(image.getdata())

    # Count the occurrences of each color
    color_counts = Counter(pixels)

    # Calculate the total number of pixels in the image
    total_pixels = len(pixels)

    # Calculate the percentage of each color's presence
    color_percentages = [(rgb_to_hex(color), round(count / total_pixels * 100, 6)) for color, count in color_counts.items()]

    # Get the top N colors, sort descending by color percentage
    top_colors = sorted(color_percentages, key=itemgetter(1), reverse=True)[:num_colors]

    return top_colors
