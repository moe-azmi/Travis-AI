from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/")
def home():
    return "Travis AI is LIVE 🚀"


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    response = model.generate_content(user_message)

    return jsonify({
        "reply": response.text
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
