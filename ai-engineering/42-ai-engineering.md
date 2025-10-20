# 🔁 Lesson 42 — Recurrent Neural Networks (RNNs) & LSTMs

### *AI Engineer Roadmap 2025 — Skill #42*

---

## 🎯 Objective

Understand how **Recurrent Neural Networks (RNNs)** and their improved variant **LSTMs (Long Short-Term Memory)** process **sequential data**, enabling AI to handle time series, speech, and natural language.

---

## 🧩 Definition

**RNNs** are neural networks that remember previous inputs through **hidden state connections**, allowing them to learn temporal dependencies.
However, basic RNNs suffer from **vanishing gradients**, which **LSTMs** and **GRUs** solve by adding **gates** that control memory flow over long sequences.

---

## 🧠 Core Concepts

| Concept                           | Description                                                               |
| --------------------------------- | ------------------------------------------------------------------------- |
| **Sequence Data**                 | Ordered inputs where time or position matters (text, audio, time series). |
| **Hidden State**                  | Stores information from previous time steps.                              |
| **Vanishing Gradient Problem**    | Loss of memory over long sequences in basic RNNs.                         |
| **LSTM (Long Short-Term Memory)** | Adds gates to retain and forget information intelligently.                |
| **GRU (Gated Recurrent Unit)**    | Simplified LSTM with fewer parameters but similar performance.            |
| **Bidirectional RNNs**            | Process sequences in both forward and backward directions.                |
| **Time Steps**                    | Each input position in a sequence.                                        |
| **Sequential Modeling**           | Predicting future or next elements based on history.                      |

---

## ⚙️ Example — Simple RNN in Keras

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

model = Sequential([
    SimpleRNN(50, activation='tanh', input_shape=(10, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10, batch_size=16)
```

---

## ⚙️ Example — LSTM for Text Sequences

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense

model = Sequential([
    Embedding(input_dim=10000, output_dim=128, input_length=50),
    LSTM(128, return_sequences=False),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
```

---

## 🧱 Key Variants & Use Cases

| Model Type             | Use Case                                         |
| ---------------------- | ------------------------------------------------ |
| **Simple RNN**         | Basic time series or small sequence prediction.  |
| **LSTM**               | Long-term memory (language modeling, speech).    |
| **GRU**                | Lightweight version of LSTM for faster training. |
| **Bidirectional LSTM** | Context-aware NLP (reads sequences both ways).   |
| **Stacked RNNs**       | Multiple layers for complex dependencies.        |

---

## 📘 Mini Project

**Goal:** Build a **Text Sentiment Predictor using LSTM**
**Steps:**

1. Tokenize text and convert to padded sequences.
2. Train an embedding + LSTM model.
3. Evaluate on sentiment classification (positive/negative).
4. Visualize training loss and accuracy.

**Expected Outcome:**
A model that learns sentence structure and emotion, achieving 85–90% accuracy on text sentiment analysis.

---

## 🧠 Example Prompt

> “How do LSTMs solve the vanishing gradient problem that limits standard RNNs?”

---

## 🔍 Key Takeaway

RNNs and LSTMs enable machines to **learn from sequences and context over time**, forming the backbone of early NLP and speech models before Transformers took over.

---

## 📚 Further Reading

* [Understanding LSTMs — Colah’s Blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Keras LSTM Example](https://keras.io/examples/nlp/lstm_text_classification/)
* [GRU vs LSTM Comparison](https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be)
* [Sequence Models — Andrew Ng (Coursera)](https://www.coursera.org/learn/nlp-sequence-models)
* [Hands-on RNNs in TensorFlow](https://www.tensorflow.org/guide/keras/rnn)