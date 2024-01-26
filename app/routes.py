from flask import Blueprint, Flask, render_template, request
from config import Config
from .logic import get_top_colors
import os


def create_app():
    app = Flask(__name__)

    # Register the main blueprint
    from .routes import bp
    app.register_blueprint(bp)

    return app


bp = Blueprint('main', __name__)


@bp.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print("Form Data:", request.form)
        print("Files:", request.files)
        print("Request Data:", request)

        try:
            # Handle file upload
            new_image = request.files['image']
        
            # Save the new image to a temporary directory
            temp_path = 'app/static/temp'
            new_image_path = os.path.join(temp_path, new_image.filename)
            new_image.save(new_image_path)
            
            # Get top colors from the new image
            top_colors = get_top_colors(new_image_path)

            # Update the image path to the new image
            img_path = f'temp/{new_image.filename}'

            return render_template('index.html', top_colors=top_colors, img_path=img_path)

        except KeyError:
            print("KeyError: 'image' not found in request.files")
    
    img_path = Config.DEFAULT_IMG_PATH
    top_colors = get_top_colors(f'app/static/{img_path}')

    return render_template('index.html', top_colors=top_colors, img_path=img_path)
