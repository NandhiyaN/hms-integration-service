
import subprocess
import asyncio
import pytest


def start_hms():
    # Clean up any existing containers and images
    subprocess.run(["docker-compose", "up", "--build", "-d"], check=True)

def stop_hms():
    subprocess.run(["docker-compose", "down"], check=True)
    subprocess.run(["docker-compose", "down", "--rmi", "all"], check=True)

def run_tests():
    #subprocess.run(["python3", "-m", "pytest", "hms_tests.py", "-v"], check=True)
    # run the test asyncio tests
    #subprocess.run(["pytest", "hms_tests.py", "-v"], check=True)
    subprocess.run([
        "python3", "-m", "pytest", 
        "hms_tests.py", 
        "-v", 
        "-o", "asyncio_mode=auto"

        # bruno tests add here
        
    ], check=True)


#pass STOP or START as command line argument to stop or start the services 
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "STOP":
            stop_hms()
        elif sys.argv[1] == "START":
            start_hms()
        elif sys.argv[1] == "TEST":
            run_tests()
        else:
            print("Invalid argument. Use STOP, START, or TEST.")
    else:        print("No argument provided. Use STOP, START, or TEST.")