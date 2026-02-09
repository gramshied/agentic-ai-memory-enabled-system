class MemoryManager:
    def __init__(self, memory_store):
        self.memory_store = memory_store

    def get_success_rate(self, action_name):
        memory = self.memory_store.get_all_memory()

        action_episodes = [
            episode for episode in memory
            if episode["action_taken"] == action_name
        ]

        if not action_episodes:
            return None  # No history

        successes = sum(1 for episode in action_episodes if episode["success"])

        return successes / len(action_episodes)

    def get_best_action(self, possible_actions):
        """
        Returns the action with highest historical success rate.
        If no memory exists, returns None.
        """
        best_action = None
        best_score = -1

        for action in possible_actions:
            score = self.get_success_rate(action)

            if score is not None and score > best_score:
                best_score = score
                best_action = action

        return best_action
