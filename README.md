from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/yield')
def get_data():
    return jsonify({
        "profit": "15.75",
        "status": "LIVE",
        "commander": "Mohamed Hussein",
        "wallet": "01011257797"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
