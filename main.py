import os
import openai
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Set OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Root route to handle the homepage
@app.route("/", methods=["GET"])
def home():
    return "Welcome to Karen AI! Use the /chat endpoint to interact with Karen."

# /chat endpoint to handle AI chat
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's message from the request
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Use OpenAI API to generate a response using the new API format
        response = openai.Completion.create(
            model="gpt-4",
            prompt=user_message,  # Use the prompt parameter for the message
            max_tokens=100
        )
        # Return the response
        return jsonify({"response": response['choices'][0]['text'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))