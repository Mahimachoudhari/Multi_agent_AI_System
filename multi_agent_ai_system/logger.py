from datetime import datetime


def log_data(step, content):
    try:
        with open("logs.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{'='*60}\n")
            file.write(f"{datetime.now()} | {step}\n")
            file.write(f"{content}\n")
    except Exception as e:
        print("Logging Error:", e)