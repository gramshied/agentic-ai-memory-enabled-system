class PlannerAgent:
    def __init__(self, memory_manager=None):
        self.memory_manager = memory_manager

    def plan(self, analysis):
        risk_level = analysis["risk_level"]
        churn_probability = analysis["churn_probability"]

        # Default rule-based actions
        if risk_level == "High":
            possible_actions = [
                "Offer discount",
                "Upgrade plan for 1 month",
                "Free access for 3 months"
            ]
        elif risk_level == "Medium":
            possible_actions = [
                "Upgrade plan for 1 month",
                "Free access for 3 months"
            ]
        else:
            possible_actions = ["No immediate action"]

        selected_action = None

        # If memory is available, try adaptive selection
        if self.memory_manager:
            best_action = self.memory_manager.get_best_action(possible_actions)
            if best_action:
                selected_action = best_action

        # Fallback to first rule-based action
        if not selected_action:
            selected_action = possible_actions[0]

        plan = {
            "risk_level": risk_level,
            "churn_probability": churn_probability,
            "recommended_actions": [selected_action],
            "decision_confidence": self._confidence_score(churn_probability)
        }

        return plan

    def _confidence_score(self, churn_probability):
        if churn_probability >= 0.7:
            return "Very High"
        elif churn_probability >= 0.5:
            return "High"
        elif churn_probability >= 0.3:
            return "Medium"
        else:
            return "Low"
