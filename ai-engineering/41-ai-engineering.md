# 🖼️ Lesson 41 — Convolutional Neural Networks (CNNs)

### *AI Engineer Roadmap 2025 — Skill #41*

---

## 🎯 Objective

Learn how **Convolutional Neural Networks (CNNs)** work — the deep learning architecture that revolutionized **computer vision**, enabling machines to recognize images, objects, and patterns automatically.

---

## 🧩 Definition

A **Convolutional Neural Network** is a deep learning model designed to process **grid-like data**, such as images.
CNNs use **convolution layers** to automatically learn **spatial hierarchies of features**, replacing the need for manual feature extraction.

---

## 🧠 Core Concepts

| Concept               | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| **Convolution Layer** | Slides filters (kernels) over an image to extract features.     |
| **Filters / Kernels** | Small matrices that detect patterns like edges or colors.       |
| **Feature Maps**      | Output of convolution that highlights learned features.         |
| **Pooling Layer**     | Downsamples feature maps to reduce dimensions (Max/Average).    |
| **Stride & Padding**  | Control filter movement and output size.                        |
| **Flatten Layer**     | Converts 2D feature maps into 1D arrays for dense layers.       |
| **Dropout**           | Reduces overfitting by randomly turning off neurons.            |
| **Transfer Learning** | Using pre-trained CNNs (ResNet, VGG, EfficientNet) on new data. |

---

## ⚙️ Example — Simple CNN with Keras

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64,64,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

---

## ⚙️ Example — Transfer Learning with Pre-Trained ResNet

```python
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

base = ResNet50(weights='imagenet', include_top=False)
x = GlobalAveragePooling2D()(base.output)
x = Dense(64, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x)
model = Model(inputs=base.input, outputs=output)

for layer in base.layers:
    layer.trainable = False  # freeze pretrained layers

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

---

## 🧱 Common CNN Architectures

| Model                                    | Description                                                   |
| ---------------------------------------- | ------------------------------------------------------------- |
| **LeNet (1998)**                         | First practical CNN for digit recognition.                    |
| **AlexNet (2012)**                       | Kickstarted deep learning era — ImageNet breakthrough.        |
| **VGG16 / VGG19**                        | Simple and deep with uniform 3×3 filters.                     |
| **ResNet**                               | Introduced residual connections — solved vanishing gradients. |
| **EfficientNet**                         | Scales width, depth, and resolution optimally.                |
| **ConvNeXt / Vision Transformer Hybrid** | Modern CNNs matching transformer performance.                 |

---

## 📘 Mini Project

**Goal:** Build an **Image Classifier for Cats vs Dogs**
**Steps:**

1. Load and preprocess images (64×64 RGB).
2. Train a CNN with 2–3 convolution layers.
3. Evaluate accuracy and visualize misclassifications.
4. Optionally fine-tune using a pre-trained model.

**Expected Outcome:**
A CNN that achieves >90% accuracy in binary image classification.

---

## 🧠 Example Prompt

> “Explain why convolutional layers outperform fully connected layers in image processing.”

---

## 🔍 Key Takeaway

CNNs learn **spatial hierarchies** — they see edges, textures, shapes, and objects progressively, forming the backbone of modern computer vision systems.

---

## 📚 Further Reading

* [CS231n CNN Guide (Stanford)](https://cs231n.github.io/convolutional-networks/)
* [Keras CNN Tutorial](https://keras.io/examples/vision/cnn_image_classification/)
* [ResNet Paper (Deep Residual Learning)](https://arxiv.org/abs/1512.03385)
* [Visualizing CNN Filters](https://distill.pub/2017/feature-visualization/)
* [EfficientNet Research](https://arxiv.org/abs/1905.11946)