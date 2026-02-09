# Memory-Enabled Agentic AI System (Adaptive Decision Intelligence)

## Overview
This project implements a memory-enabled Agentic AI system capable of adapting decisions based on historical performance.

Unlike static decision systems, this architecture introduces episodic memory and feedback-driven planning, allowing agents to learn from past outcomes and improve future strategies.

---

## Problem
Most AI decision systems treat each case independently.  
This project addresses that limitation by enabling agents to:

- Store past decisions
- Evaluate outcomes based on revenue impact
- Compute historical success rates
- Adapt future strategies using experience

---

## Architecture

### Core Components
- **Memory Store** – Logs decision episodes and revenue outcomes  
- **Memory Manager** – Computes success rates and identifies best-performing strategies  
- **Adaptive Planner Agent** – Selects actions using historical performance  
- **Explainer Agent** – Produces decision summaries  

### Execution Flow

---

## Learning Mechanism
- Success defined as revenue increase  
- Historical success rates guide future action selection  
- Planner overrides static rules when memory data exists  

---

## Key Features
- Episodic memory tracking  
- Revenue-based success evaluation  
- Adaptive planning logic  
- Feedback loop integration  
- Modular, extensible architecture  

---

## Tech Stack
Python · Multi-agent architecture · In-memory episodic storage

---

## Positioning
This project demonstrates early-stage autonomous behavior in Agentic AI systems through feedback-driven adaptation and experience-aware planning.
