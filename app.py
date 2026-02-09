from agents.analyst import AnalystAgent
from agents.planner import PlannerAgent
from agents.explainer import ExplainerAgent

from memory.memory_store import MemoryStore
from memory.memory_manager import MemoryManager


def simulate_revenue(action, revenue_before):
    """
    Simple simulation logic for demonstration.
    """
    if action == "Offer discount":
        return revenue_before + 200  # Sometimes not very effective
    elif action == "Upgrade plan for 1 month":
        return revenue_before + 400
    elif action == "Free access for 3 months":
        return revenue_before + 300
    else:
        return revenue_before


def run_memory_enabled_decision(customer_id, customer_profile, churn_probability,
                                 revenue_before, memory_store):

    memory_manager = MemoryManager(memory_store)

    analyst = AnalystAgent()
    planner = PlannerAgent(memory_manager=memory_manager)
    explainer = ExplainerAgent()

    # Step 1: Analysis
    analysis = analyst.analyze(customer_profile, churn_probability)

    # Step 2: Adaptive planning
    plan = planner.plan(analysis)
    selected_action = plan["recommended_actions"][0]

    # Step 3: Simulate outcome
    revenue_after = simulate_revenue(selected_action, revenue_before)

    # Step 4: Store episode in memory
    memory_store.add_episode(
        customer_id=customer_id,
        risk_level=analysis["risk_level"],
        action_taken=selected_action,
        revenue_before=revenue_before,
        revenue_after=revenue_after
    )

    # Step 5: Explain decision
    explanation = explainer.explain(
        analysis=analysis,
        plan=plan,
        critique={
            "approved": True,
            "final_actions": [selected_action],
            "concerns": []
        }
    )

    explanation["revenue_before"] = revenue_before
    explanation["revenue_after"] = revenue_after

    return explanation


if __name__ == "__main__":
    memory_store = MemoryStore()

    customer_profile = {
        "tenure": 3,
        "contract": "Month-to-month",
        "monthly_charges": 2500,
        "internet_service": "Fiber optic"
    }

    churn_probability = 0.65
    revenue_before = 2500

    print("\n--- FIRST DECISION ---")
    decision1 = run_memory_enabled_decision(
        customer_id="C001",
        customer_profile=customer_profile,
        churn_probability=churn_probability,
        revenue_before=revenue_before,
        memory_store=memory_store
    )

    for k, v in decision1.items():
        print(f"{k.upper()}: {v}")

    print("\n--- SECOND DECISION (AFTER MEMORY) ---")
    decision2 = run_memory_enabled_decision(
        customer_id="C002",
        customer_profile=customer_profile,
        churn_probability=churn_probability,
        revenue_before=revenue_before,
        memory_store=memory_store
    )

    for k, v in decision2.items():
        print(f"{k.upper()}: {v}")
