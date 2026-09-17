import time

print("🚀 AutoDev Crash Test Started")

numbers = [10, 5, 2, 0, 1]

for n in numbers:
    print(f"Processing value: {n}")
    time.sleep(1)

    result = 100 / n

    print(f"Result: {result}")

print("✅ Processing completed")
