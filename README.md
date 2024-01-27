# Image Colors Palette Generator

This project is a simple web application that generates the top colors from an uploaded image and displays them along with the image itself. The application is built using the Flask framework and utilizes the Pillow library for image processing.

## Table of Contents

-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)


## Installation

To run the application locally, follow these steps:

1. Clone the repository:
```
git clone https://github.com/your-username/image-colors-palette-generator.git
```
2. Navigate to the project directory:
```
cd image-colors-palette-generator
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the Flask application: `python run.py`
2. Open your web browser and go to http://localhost:5000.
3. Upload an image using the provided form, and the application will display the top 10 most common colors along with their color codes and percentages.

## Project Structure

The project is organized as follows:

-   run.py: Main script to run the Flask application.
-   app/static: Static files including images and temporary uploads.
-   app/templates: HTML templates for rendering the web pages.
-   app/routes.py: Flask routes and logic for handling requests.
-   app/logic.py: Image processing logic for extracting top colors.
-   config.py: Configuration class for the Flask application.
-   requirements.txt: List of dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to explore and modify the code to suit your needs!
