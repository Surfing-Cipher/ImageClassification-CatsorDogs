# your_flask_app/Dockerfile

# Use a slim Python base image for a smaller final image size
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
# This means if requirements.txt doesn't change, these layers are cached
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir: Reduces image size by not storing pip's cache
# -r requirements.txt: Installs packages from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
# This includes app.py, model_loader.py, static/, templates/, and your_model_files/
COPY . .

# Ensure the model file is in the correct place inside the container
# The model_loader.py expects it in 'your_model_files/efficientnetb0_cats_dogs_classifier.keras'
# The COPY . . command above will handle this if your local structure is correct.

# Set Flask environment variables for production
# FLASK_APP: tells Flask which file to run
# FLASK_ENV: sets Flask to production mode (disables debug, enables optimizations)
# PYTHONUNBUFFERED: ensures Python output (e.g., print statements) is not buffered
ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    PYTHONUNBUFFERED=1

# Expose the port Flask runs on (default is 5000)
EXPOSE 5000

# Command to run the Flask application when the container starts
# --host=0.0.0.0 makes the app accessible from outside the container
CMD ["flask", "run", "--host=0.0.0.0"]