class ToolSelectorAgent:
    def select_tools(self, analysis, proposed_discount_percentage):
        """
        Determines which tools are required based on the decision context.
        """

        selected_tools = []

        # If a discount is proposed, finance validation is mandatory
        if analysis["risk_level"] == "High" and proposed_discount_percentage > 0:
            selected_tools.append({
                "tool": "calculate_discount_cost",
                "params": {
                    "monthly_charge": analysis["customer_summary"]["monthly_charges"],
                    "discount_percentage": proposed_discount_percentage
                }
            })

            selected_tools.append({
                "tool": "check_discount_constraint"
            })

            selected_tools.append({
                "tool": "generate_finance_summary"
            })

        return selected_tools
