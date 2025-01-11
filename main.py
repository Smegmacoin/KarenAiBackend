import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are Karen, a flirty AI focused on SpongeBob SquarePants.\nUser: {user_message}\nKaren:",
            max_tokens=100
        )
        return jsonify({"response": response['choices'][0]['text'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))