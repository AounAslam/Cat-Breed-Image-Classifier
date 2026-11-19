# 🐱 Cat-Breed-Image-Classifier

A deep learning image classification model that identifies the breed of a cat from a photo. The model was trained using **Google Teachable Machine** and exported in **Keras (TensorFlow)** format for use in Python.

## 🐾 Supported Breeds

The model can classify the following 4 cat breeds:

| # | Breed |
|---|-------|
| 0 | American Shorthair |
| 1 | Persian Cat |
| 2 | Abyssinian |
| 3 | Siamese Cat |

## 📁 Project Files

| File | Description |
|------|-------------|
| `keras_model.h5` | Trained Keras model |
| `labels.txt` | Class labels |
| `main.py` | Python script to run predictions |
| `requirements.txt` | Required Python libraries |

## ⚙️ Installation

1. Clone this repository:
```bash
git clone https://github.com/AounAslam/cat-breed-classifier-.git
cd cat-breed-classifier-
```

2. Install the required libraries:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Put the cat image you want to test in the project folder (e.g. `test.jpg`).
2. Run the script:
```bash
python main.py
```
3. ## 📸 Example Output <img width="180" height="304" alt="image" src="https://github.com/user-attachments/assets/98ac0cb0-683f-4c97-b718-46f2366a48c2" />


```
Class: Abyssinian
Confidence: 100%
```

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pillow
- Google Teachable Machine

## 📌 Notes

- Input images are resized to **224x224** pixels.
- For best results, use clear photos where the cat's face and body are visible.
- The model works only for the 4 breeds listed above; other breeds may be classified incorrectly.

## 👤 Author

Your Name  
GitHub: [@AounAslam](https://github.com/AounAslam)


