<img width="1570" height="884" alt="image" src="https://github.com/user-attachments/assets/b5f1e280-1c45-464a-9d8c-cab0e622c264" />

🕵️ Crime Investigation Chatbot Game
📌 About

This is a web-based crime investigation game where the user plays as a detective. The player interrogates suspects, investigates clues, and identifies the real killer using logical reasoning and decision-making.

🚀 Features
Interrogate suspects (Sarah, Alex, John)
Investigate crime scene
Clue-based gameplay
Twist ending
Stores chat data in database
🛠️ Tech Stack
Flask (Backend)
IBM Watson Assistant (Chatbot logic)
Cloudant Database
HTML, CSS, JavaScript
🔧 Dependencies
flask
flask-cors
ibm-watson
ibm-cloud-sdk-core
cloudant

Or install directly:

pip install flask flask-cors ibm-watson ibm-cloud-sdk-core cloudant
🔐 Configuration

Add your credentials in app.py:

API_KEY = "your_api_key_here"
URL = "your_service_url_here"
ASSISTANT_ID = "your_assistant_id_here"
ENVIRONMENT_ID = "your_environment_id_here"


▶️ How to Run
Clone repository
git clone <your-repo-link>
cd your-project-folder
Install dependencies
pip install -r requirements.txt
Run server
python app.py
Open in browser
http://127.0.0.1:5000
📡 API
POST /chat

Request:

{
  "message": "interrogate sarah"
}

Response:

{
  "reply": "Bot response here"
}
🎮 How to Play
Interrogate suspects
Analyze their responses
Investigate clues
Decide who the killer is
🔮 Future Improvements
Better UI
Scoring system
Timer-based gameplay
Voice interaction

👤 Author
Prisha Kaushal
