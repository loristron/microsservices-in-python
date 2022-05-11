from flask import Flask, jsonify, request, render_template
import socket

app = Flask(__name__)

# FUNCTION TO FECH HOSTNAME AND IP ADDRESS
def fetch_details():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip

# DEFAULT FLASK APP PAGE
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# RETURNING JSONIFY CONTENT
@app.route("/health", methods=['GET'])
def health():
    return jsonify(
        status = "UP"
    )

# STATIC HTML PAGE
@app.route('/details', methods=['GET'])
def details():
    data = {}
    data['hostname'],  data['ip'] = fetch_details()
    return render_template('index.html', data=data)



# RUNNING WITH PYTHON3 APP.PY
# CHOOSING HOST AND PORT 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)