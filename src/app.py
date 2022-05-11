from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health", methods=['GET'])
def health():
    
    return jsonify(
        status = "UP"
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)