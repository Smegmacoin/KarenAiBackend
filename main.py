import os
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Root route to handle the homepage
@app.route("/", methods=["GET"])
def home():
    return "Welcome to Karen AI! Use the /chat endpoint to interact with Karen."

# /chat endpoint to handle AI chat (temporarily just return the received message)
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the request
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Temporarily return the received message (for testing)
    return jsonify({"received_message": user_message})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))