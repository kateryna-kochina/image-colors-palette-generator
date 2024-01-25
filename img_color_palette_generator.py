from flask import Flask, render_template, request
from PIL import Image
from collections import Counter
import io


app = Flask(__name__)


def get_top_colors(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB
    rgb_image = image.convert("RGB")

    # Get all pixel colors
    colors = list(rgb_image.getdata())

    # Count occurrences of each color
    color_counter = Counter(colors)

    # Get the top 10 most common colors
    top_colors = color_counter.most_common(10)

    return top_colors


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded image
        uploaded_file = request.files['image']

        if uploaded_file:
            # Get the file name
            file_name = uploaded_file.filename

            return render_template('selected_file.html', file_name=file_name)

        if uploaded_file.filename != '':
            # Read the image file
            image_data = uploaded_file.read()

            # Analyze the image and get the top colors
            top_colors = get_top_colors(io.BytesIO(image_data))

            return render_template('result.html', top_colors=top_colors)

    return render_template('index.html', file_name=None)


if __name__ == '__main__':
    app.run(debug=True)
