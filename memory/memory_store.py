import json
from datetime import datetime


class MemoryStore:
    def __init__(self):
        self.memory = []

    def add_episode(self, customer_id, risk_level, action_taken,
                    revenue_before, revenue_after):

        success = revenue_after > revenue_before

        episode = {
            "customer_id": customer_id,
            "risk_level": risk_level,
            "action_taken": action_taken,
            "revenue_before": revenue_before,
            "revenue_after": revenue_after,
            "success": success,
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(episode)

    def get_all_memory(self):
        return self.memory

    def export_to_json(self, filename="memory_log.json"):
        with open(filename, "w") as f:
            json.dump(self.memory, f, indent=4)
