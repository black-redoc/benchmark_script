#!/usr/bin/env python3
import subprocess
from statistics import mean

from time_benchmark import time_benchmark

SCRIPT_PATH = "./<your-script>.sh"
TIME_ELAPSED = list()
RATE_REQUESTS = 100
VERBOSE = 1


@time_benchmark(verbose=VERBOSE)
def request_stage():
    subprocess.call(
        SCRIPT_PATH, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT
    )


if __name__ == "__main__":
    try:
        for i in range(0, RATE_REQUESTS):
            if VERBOSE:
                print("request #%d" % (i + 1), end="")
            elapsed = request_stage()
            TIME_ELAPSED.append(elapsed)
    except PermissionError:
        print("\nERROR!")
        print("The script to exec hasn't execution permissions")
        print("Please run this command:")
        print("\tchmod +x ./<script_name>.sh")

        exit()

    avg = mean(TIME_ELAPSED)
    print("AVERAGE time elapsed from %d requests is %.2f" % (RATE_REQUESTS, avg))
