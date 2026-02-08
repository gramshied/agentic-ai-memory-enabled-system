class ValidatorAgent:
    def validate(self, proposed_actions, execution_results):
        """
        Validates proposed actions against tool-derived facts.
        """

        validation = {
            "approved": True,
            "final_actions": proposed_actions,
            "validation_notes": []
        }

        finance_summary = execution_results.get("finance_summary")

        # If finance summary exists, enforce approval
        if finance_summary:
            if not finance_summary["finance_approval"]:
                validation["approved"] = False
                validation["final_actions"] = [
                    "Upgrade plan for 1 month",
                    "Free access for 3 months"
                ]
                validation["validation_notes"].append(
                    finance_summary["finance_note"]
                )
            else:
                validation["validation_notes"].append(
                    "Finance constraints satisfied."
                )

        return validation
