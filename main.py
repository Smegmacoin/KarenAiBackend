import os
import openai
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Set OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Karen AI! Use the /chat endpoint to interact with Karen."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Karen, a flirty AI focused on SpongeBob SquarePants."},
                {"role": "user", "content": user_message},
            ]
        )
        return jsonify({"response": response.choices[0].message["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))