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
    try:
        # Get the user's message from the request
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Use OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Update based on your chosen model
            prompt=f"You are Karen, a flirty AI focused on SpongeBob SquarePants. Respond to this message: {user_message}",
            max_tokens=150
        )

        # Return the response
        return jsonify({"response": response['choices'][0]['text'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))