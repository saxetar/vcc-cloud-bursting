from flask import Flask
import time
import multiprocessing

app = Flask(__name__)


def stress_load():
    timeout = time.time() + 30  # Run for 30 seconds
    while time.time() < timeout:
        _ = 12345 * 12345

@app.route('/')
def home():
    return "Local App is Running!"

@app.route('/stress')
def stress():
    print("Multi-core stress test started...")
    
    processes = []
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=stress_load)
        p.start()
        processes.append(p)
    
    return "Multi-core stress test triggered on Local VM!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
