import json
import os
from datetime import datetime


class MedicationLogger:
    def __init__(self, log_path="logs/medication_log.json"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        if not os.path.exists(log_path):
            with open(log_path, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def save_event(self, event, state):
        with open(self.log_path, "r", encoding="utf-8") as f:
            logs = json.load(f)

        logs.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event": event,
            "state": state
        })

        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=4)
