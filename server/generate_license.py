
import hmac
import hashlib
import base64

SECRET_KEY = b'super_secret_key_change_me'

def generate_license_key(pc_id):
    hmac_digest = hmac.new(SECRET_KEY, pc_id.encode(), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(hmac_digest).decode()[:25]

if __name__ == "__main__":
    pc_id = input("Enter PC ID: ").strip()
    print("License Key:", generate_license_key(pc_id))
