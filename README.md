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

---

## Changes needed before pushing to GitHub

Your uploaded project folder had a few things that should **not** be committed to GitHub. Here's what to fix:

1. **Remove the `venv/` folder** — this is your local Python virtual environment (hundreds of files). It should never be committed; it's machine-specific and bloats the repo. Instead, commit a `requirements.txt` (included below) so anyone can recreate the environment.
2. **Remove `__pycache__/` folders and `.pyc` files** — these are compiled Python cache files, auto-generated and unnecessary in version control.
3. **Remove `tempCodeRunnerFile.python`** — this file contains an unrelated "Password Strength Analyzer" script (looks like leftover code from a different exercise/task, not part of the Health Chatbot). It's not imported or used anywhere in `app.py`/`chatbot.py`, so it can be safely deleted.
4. **Add a `.gitignore`** (included below) so `venv/`, cache files, and editor junk never get committed in the future.
5. **Add a `requirements.txt`** (included below) — currently the project has no dependency file, so nobody else can install the correct packages easily.
6. (Optional but recommended) Fix line endings — the source files use Windows-style `\r\n` line endings. Not a functional problem, but if you plan to collaborate across OSes, consider normalizing to `\n` (most editors/Git can do this automatically via `.gitattributes`).

### Files provided for you
- `.gitignore` — excludes `venv/`, `__pycache__/`, and the leftover temp file
- `requirements.txt` — lists `Flask` (the only external dependency actually used)
- This `README.md`

Copy these into your project's root folder (next to `app.py`), **delete `venv/`, `__pycache__/`, and `tempCodeRunnerFile.python`**, then push to GitHub.

---

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
