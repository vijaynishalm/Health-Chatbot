from flask import Flask, render_template, request
from chatbot import analyze_symptoms
from data import symptom_conditions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    user_input = ""
    follow_up_answers = {}

    if request.method == "POST":
        user_input = request.form.get("symptoms", "")
        for symptom in symptom_conditions:
            key = f"follow_up_{symptom}"
            if key in request.form:
                follow_up_answers[symptom] = request.form[key]
        results = analyze_symptoms(user_input, follow_up_answers)

    return render_template("index.html", results=results, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)