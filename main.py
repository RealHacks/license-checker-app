
import requests
import uuid
import sys

LICENSE_SERVER_URL = "https://license-server.onrender.com/api/check_license"

def get_pc_id() -> str:
    return str(uuid.getnode())

def validate_license_online(pc_id: str, license_key: str) -> bool:
    try:
        response = requests.post(LICENSE_SERVER_URL, json={
            "pc_id": pc_id,
            "license_key": license_key
        })
        response.raise_for_status()
        return response.json().get("valid", False)
    except Exception as e:
        print("Error:", e)
        return False

def start_app():
    print("✅ License valid. App started!")

def main():
    pc_id = get_pc_id()
    license_key = input("Enter license key: ").strip()

    if validate_license_online(pc_id, license_key):
        start_app()
    else:
        print("❌ Invalid license.")
        sys.exit(1)

if __name__ == "__main__":
    main()
