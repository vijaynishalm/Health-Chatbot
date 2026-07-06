# 🩺 Health Chatbot

A simple Flask-based web app that takes a user's symptoms as text input, matches them against a built-in symptom database, asks a relevant follow-up question, and returns possible conditions along with a severity level and an urgency score (out of 10).

Built for a hackathon (Hackster Hackathon).

---

## How it works

1. The user types their symptoms in a text box (e.g. `headache, fever`).
2. `chatbot.py` matches the input against the symptom dictionary in `data.py`.
3. For each matched symptom, the app shows:
   - Possible conditions
   - Severity (common / critical / very critical)
   - Urgency score (1–10)
   - A follow-up question (e.g. "Do you also feel nausea or blurred vision?")
4. Once the user answers the follow-up question, the app refines the list of possible conditions and recalculates the urgency score based on keyword matching (e.g. mentioning "vomiting" or "fainting" increases urgency).

⚠️ **Disclaimer:** This tool is for educational/demo purposes only. It does not provide medical advice or diagnosis. Always consult a real healthcare professional for medical concerns.

---

## Project structure

```
hackster hackathon/
├── app.py                  # Flask app entry point (routes)
├── chatbot.py               # Core logic: matching symptoms, refining conditions/urgency
├── data.py                  # Symptom → conditions/severity/urgency/follow-up database
└── templates/
    └── index.html            # Front-end page (Tailwind CSS via CDN)
```


## How to run this project

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
Go to:
```
http://127.0.0.1:5000
```

Type in your symptoms, hit **Check**, answer the follow-up question if one appears, then submit again to see the refined results.

---

## Tech stack
- **Backend:** Python, Flask
- **Frontend:** HTML, Jinja2 templates, Tailwind CSS (via CDN)
- **Logic:** Rule-based keyword matching (no external ML/AI model)
