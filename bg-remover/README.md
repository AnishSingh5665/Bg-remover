# Background Removal Flask Application

This Flask application allows users to upload an image, remove its background, and download the processed image. It supports common image formats such as JPEG and PNG.

## Features

- **Upload an image** with background.
- **Remove the background** from the image.
- **Download the processed image** with the background removed.

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of Flask and Python.

## Installation

**Clone the Repository**:
   
   ```bash
   git clone <repository-url>
   cd <repository-directory>

Create and Activate a Virtual Environment (Recommended)

Create the Virtual Environment:

bash
Copy code
python -m venv .venv
Activate the Virtual Environment:

On Windows:

bash
Copy code
.venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source .venv/bin/activate

Install Dependencies

Create a requirements.txt file in the project root directory with the following content:

text
Copy code
Flask
Pillow
rembg
Install the dependencies using pip:

bash
Copy code
pip install -r requirements.txt

Running the Application

Ensure Folders Exist: The application uses input and output folders. These will be created automatically if they don't exist.

Start the Flask Application:

bash
Copy code
python app.py
The application will start and listen on port 7777 by default. You can access it in your web browser at http://127.0.0.1:7777.

API Endpoints

Upload Image:

URL: /upload
Method: POST
Description: Upload an image to remove its background.
Parameters: file (multipart/form-data)
Response: Redirects to the /download/<filename> endpoint.
Download Processed Image:

URL: /download/<filename>
Method: GET
Description: Download the processed image with the background removed.
Parameters: filename (URL parameter)
Response: The processed image file.

Example Usage

Uploading an Image:

Use a tool like Postman or an HTML form to send a POST request to /upload with an image file.
Downloading the Processed Image:

After uploading, you will be redirected to a URL like /download/<filename> where <filename> is the name of the processed image.

Libraries Used:

Flask: A lightweight web framework for Python.
Pillow (PIL): Python Imaging Library for image processing.
rembg: Library for background removal from images.
