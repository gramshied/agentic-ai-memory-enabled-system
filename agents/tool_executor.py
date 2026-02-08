from tools.cost_calculator import calculate_discount_cost
from tools.constraint_checker import check_discount_constraint
from tools.finance_summary import generate_finance_summary


class ToolExecutorAgent:
    def execute(self, tool_plan):
        """
        Executes selected tools sequentially and returns their outputs.
        """

        execution_results = {}
        cost_result = None
        constraint_result = None

        for step in tool_plan:
            tool_name = step["tool"]

            if tool_name == "calculate_discount_cost":
                cost_result = calculate_discount_cost(**step["params"])
                execution_results["cost_calculation"] = cost_result

            elif tool_name == "check_discount_constraint":
                if cost_result is None:
                    raise ValueError("Cost calculation must run before constraint check.")
                constraint_result = check_discount_constraint(
                    cost_result["discount_cost"]
                )
                execution_results["constraint_check"] = constraint_result

            elif tool_name == "generate_finance_summary":
                if cost_result is None or constraint_result is None:
                    raise ValueError(
                        "Finance summary requires cost and constraint results."
                    )
                finance_summary = generate_finance_summary(
                    cost_result, constraint_result
                )
                execution_results["finance_summary"] = finance_summary

        return execution_results
