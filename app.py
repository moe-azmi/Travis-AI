from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Travis AI server is running."

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = f"You said: {user_message}"

    return jsonify({
        "reply": response,
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)