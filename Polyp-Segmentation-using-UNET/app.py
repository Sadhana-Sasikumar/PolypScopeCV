from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the uploaded image file
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            # Save the uploaded file to a location
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            # Perform segmentation on the uploaded image
            # (Replace this with your segmentation logic)
            segmented_image_path = 'static/results/Segmented_image.png'

            # Pass the path to the segmented image to the result page
            return render_template('result.html', segmented_image=segmented_image_path)
    else:
        # Handle GET request
        # Pass the path to the default segmented image to the result page
        segmented_image_path = 'static/results/Segmented_image.png'
        return render_template('result.html', segmented_image=segmented_image_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
