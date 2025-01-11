import os
import openai
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route for the homepage
@app.route("/", methods=["GET"])
def home():
    return "Welcome to Karen AI! Use the /chat endpoint to interact with Karen."

# Route for chat interactions
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate a response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine
            prompt=f"You are Karen, a flirty AI focused on SpongeBob SquarePants.\nUser: {user_message}\nKaren:",
            max_tokens=100,
            temperature=0.7
        )
        # Extract and return the response text
        return jsonify({"response": response['choices'][0]['text'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))