# your_flask_app/app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from model_loader import predict_image, CLASS_NAMES # Import our prediction logic

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here' # Change this to a random string!
# It's good practice to set a secret key for security in Flask applications,
# especially if using sessions or flash messages.

# Configuration for file uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path) # Save the uploaded file temporarily

            # Get prediction using your model_loader
            predicted_class, confidence = predict_image(file_path)

            # Pass prediction results and image path to result template
            return render_template('result.html', 
                                   prediction=predicted_class, 
                                   confidence=confidence, 
                                   image_url=url_for('static', filename=f'uploads/{filename}'))
        else:
            flash('Allowed image types are png, jpg, jpeg, gif')
            return redirect(request.url)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # Run in debug mode for development (auto-reloads on code changes)