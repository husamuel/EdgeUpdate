from flask import Flask, jsonify, request, Response
from datetime import datetime
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, CollectorRegistry

app = Flask(__name__)

device_state = {
    "device_id": "device_1",
    "version": "1.0.0",
    "last_update": None,
    "online": True
}

registry = CollectorRegistry()
requests_total = Counter('requests_total', 'Total requests', registry=registry)

@app.route('/status', methods=['GET'])
def status():
    requests_total.inc()
    return jsonify(device_state)

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    new_version = data.get("version")

    if new_version:
        device_state["version"] = new_version
        device_state["last_update"] = datetime.now().isoformat()
        requests_total.inc()
        return jsonify({
            "message": "Updated",
            "device": device_state["device_id"],
            "version": new_version
        })
    else:
        return jsonify({"error": "No version provided"}), 400

@app.route('/metrics')
def metrics():
    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
