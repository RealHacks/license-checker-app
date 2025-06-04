
from flask import Flask, request, jsonify
import hmac
import hashlib
import base64

app = Flask(__name__)
SECRET_KEY = b'super_secret_key_change_me'

def generate_license_key(pc_id: str) -> str:
    hmac_digest = hmac.new(SECRET_KEY, pc_id.encode(), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(hmac_digest).decode()[:25]

@app.route('/api/check_license', methods=['POST'])
def check_license():
    data = request.json
    pc_id = data.get("pc_id", "")
    provided_key = data.get("license_key", "")

    expected_key = generate_license_key(pc_id)
    valid = hmac.compare_digest(expected_key, provided_key)
    return jsonify({"valid": valid})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
