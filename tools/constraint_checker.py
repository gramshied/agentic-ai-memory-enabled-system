MAX_DISCOUNT_COST = 500  # INR


def check_discount_constraint(discount_cost):
    """
    Ensures discount cost does not exceed finance constraints.

    Args:
        discount_cost (float)

    Returns:
        dict: constraint validation result
    """
    if discount_cost <= MAX_DISCOUNT_COST:
        return {
            "approved": True,
            "reason": "Discount cost is within approved finance limits."
        }
    else:
        return {
            "approved": False,
            "reason": (
                f"Discount cost exceeds ₹{MAX_DISCOUNT_COST} limit "
                f"(calculated: ₹{discount_cost})."
            )
        }
