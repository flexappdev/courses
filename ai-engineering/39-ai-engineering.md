# 🎛️ Lesson 39 — Hyperparameter Tuning & Optimization

### *AI Engineer Roadmap 2025 — Skill #39*

---

## 🎯 Objective

Learn how to **optimize model performance** by tuning hyperparameters — the adjustable settings that control how an algorithm learns, generalizes, and balances accuracy with overfitting.

---

## 🧩 Definition

**Hyperparameter Tuning** is the process of finding the **best combination of model parameters** (like learning rate, depth, or batch size) that maximize performance on validation data.
Unlike learned parameters (weights), hyperparameters are **set before training** and significantly affect outcomes.

---

## 🧠 Core Concepts

| Concept                      | Description                                                          |
| ---------------------------- | -------------------------------------------------------------------- |
| **Hyperparameters**          | External controls like `n_estimators`, `learning_rate`, `max_depth`. |
| **Grid Search**              | Exhaustively tries all combinations from a defined grid.             |
| **Random Search**            | Samples random combinations for efficiency.                          |
| **Bayesian Optimization**    | Uses past results to choose promising hyperparameter sets.           |
| **Early Stopping**           | Stops training when validation loss stops improving.                 |
| **Cross-Validation**         | Splits data to evaluate performance consistency.                     |
| **Learning Rate Scheduling** | Adjusts learning rate dynamically during training.                   |
| **Hyperparameter Space**     | The search range for each tuning parameter.                          |

---

## ⚙️ Example — Grid Search (Scikit-Learn)

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

params = {"n_estimators": [50, 100, 200], "max_depth": [5, 10, 20]}
model = RandomForestClassifier()

grid = GridSearchCV(model, param_grid=params, cv=5, scoring='f1')
grid.fit(X_train, y_train)

print("Best Params:", grid.best_params_)
print("Best F1 Score:", grid.best_score_)
```

---

## ⚙️ Example — Bayesian Optimization (Optuna)

```python
import optuna
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 50, 300)
    lr = trial.suggest_float("learning_rate", 0.01, 0.3)
    model = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=lr)
    model.fit(X_train, y_train)
    return accuracy_score(y_val, model.predict(X_val))

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=25)
print(study.best_params)
```

---

## 🧱 Popular Optimization Tools

| Tool                                               | Description                                              |
| -------------------------------------------------- | -------------------------------------------------------- |
| **Scikit-Learn GridSearchCV / RandomizedSearchCV** | Classic, reliable search methods.                        |
| **Optuna**                                         | Bayesian optimization for any ML framework.              |
| **Ray Tune**                                       | Scalable hyperparameter tuning for distributed training. |
| **Weights & Biases Sweeps**                        | Experiment management for large tuning runs.             |
| **HyperOpt**                                       | Lightweight optimization using TPE algorithms.           |

---

## 📘 Mini Project

**Goal:** Tune a **Gradient Boosting Model** for Credit Risk Prediction
**Steps:**

1. Define parameter ranges (`learning_rate`, `max_depth`, `n_estimators`).
2. Use Optuna or GridSearchCV for optimization.
3. Evaluate with cross-validation.
4. Plot parameter importance and performance.

**Expected Outcome:**
A tuned model achieving significantly higher F1 and ROC-AUC than the default setup.

---

## 🧠 Example Prompt

> “Why does random search often outperform grid search for hyperparameter tuning?”

---

## 🔍 Key Takeaway

Hyperparameter tuning is **model alchemy** — small adjustments can yield huge improvements, turning a good model into a great one.

---

## 📚 Further Reading

* [Optuna Official Docs](https://optuna.org/)
* [Scikit-Learn Grid Search Guide](https://scikit-learn.org/stable/modules/grid_search.html)
* [Ray Tune Quickstart](https://docs.ray.io/en/latest/tune/index.html)
* [W&B Sweeps Tutorial](https://docs.wandb.ai/guides/sweeps)
* [Hyperparameter Optimization Best Practices](https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/)