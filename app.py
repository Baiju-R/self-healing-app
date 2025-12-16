from flask import Flask, jsonify
import os
import psutil
import threading
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Self-Healing DevOps App",
        "status": "running",
        "version": os.getenv("APP_VERSION", "v1")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent
    })


@app.route("/cpu-stress")
def cpu_stress():
    def burn_cpu():
        while True:
            pass

    thread = threading.Thread(target=burn_cpu)
    thread.start()

    return jsonify({
        "message": "CPU stress started"
    })


@app.route("/memory-stress")
def memory_stress():
    big_data = []
    while True:
        big_data.append("X" * 10**6)
        time.sleep(0.1)


@app.route("/crash")
def crash():
    os._exit(1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
