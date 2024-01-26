from flask import Blueprint, Flask, redirect, render_template, request, url_for
from .logic import get_top_colors
from config import Config


def create_app():
    app = Flask(__name__)

    # Register the main blueprint
    from .routes import bp
    app.register_blueprint(bp)

    return app


bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    img_path = Config.DEFAULT_IMG_PATH
    top_colors = get_top_colors(img_path)

    return render_template('index.html', top_colors=top_colors)
