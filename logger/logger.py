import os
from datetime import datetime

LOG_FILE = 'logs/keylog.txt'

class KeyLoggerService:
    def __init__(self):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        self.log_file = LOG_FILE
    def log(self, key_str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"[{timestamp}] {key_str}\n"
        with open(self.log_file, "a") as f:
            f.write(formatted)
                    