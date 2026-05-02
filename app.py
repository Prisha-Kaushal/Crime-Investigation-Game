from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "pg_crime_integrated"

# -------------------------
# FULL INTEGRATED GAME DATA
# -------------------------
GAME = {
    "intro": "You are a student moving to Delhi for studies. You choose a PG. After moving in, a mystery unfolds.",

    "pg_types": {
        "cheap": {
            "name": "Cheap PG",
            "clue_modifier": "low_security"
        },
        "mid": {
            "name": "Mid PG",
            "clue_modifier": "balanced"
        },
        "premium": {
            "name": "Premium PG",
            "clue_modifier": "high_security"
        }
    },

    "suspects": [
        "Rohan (Roommate)",
        "Aditi (PG Owner)",
        "Karan (Neighbor)"
    ],

    "killer": "Rohan (Roommate)",

    "clues": {
        "low_security": [
            "Door lock was weak and easily broken.",
            "No CCTV outside the PG."
        ],
        "balanced": [
            "CCTV shows a shadow at 2 AM.",
            "Shared kitchen was disturbed."
        ],
        "high_security": [
            "Security footage partially recovered.",
            "Access card used at odd hours."
        ]
    }
}

# -------------------------
# INIT
# -------------------------
@app.route("/")
def index():
    session["phase"] = "pg_selection"
    session["pg"] = None
    session["clue_index"] = 0
    session["questions"] = 0
    return render_template("index.html")

# -------------------------
# CORE GAME ENGINE
# -------------------------
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    msg = data.get("message", "").lower()

    # INIT SCORE IF NOT EXISTS
    if "score" not in session:
        session["score"] = 0

    phase = session.get("phase", "pg_selection")
    response = ""

    # -------------------------
    # PG SELECTION PHASE
    # -------------------------
    if phase == "pg_selection":

        if "cheap" in msg:
            session["phase"] = "investigation"
            response = "Cheap PG selected. Mystery begins..."

        elif "mid" in msg:
            session["phase"] = "investigation"
            response = "Mid PG selected. Something feels off..."

        elif "premium" in msg:
            session["phase"] = "investigation"
            response = "Premium PG selected. High security but strange vibes..."

        else:
            response = "Choose PG: cheap / mid / premium"

    # -------------------------
    # INVESTIGATION PHASE
    # -------------------------
    elif phase == "investigation":

        # SUSPECTS
        if "suspects" in msg:
            response = "Suspects: Rohan, Aditi, Karan"
            session["score"] += 2  # small reward for exploration

        # CLUES
        elif "clue" in msg:
            session["score"] += 10
            response = "Clue found: CCTV shows suspicious movement at night."

        # ACCUSATION
        elif "accuse" in msg:
            if "rohan" in msg:
                session["score"] += 20
                response = f"Correct! Case solved. Final Score: {session['score']}"
                session["phase"] = "ended"
            else:
                session["score"] -= 10
                response = f"Wrong accusation. Score: {session['score']}"

        # GENERAL
        else:
            response = f"Investigate further... Current Score: {session['score']}"

    # -------------------------
    # END PHASE
    # -------------------------
    else:
        response = f"Game over. Final Score: {session['score']}"

    return jsonify({
        "reply": response,
        "score": session["score"]
    })


if __name__ == "__main__":
    app.run(debug=True)