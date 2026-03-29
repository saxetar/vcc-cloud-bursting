from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Local App is Running!"

@app.route('/stress')
def stress():
    print("Stress test started...")
    start_time = time.time()
    while time.time() - start_time < 30:
        _ = 12345 * 12345
    return "Stress test completed on Local VM!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
