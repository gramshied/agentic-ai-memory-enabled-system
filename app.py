from agents.analyst import AnalystAgent
from agents.planner import PlannerAgent
from agents.critic import CriticAgent
from agents.explainer import ExplainerAgent

from agents.tool_selector import ToolSelectorAgent
from agents.tool_executor import ToolExecutorAgent
from agents.validator import ValidatorAgent


def run_tool_using_agentic_decision(customer_profile, churn_probability, discount_percentage):
    # Instantiate agents
    analyst = AnalystAgent()
    planner = PlannerAgent()
    tool_selector = ToolSelectorAgent()
    tool_executor = ToolExecutorAgent()
    validator = ValidatorAgent()
    explainer = ExplainerAgent()

    # Step 1: Risk analysis
    analysis = analyst.analyze(customer_profile, churn_probability)

    # Step 2: Initial planning
    plan = planner.plan(analysis)
    proposed_actions = plan["recommended_actions"]

    # Step 3: Tool selection
    tool_plan = tool_selector.select_tools(
        analysis,
        proposed_discount_percentage=discount_percentage
    )

    # Step 4: Tool execution (facts)
    execution_results = {}
    if tool_plan:
        execution_results = tool_executor.execute(tool_plan)

    # Step 5: Validation (finance authority)
    validation = validator.validate(proposed_actions, execution_results)

    # Step 6: Explanation
    explanation = explainer.explain(
        analysis=analysis,
        plan=plan,
        critique={
            "approved": validation["approved"],
            "final_actions": validation["final_actions"],
            "concerns": validation["validation_notes"]
        }
    )

    # Attach finance facts if present
    if "finance_summary" in execution_results:
        explanation["finance_summary"] = execution_results["finance_summary"]

    return explanation


if __name__ == "__main__":
    # Example input
    customer_profile = {
        "tenure": 4,
        "contract": "Month-to-month",
        "monthly_charges": 3000,
        "internet_service": "Fiber optic"
    }

    churn_probability = 0.62
    proposed_discount_percentage = 20  # %

    decision = run_tool_using_agentic_decision(
        customer_profile,
        churn_probability,
        proposed_discount_percentage
    )

    print("\n=== LEVEL 2: TOOL-USING AGENTIC AI DECISION ===\n")
    for key, value in decision.items():
        print(f"{key.upper()}:\n{value}\n")
