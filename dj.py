import subprocess
import time

while True:
    processes = []
    for i in range(3):
        process = subprocess.Popen(['python3', 'main.py'])
        processes.append(process)
        print(f"started {i}")
        time.sleep(5)

    # Wait for all processes to complete
    for process in processes:
        process.wait()
    print("All stopped")
    open("ds.txt", 'a').write("All stopped\n")
    time.sleep(5)
