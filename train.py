import json
import pandas as pd
import joblib
from sklearn.svm import LinearSVC


data = []

with open("data/problems_data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)

df = df[[
    "title",
    "description",
    "input_description",
    "output_description",
    "problem_class",
    "problem_score"
]]

df.fillna("", inplace=True)

df["full_text"] = (
    df["title"] + " " +
    df["description"] + " " +
    df["input_description"] + " " +
    df["output_description"]
)


df["full_text"] = df["full_text"].str.lower().str.strip()


print("******************************")
X_text = df["full_text"]
y_class = df["problem_class"]
y_score = df["problem_score"]



from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    stop_words="english"
)

X = vectorizer.fit_transform(X_text)

from sklearn.model_selection import train_test_split
X_train, X_test, y_class_train, y_class_test, y_score_train, y_score_test = train_test_split(
    X,
    y_class,
    y_score,
    test_size=0.2,
    random_state=42,
    stratify=y_class
)

svm_clf = LinearSVC(class_weight="balanced", random_state=42)
svm_clf.fit(X_train, y_class_train)
y_svm_pred = svm_clf.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix

print("SVM Classification Report:")
print(classification_report(y_class_test, y_svm_pred))

print("SVM Confusion Matrix:")
print(confusion_matrix(y_class_test, y_svm_pred))


from sklearn.ensemble import GradientBoostingRegressor
reg = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)

reg.fit(X_train, y_score_train)
y_score_pred = reg.predict(X_test)
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
mae = mean_absolute_error(y_score_test, y_score_pred)
rmse = np.sqrt(mean_squared_error(y_score_test, y_score_pred))

print("Regression Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)


joblib.dump(vectorizer, "models/vectorizer.pkl")
joblib.dump(svm_clf, "models/svm_classifier.pkl")
joblib.dump(reg, "models/regressor.pkl")
print("Models and vectorizer saved successfully.")