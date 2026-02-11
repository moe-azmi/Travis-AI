from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_request():
    data = request.json
    user_message = data.get("query", [{}])[0].get("content", "")

    return jsonify({
        "response": f"Travis received: {user_message}"
    })

@app.route("/", methods=["GET"])
def home():
    return "Travis AI server is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
