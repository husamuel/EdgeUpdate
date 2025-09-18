from flask import Flask, jsonify, request, Response
from datetime import datetime
import requests
from prometheus_client import start_http_server, Counter, generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry

app = Flask(__name__)

registry = CollectorRegistry()
requests_total = Counter('requests_total', 'Total requests', registry=registry)

devices_status = {
    "device_1": {"device_id": 1, "version": "1.0.0", "last_update": None, "online": True},
    "device_2": {"device_id": 2, "version": "1.0.0", "last_update": None, "online": True},
    "device_3": {"device_id": 3, "version": "1.0.0", "last_update": None, "online": True},
}

def update_version(device_id, new_version):
    url = f"http://{device_id}:5000/update" 

    try:
        response = requests.post(url, json={"version": new_version})
        if response.status_code == 200:
            devices_status[device_id]["version"] = new_version
            devices_status[device_id]["last_update"] = datetime.now().isoformat()
            return True
        else:
            return False
    except:
        return False

@app.route('/devices', methods=['GET'])
def devices():
    requests_total.inc()
    return jsonify(devices_status)

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    device_id = data.get("device_id")
    new_version = data.get("version")

    if device_id in devices_status:
        success = update_version(device_id, new_version)
        if success:
            return jsonify({"message": "Updated", "device": device_id, "version": new_version})
        else:
            return jsonify({"error": "Failed to update device"})
    else:
        return jsonify({"error": "Device not found"}), 404

@app.route('/metrics')
def metrics():
    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)