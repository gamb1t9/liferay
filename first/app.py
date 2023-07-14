from flask import Flask, render_template, request
import os
from PIL import Image

app = Flask('liferay-hw')

# Set the path for uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the maximum size ratio for resizing images
MAX_SIZE_RATIO = 0.5

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if file was submitted
        if 'image' in request.files:
            image = request.files['image']
            if image.filename != '':
                # Save the uploaded image
                filename = image.filename
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image.save(image_path)

                # Get image information
                image_size_mb = get_file_size_mb(image_path)
                image_width, image_height = get_image_size(image_path)

                # Resize image if necessary
                resized = False
                window_width, window_height = get_window_size()
                max_image_width = window_width * MAX_SIZE_RATIO
                if image_width > max_image_width:
                    resized_image_path = resize_image(image_path, max_image_width)
                    if resized_image_path:
                        image_path = resized_image_path
                        image_width, image_height = get_image_size(image_path)
                        resized = True

                # Render the index template with the container creation date, uploaded image, and image information
                return render_template("index.html", creation_date=get_container_creation_date(), uploaded_image=filename, image_size_mb=image_size_mb, image_width=image_width, image_height=image_height, resized=resized)

    # Render the index template with the container creation date
    return render_template("index.html", creation_date=get_container_creation_date())

def get_container_creation_date():
    # Read the container creation date from the file
    creation_date_file = "creation_date"
    with open(creation_date_file, "r") as f:
        creation_date = f.read().strip()

    return creation_date

def get_file_size_mb(file_path):
    size_in_bytes = os.path.getsize(file_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    return "{:.2f} MB".format(size_in_mb)

def get_image_size(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def get_window_size():
    # Assuming a default Full HD (1920x1080) resolution
    return 1920, 1080

def resize_image(image_path, max_width):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if width > max_width:
                new_width = max_width
                new_height = int((new_width / width) * height)
                resized_img = img.resize((new_width, new_height))
                resized_image_path = image_path.replace(".", "_resized.")
                resized_img.save(resized_image_path)
                return resized_image_path
    except Exception as e:
        print(f"Error occurred while resizing image: {e}")
    return None

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
