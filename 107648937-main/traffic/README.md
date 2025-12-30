# Traffic Sign Classifier with CNN (TensorFlow)

This project implements a convolutional neural network (CNN) using TensorFlow to classify traffic signs from the \[German Traffic Sign Recognition Benchmark (GTSRB)] dataset. The model achieves over **96% test accuracy**, learning to differentiate between 43 distinct classes of road signs.

---

## Model Architecture and Experimentation

### Experimentation Summary

I conducted a series of experiments to fine-tune the model's architecture, dropout, and training duration (epochs). Key highlights from the experimentation are:

* **Baseline model**: 1 Conv2D layer → Flatten → Dense (output) → Low accuracy (\~60%)
* **Final model**:

  * **Conv2D Layer 1**: 32 filters, 3×3 kernel, ReLU
  * **MaxPooling2D Layer 1**: pool size (2×2)
  * **Conv2D Layer 2**: 64 filters, 3×3 kernel, ReLU
  * **MaxPooling2D Layer 2**: pool size (2×2)
  * **Flatten Layer**
  * **Dense Layer**: 128 units, ReLU
  * **Dropout Layer**: 0.5 dropout rate
  * **Dense Output Layer**: 43 units (Softmax)

### Dropout Layer

Dropout was introduced after observing **overfitting beyond 5 epochs**. Training accuracy increased rapidly but validation accuracy plateaued. A 50% dropout rate (after the dense layer) significantly helped in regularizing the network, preventing overfitting, and stabilizing validation performance.

### Epoch Tuning

* Initial tests were run with 5, 10, and 15 epochs.
* Over 10 epochs, accuracy consistently improved without overfitting thanks to dropout.
* **10 epochs was chosen** as the optimal balance between training time and performance.

### Failed Experiments

* **Too many convolutional layers**: Adding a third Conv2D layer with 128 filters resulted in GPU memory saturation and minimal accuracy gain.
* **No dropout**: Performance peaked early and then degraded (classic overfitting).
* **Excessive dense layers**: Adding a second dense layer worsened generalization and increased training time unnecessarily.

---

## Results

| Metric         | Value      |
| -------------- | ---------- |
| Final Accuracy | **96.09%** |
| Final Loss     | **0.1609** |
| Model Saved As | `model.h5` |

> Model was trained on 43 categories of traffic signs, resized to 30×30 RGB images.

---

## 🛠 Dependencies

```bash
tensorflow
opencv-python
scikit-learn
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Running the Model

```bash
python traffic.py gtsrb
```

To save the trained model:

```bash
python traffic.py gtsrb model.h5
```

---

## Directory Structure

```
traffic/
├── gtsrb/               # 43 folders (0–42), each with training images
├── traffic.py           # Main training and evaluation script
├── model.h5             # Saved model (optional)
├── requirements.txt
└── README.md
```


