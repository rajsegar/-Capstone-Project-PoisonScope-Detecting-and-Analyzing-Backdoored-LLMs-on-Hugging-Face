# Capstone-Project-PoisonScope-Detecting-and-Analyzing-Backdoored-LLMs-on-Hugging-Face

----------------
# 🚀 Overview

This project provides a complete, end‑to‑end workflow for working with TextAttack, a powerful framework for training, evaluating, and attacking NLP models. It demonstrates how to:

Install and configure TextAttack in a Windows environment

Train a transformer‑based sentiment analysis model using Hugging Face datasets

Evaluate model performance using TextAttack’s built‑in evaluation utilities

Perform adversarial attacks such as TextFooler and DeepWordBug to measure model robustness

Generate detailed summaries and metrics that highlight vulnerabilities in language models

This documentation serves as a practical guide for anyone looking to explore adversarial NLP, understand model weaknesses, and integrate adversarial testing into their ML pipelines.

# TextAttack Installation and Usage Guide (Revised)

## 🖥️ Windows Installation Requirements

To install and run **TextAttack** on Windows 10 or 11, make sure you have the following:

* **Windows 10 or 11** operating system
* **Anaconda Distribution** installed
* **MSVC Compiler** (required for building some Python packages)

---

## 📦 Step 1: Create a Conda Environment

Using Anaconda virtual environments ensures clean and isolated setups.

```bash
conda create -n textattack python=3.8
conda activate textattack
```

---

## 📥 Step 2: Install pycld2 Manually (Windows Requirement)

TextAttack requires **pycld2**, which does **not** build automatically on Windows.
You must install it manually from one of these sources:

* PyPI: [https://pypi.org/project/pycld2/#files](https://pypi.org/project/pycld2/#files)
* Christoph Gohlke’s Unofficial Binaries: [https://www.cgohlke.com/](https://www.cgohlke.com/)

Install the appropriate `.whl` file for your Python version.

---

## ⚙️ Step 3: Install TextAttack

Once pycld2 is installed, proceed with TextAttack:

```bash
pip install textattack
pip install textattack[tensorflow]
```

Verify installation:

```bash
pip show textattack
```

---

## ⚡ Optional: CUDA Acceleration

If you have an NVIDIA GPU, you can enable hardware acceleration.

Install **CUDA 11.0**, which is supported by both TensorFlow and PyTorch.

NVIDIA CUDA 11.0 Guide:
[https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-microsoft-windows/index.html](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-microsoft-windows/index.html)

After installing:

```bash
nvcc -V
```

This confirms CUDA is installed correctly.

---

# 📚 Training a Model with TextAttack

### Preview the Dataset

```bash
textattack peek-dataset --dataset-from-huggingface rotten_tomatoes
```

### Train a Model (DistilBERT Example)

```bash
textattack train \
  --model-name-or-path distilbert-base-uncased \
  --dataset rotten_tomatoes \
  --model-num-labels 2 \
  --model-max-length 64 \
  --per-device-train-batch-size 128 \
  --num-epochs 1
```

This trains a binary classifier on the Rotten Tomatoes dataset.

### Notes

* Dataset is already lowercased → use **uncased model**
* Max sequence length of 64 is sufficient

---

# 📈 Evaluation

Once training is complete, evaluate the model:

```bash
textattack eval --num-examples 1000 \
  --model ./outputs/2025-11-01-09-44-22-099720/best_model/ \
  --dataset-from-huggingface rotten_tomatoes \
  --dataset-split test
```

### Summary Achieved

* Accuracy improved steadily across epochs
* Loss decreased consistently
* Output model saved automatically each epoch
* Example result: **72.30% accuracy** on test set

---

# 🔥 Running Adversarial Attacks (TextFooler)

Test model robustness using **TextFooler**:

```bash
textattack attack \
  --recipe textfooler \
  --num-examples 100 \
  --model ./outputs/2025-11-01-09-44-22-099720/best_model/ \
  --dataset-from-huggingface rotten_tomatoes \
  --dataset-split test
```

### Example Attack Summary

* Original accuracy: **83%**
* Attack success rate: **100%**
* Modified words per sample: **18.25%**
* Queries per attack: **96.01**
* Model accuracy under attack: **0%** (fully compromised)

**Example:**
Replacing "approach to material" with "approaches to equipment" flips model prediction despite similar meaning.

---

# 🎁 Bonus: Additional Attack Examples

### DeepWordBug Attack

```bash
textattack attack \
  --recipe deepwordbug \
  --model lstm-mr \
  --num-examples 2 \
  --log-summary-to-json attack_summary.json
```

This generates a machine‑readable `attack_summary.json`.

Enable advanced metrics:

```bash
textattack attack --model lstm-mr --recipe deepwordbug --num-examples 2 --attack-n --enable-advance-metrics
```

---

# ✅ End of Documentation
