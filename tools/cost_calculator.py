def calculate_discount_cost(monthly_charge, discount_percentage):
    """
    Calculates the absolute discount cost for one billing cycle.

    Args:
        monthly_charge (float): Customer's monthly charge in INR
        discount_percentage (float): Discount percentage (e.g., 20 for 20%)

    Returns:
        dict: discount cost and calculation details
    """
    discount_cost = (monthly_charge * discount_percentage) / 100

    return {
        "monthly_charge": monthly_charge,
        "discount_percentage": discount_percentage,
        "discount_cost": round(discount_cost, 2)
    }
