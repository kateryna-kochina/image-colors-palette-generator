import os
from flask import Blueprint, Flask, render_template, request
from config import Config
from .logic import get_top_colors


def create_app():
    '''
    Create and configure the Flask application.

    Returns:
        Flask: The configured Flask application instance.
    '''
    app = Flask(__name__)

    # Register the main blueprint
    from .routes import bp
    app.register_blueprint(bp)

    return app


bp = Blueprint('main', __name__)


@bp.route('/', methods=['POST', 'GET'])
def home():
    '''
    Handle requests to the home route ('/').

    Returns:
        str: Rendered HTML template with top colors and image path.
    '''
    if request.method == 'POST':
        try:
            # Handle file upload
            new_image = request.files['image']

            # Save the new image to a temporary directory
            new_image_path = os.path.join(
                Config.TEMP_IMG_PATH, new_image.filename)
            new_image.save(new_image_path)

            # Get top colors from the new image
            top_colors = get_top_colors(new_image_path)

            # Update the image path to the new image
            img_path = os.path.join('temp', new_image.filename)

            return render_template('index.html', top_colors=top_colors, img_path=img_path)

        except KeyError:
            print("KeyError: 'image' not found in request.files")

    # Default image path and top colors for initial rendering
    img_path = Config.DEFAULT_IMG_PATH
    top_colors = get_top_colors(f'app/static/{img_path}')

    return render_template('index.html', top_colors=top_colors, img_path=img_path)
