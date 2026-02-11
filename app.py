from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Travis AI server is running."

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({
        "status": "success",
        "message": "Hello from Travis AI 🚀"
    })

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    return jsonify({
        "reply": f"You said: {user_message}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)