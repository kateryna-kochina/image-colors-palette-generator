import os
from collections import Counter
from operator import itemgetter
from PIL import Image


def rgb_to_hex(rgb):
    '''
    Convert RGB values to hexadecimal representation.

    Args:
        rgb (tuple): A tuple containing three integers representing the Red, Green, and Blue values.

    Returns:
        str: Hexadecimal representation of the RGB values.
    '''
    hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
    return hex_color


def get_top_colors(image_path, num_colors=10):
    '''
    Get the top N colors in an image based on their occurrence percentages.

    Args:
        image_path (str): The path to the image file.
        num_colors (int, optional): The number of top colors to retrieve. Defaults to 10.

    Returns:
        list: A list of tuples containing the top N colors and their occurrence percentages.
              Each tuple has the format (hex_color, percentage).
    '''
    try:
        # Check if the file exists
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"The file '{image_path}' does not exist.")

        # Check if the file type is supported
        _, file_extension = os.path.splitext(image_path)
        supported_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        if file_extension.lower() not in supported_extensions:
            raise ValueError(f"Unsupported file type: {file_extension}. Supported types are {
                             ', '.join(supported_extensions)}.")

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
        color_percentages = [(rgb_to_hex(color), round(
            count / total_pixels * 100, 6)) for color, count in color_counts.items()]

        # Get the top N colors, sort descending by color percentage
        top_colors = sorted(color_percentages, key=itemgetter(
            1), reverse=True)[:num_colors]

        return top_colors

    except Exception as e:
        print(f"Error: {e}")
        return None
