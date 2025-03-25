## 🎨 AI-Image-Colorization  

### 📌 Project Description  
AI-Image-Colorization is a deep learning-based application that converts black-and-white images into colored versions using a Generative Adversarial Network (GAN). This project uses a U-Net-based Generator and a Discriminator to generate realistic colorized images.  

---

## ✨ Features  
✅ Deep Learning-based image colorization using GANs  
✅ Supports black-and-white images of different resolutions  
✅ Uses TensorFlow/Keras for training and inference  
✅ Works on CPU and GPU (optimized for TPU training)  
✅ Easy-to-use FastAPI backend for inference  
✅ Frontend built with HTML, CSS, and JavaScript for real-time uploads  

---

## 🚀 Installation  

### 🔹 Clone the Repository  
```bash
git clone https://github.com/dev-3119/AI-Image-Colorization.git
cd AI-Image-Colorization  
```

### 🔹 Install Dependencies  
For the backend:  
```bash
pip install -r requirements.txt  
```
For the frontend, no additional dependencies are required.

---

## 🎨 Usage  

### 🔹 Download the Pre-trained Model  
Download the model from the following link and place it in the project directory:
[Download Model](https://drive.google.com/file/d/1hpxOuYpmorB6BaiAs4OzMV6yFRHYELev/view?usp=sharing)
Model Name: test_gan_1.h5

### 🔹 Run the Backend  
```bash  
uvicorn app:app --host 0.0.0.0 --port 8000  
```
The API will be available at `http://localhost:8000`.  

### 🔹 Run the Frontend  
Simply open `index.html` in a browser.  

### 🔹 Upload an Image  
1. Select a black-and-white image.  
2. Click "Colorize".  
3. The model processes the image and returns a colorized version.  

---

## 🎯 Training the Model  

To train your own colorization model:  
```bash
python GAN.ipynb  
```
Modify `GAN.ipynb` to customize training parameters like epochs, batch size, etc.

---

### 🔹 Deploy Backend on Render  
1. Push the backend code to GitHub.  
2. Deploy using `uvicorn` as the start command.  

---

### 🎯 Future Enhancements  
🔹 Add support for video colorization  
🔹 Improve color accuracy using advanced GAN architectures  
🔹 Convert model into a TensorFlow Lite version for mobile apps

