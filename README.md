# ElegantVision

Welcome to **ElegantVision** – where Django meets computer vision in the coolest way possible! This project is a playful exploration of machine learning, built with a dash of humor and a sprinkle of modern design. It's not just about code; it's about having fun while pushing the boundaries of what a web app can do.

👉 **Live Demo:** [https://elegantvision.onrender.com/](https://elegantvision.onrender.com/)

## 🚀 What is ElegantVision?

ElegantVision is a Django-powered web application that demonstrates computer vision using a pre-trained **EfficientNetB0** model. In plain terms, you can upload an image (via drag-and-drop or a neat "Browse" option), and our friendly model will tell you what it sees. It’s a neat experiment with machine learning that’s as eye-catching as it is clever!

## ✨ Features

- ✅ **Computer Vision Magic** – Uses EfficientNetB0 to classify images because… well, why not?  
- ✅ **Slick, Modern UI** – A visually stunning experience with glowing effects and smooth transitions.  
- ✅ **Interactive Feedback** – Real-time predictions with a fancy loading spinner.  
- ✅ **Drag-and-Drop Upload** – Supports both drag-and-drop and traditional file browsing.  
- ✅ **Built with My Buddy ChatGPT 🤖** – Because AI teamwork makes the dream work!  

## 🛠️ Tech Stack

### 🔹 Backend:
- Django 5.1.6
- Python 3.x
- Gunicorn (for production)

### 🔹 Machine Learning:
- TensorFlow & Keras (EfficientNetB0 pretrained on ImageNet)
- Pillow (image processing)

### 🔹 Frontend:
- HTML, CSS, JavaScript
- Font Awesome icons
- Custom animations & effects

### 🔹 Static Files:
- WhiteNoise (serves static assets efficiently)

### 🔹 Deployment:
- **Render**: Hosted with a **Procfile**:
  web: gunicorn ElegantVision.wsgi

## 🛠️ Installation

1️⃣ **Clone the Repository:**  
```
   git clone https://github.com/ali-sehran/ElegantVision.git  
   cd ElegantVision  
```
2️⃣ **Create a Virtual Environment:**  
```
   python3 -m venv .venv  
   source .venv/bin/activate  
```
3️⃣ **Install Dependencies:**  
```
   pip install -r requirements.txt  
```
4️⃣ **Apply Migrations:**  
```
   python manage.py migrate  
```

5️⃣ **Collect Static Files (for production):**  
```
   python manage.py collectstatic --noinput  
```

6️⃣ **Run the Development Server:**  
```
   python manage.py runserver  
```
   Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser and enjoy!

## 🌍 Deployment on Render

To deploy ElegantVision on **Render**, follow these steps:

- Push your code to a Git repository.
- Create a **New Web Service** on Render.
- Connect your repository and let Render detect your **Procfile**.
- Set your **Environment Variables** (`DEBUG=False`, `DJANGO_SECRET_KEY`, `ALLOWED_HOSTS`).
- Deploy! Your app will be live at **`https://your-app-name.onrender.com/`**.

## 🎉 Credits & Disclaimer

ElegantVision was built as a fun experiment to explore the **Django framework and computer vision**.  
A big shout-out to my coding partner, **ChatGPT**, for all the collaboration and laughs along the way! 😎💡  

📢 **Note:** The EfficientNetB0 model used in this demo isn’t our creation – it’s a fantastic tool from the deep learning world, used here purely for **experimentation** and **demonstration purposes**.

