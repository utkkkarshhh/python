import os
import logging
from datetime import datetime

log_file_path = os.path.join(".", "logs", "user_activity.log")
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_activity(message):
    logging.info(message)

if __name__ == "__main__":
    log_activity("User logged in.")
    log_activity("User viewed profile page.")
    log_activity("User logged out.")
    print(f"User activities have been logged to {log_file_path}")
