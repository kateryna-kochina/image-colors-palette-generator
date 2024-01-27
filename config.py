class Config:
    '''
    Configuration class for the Flask application.

    Attributes:
        DEFAULT_IMG_PATH (str): Default path for the image used at the start of the application and in case of missing or invalid images.
        TEMP_IMG_PATH (str): Path to the temporary directory for storing uploaded images.
    '''

    DEFAULT_IMG_PATH = 'assets/img/default-image.jpg'
    TEMP_IMG_PATH = 'app/static/temp'
