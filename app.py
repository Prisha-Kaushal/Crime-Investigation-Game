from flask import Flask, render_template, request, jsonify, session
import os

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
ENVIRONMENT_ID = os.getenv("ENVIRONMENT_ID")

app = Flask(__name__)
app.secret_key = "crime_game_secret"

@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    msg = data.get("message", "").lower()

    if "suspect" in msg:
        reply = "Suspects: John, Sarah, Alex"
    elif "clue" in msg:
        reply = "Check CCTV, fingerprints, and knife carefully."
    elif "accuse" in msg:
        if "john" in msg:
            reply = "Correct suspect! You solved the case."
        else:
            reply = "Wrong suspect. Try again."
    else:
        reply = "Try: suspects / clue / accuse John"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)