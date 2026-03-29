@app.route('/stress')
def stress():
    # Simulating a heavy scientific computing workload (Primality Testing)
    timeout = time.time() + 20
    num = 100000
    while time.time() < timeout:
        # Check if the number is prime to burn CPU cycles
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        num += 1
    return "Prime Generation CPU Stress test completed!"
