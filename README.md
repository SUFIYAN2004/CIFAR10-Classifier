# 🚀 CIFAR10-Classifier

A Deep Learning project that trains a Convolutional Neural Network (CNN) to recognize images across 10 different categories and deploys the model via a user-friendly Streamlit web app.

## 📺 Video Tutorial
This project is part of a step-by-step tutorial on my YouTube channel: **[Suflearning](https://youtube.com/@suflearning)**. 
Watch the video to see how we build this from scratch!

## 📊 About the Dataset
We use the **CIFAR-10 Dataset**, a famous collection of 60,000 small images. The AI is trained to classify images into these 10 categories:
* ✈️ **Airplane**
* 🚗 **Automobile**
* 🐦 **Bird**
* 🐱 **Cat**
* 🦌 **Deer**
* 🐶 **Dog**
* 🐸 **Frog**
* 🐴 **Horse**
* 🚢 **Ship**
* 🚚 **Truck**

## 🛠️ Tech Stack
- **Python**: The core language.
- **TensorFlow/Keras**: For building and training the CNN brain.
- **Streamlit**: For the web application frontend.
- **PIL & NumPy**: For image processing and math.

## 📁 Repository Structure
- `app.py`: The Streamlit application script.
- `cifar10_model.keras`: The pre-trained model file.
- `requirements.txt`: Necessary libraries to run the project.

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone [https://github.com/YOUR_USERNAME/CIFAR10-Classifier.git](https://github.com/YOUR_USERNAME/CIFAR10-Classifier.git)
cd CIFAR10-Classifier
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the App
```bash
streamlit run app.py
```
### 📈 Model Performance
The model achieves approximately 71% accuracy. While it is great at distinguishing between distinct shapes like planes and trucks, it sometimes confuses similar shapes (like cats and dogs) due to the low 32x32 resolution.
### Happy Learning with <a href="https://www.youtube.com/@suflearning">Suflearning </a>
---
### **Final Pro-Tips for your GitHub:**
* **The Model File:** Because `.keras` files can be large, just make sure it uploads fully before you close the tab.
* **The Thumbnail:** If you want to make it look even better, you can add a screenshot of your working Streamlit app to the README later.

**You’re all set for Suflearning! Your viewers are going to love having all the files ready for them. Ready to record the intro now?**
