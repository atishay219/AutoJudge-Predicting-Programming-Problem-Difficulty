# AutoJudge: Predicting Programming Problem Difficulty

## 📌 Project Overview
AutoJudge is a classical machine learning–based system that automatically predicts the **difficulty of programming problems** using only their textual descriptions.  
The system performs two tasks:

- **Classification:** Predicts difficulty level as **Easy / Medium / Hard**
- **Regression:** Predicts a **numerical difficulty score**

The objective is to automate difficulty estimation and reduce dependence on human judgment or user feedback on coding platforms.

---

## 📊 Dataset Used
The project uses a dataset of programming problems containing labeled difficulty classes and numerical difficulty scores.

**Dataset fields include:**
- Title
- Problem Description
- Input Description
- Output Description
- Problem Class (Easy / Medium / Hard)
- Problem Score (numeric)

**Dataset reference link:**  
https://github.com/AREEG94FAHAD/TaskComplexityEval-24

*(The dataset is used only for training and evaluation.)*

---

## 🛠️ Approach and Models Used

### 1️⃣ Data Preprocessing
- Combined title, description, input description, and output description into a single text field
- Converted text to lowercase
- Handled missing values

### 2️⃣ Feature Extraction
- **TF-IDF Vectorization**
- Unigrams and bigrams
- Maximum features: 5000
- English stop-word removal

### 3️⃣ Classification Model
- **Support Vector Machine (LinearSVC)**
- Predicts difficulty class: Easy / Medium / Hard
- Selected after comparison with Logistic Regression

### 4️⃣ Regression Model
- **Gradient Boosting Regressor**
- Predicts numerical difficulty score

---

## 📈 Evaluation Metrics

### Classification

- **Accuracy:** 47%

Support Vector Machine (SVM) achieved better accuracy compared to Logistic Regression and was chosen.

### Regression
- **Mean Absolute Error (MAE):** ~1.71
- **Root Mean Squared Error (RMSE):** ~2.04

These metrics indicate reasonable performance for predicting difficulty scores using text-only features.

---

## ▶️ Steps to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/atishay219/AutoJudge-Predicting-Programming-Problem-Difficulty.git
cd AutoJudge
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the models
```bash
python train.py
```

### 4️⃣ Run the web application
```bash
python app.py
```


Open your browser and go to:

http://127.0.0.1:5000/


---

## 🌐 Web Interface Explanation
The project includes a **Flask-based web application** that allows users to:

1. Paste:
   - Problem description
   - Input description
   - Output description
2. Click **Predict Difficulty**
3. View:
   - Predicted difficulty class
   - Predicted difficulty score
   - Visual difficulty progress bar
4. Use:
   - Dark mode toggle
   - Clear / reset functionality

The web application runs locally and does not require hosting.

---

## 🎥 Demo Video

📌 **Demo Video Link (2–3 minutes):**  
👉 https://drive.google.com/drive/folders/1_fMLsP4kRYprcdYWdE97Sni4NGFbjWE3?usp=drive_link

The demo video demonstrates:
- Brief explanation of the project
- Model approach
- Working web interface with predictions

---

## 👤 Author Details

- **Name:** Atishay Jain 
- **Course:** B.TECH. Mechanical Enginering 
- **Year:** 2
- **Enrolment No.:** 24117030
- **Gmail ID:** atishay_j@me.iitr.ac.in


