import openai
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Set your OpenAI API key (replace 'os.getenv("OPENAI_API_KEY")' with your actual key if hardcoding)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Secure way using environment variables
# Uncomment the next line to hardcode the API key (less secure):
# openai.api_key = "your_actual_api_key"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    try:
        # OpenAI API request
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Karen, an AI with a flirty and SpongeBob-themed personality."},
                {"role": "user", "content": user_message}
            ]
        )
        ai_response = response['choices'][0]['message']['content']
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
