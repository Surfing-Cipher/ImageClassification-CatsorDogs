# Binary Image Classification: Cats or Dogs

This project is a web-based **binary image classifier** that determines whether an uploaded image contains a **cat** or a **dog**. Built with **Flask** and powered by a pre-trained **TensorFlow/Keras** model, it demonstrates a complete MLOps workflow, including **Docker containerization** and **automated CI/CD with GitHub Actions**.

-----

## ✨ Features

  * **Web Interface:** A simple and intuitive Flask web application for uploading images.
  * **Real-time Classification:** Upload an image and get an instant prediction (Cat or Dog).
  * **Deep Learning Model:** Utilizes an EfficientNetB0 model, fine-tuned for cat and dog classification.
  * **Containerized Application:** Packaged as a Docker image for consistent deployment across environments.
  * **Automated CI/CD:** A GitHub Actions workflow automatically builds and pushes the Docker image to Docker Hub on every code push to the `main` branch.

-----

## 🛠️ Technologies Used

  * **Backend:** Python 3.10+
  * **Web Framework:** Flask
  * **Machine Learning:** TensorFlow, Keras, NumPy, OpenCV, Pillow, Albumentations
  * **Containerization:** Docker
  * **CI/CD:** GitHub Actions
  * **Model Hosting:** Docker Hub

-----

## 🚀 How to Run Locally

You have two options to run this project on your local machine: without Docker (for development) or with Docker (for containerized testing).

### Option 1: Running Locally (Development Mode)

This method is ideal for developing and testing the application directly on your machine.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Surfing-Cipher/ImageClassification-CatsorDogs.git
    cd ImageClassification-CatsorDogs
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**

    ```bash
    flask run
    ```

    The application will typically be accessible at `http://127.0.0.1:5000/` or `http://localhost:5000/`.

5.  **Deactivate the virtual environment (when done):**

    ```bash
    deactivate
    ```

### Option 2: Running with Docker (Local Container)

This method allows you to run the application inside a Docker container, mimicking how it would be deployed in a production environment.

1.  **Ensure Docker is installed:**
    Make sure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine) installed and running on your system.

2.  **Build the Docker image locally:**
    Navigate to the project's root directory (where the `Dockerfile` is located) and run:

    ```bash
    docker build -t cats-dogs-classifier .
    ```

    This command builds the Docker image and tags it as `cats-dogs-classifier`.

3.  **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 cats-dogs-classifier
    ```

      * `-p 5000:5000`: This maps port 5000 on your local machine to port 5000 inside the Docker container, allowing you to access the app.

4.  **Access the application:**
    Open your web browser and go to `http://localhost:5000/`.

-----

## ☁️ CI/CD Pipeline (GitHub Actions & Docker Hub)

This project features an automated CI/CD pipeline set up using GitHub Actions.

  * **Workflow File:** The pipeline is defined in `.github/workflows/main.yml`.
  * **Triggers:** The workflow automatically runs on every `push` to the `main` branch and on every `pull_request` targeting the `main` branch.
  * **Steps:**
    1.  **Checkout Code:** Fetches the latest code from the repository.
    2.  **Docker Login:** Authenticates with Docker Hub using securely stored [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) (`DOCKER_USERNAME` and `DOCKER_TOKEN`).
    3.  **Build & Push:** Uses Docker Buildx to build the Docker image from the `Dockerfile` and push it to Docker Hub. The image is tagged with `latest` and also with the Git commit SHA for specific versioning. **Pushing only happens on pushes to `main` branch.**
  * **Docker Hub Repository:** The built Docker images are stored in the [surfingcipher732/cats\_dogs\_classifier](https://www.google.com/search?q=https://hub.docker.com/r/surfingcipher732/cats_dogs_classifier) repository on Docker Hub.

-----

## 📂 Project Structure

```
ImageClassification-CatsorDogs/
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI/CD workflow
├── static/                 # Static assets (CSS, JS, images for frontend)
│   └── css/
│   └── img/
│   └── ...
├── templates/              # HTML templates for Flask
│   └── index.html
├── your_model_files/       # Directory containing the Keras model
│   └── efficientnetb0_cats_dogs_classifier.keras
├── Dockerfile              # Instructions for building the Docker image
├── app.py                  # Main Flask application file
├── model_loader.py         # Handles loading and prediction with the ML model
├── requirements.txt        # Python dependencies
└── README.md               # This README file
```

-----

## 🧠 Model Details

The image classification is performed using an **EfficientNetB0** model, pre-trained on ImageNet and fine-tuned for binary classification (Cat vs. Dog). The model is saved in the Keras native format (`.keras`) and loaded via `model_loader.py`.

-----

## 🚀 Future Enhancements

  * **Deployment:** Deploy the Docker image to a cloud platform like Google Cloud Run, Render, or AWS App Runner for public access.
  * **User Feedback:** Implement a system for users to provide feedback on predictions to improve model accuracy.
  * **Performance Monitoring:** Add logging and monitoring for model inference times and application performance.
  * **Model Retraining Pipeline:** Implement a pipeline to periodically retrain the model with new data.
  * **UI/UX Improvements:** Enhance the web interface for a more polished user experience.

-----

## 🤝 Contributing

Contributions are welcome\! If you have suggestions or improvements, please:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'feat: Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

-----

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
