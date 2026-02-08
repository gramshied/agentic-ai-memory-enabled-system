def generate_finance_summary(cost_result, constraint_result):
    """
    Generates a finance-team-friendly summary.

    Args:
        cost_result (dict)
        constraint_result (dict)

    Returns:
        dict: finance summary
    """
    return {
        "discount_cost": cost_result["discount_cost"],
        "finance_approval": constraint_result["approved"],
        "finance_note": constraint_result["reason"]
    }
