from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

vectorizer = joblib.load("models/vectorizer.pkl")
svm_clf = joblib.load("models/svm_classifier.pkl")
reg = joblib.load("models/regressor.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    form_data = {
        "description": "",
        "input_description": "",
        "output_description": ""
    }

    if request.method == "POST":
        form_data["description"] = request.form["description"]
        form_data["input_description"] = request.form["input_description"]
        form_data["output_description"] = request.form["output_description"]

        full_text = (
            form_data["description"] + " " +
            form_data["input_description"] + " " +
            form_data["output_description"]
        ).lower().strip()

        X = vectorizer.transform([full_text])

        predicted_class = svm_clf.predict(X)[0]
        
        predicted_score = float(reg.predict(X)[0])


        prediction = {
            "class": predicted_class,
            "score": round(predicted_score, 2),
        }

    model_info = {
        "classifier": "Support Vector Machine (LinearSVC)",
        "regressor": "Gradient Boosting Regressor",
        "features": "TF-IDF (Unigrams + Bigrams)",
        "dataset_size": 4112
    }

    return render_template(
        "index.html",
        prediction=prediction,
        form_data=form_data,
        model_info=model_info
    )


if __name__ == "__main__":
    app.run(debug=True)
