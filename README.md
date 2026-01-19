💸 SpendWise — A Mobile AI Agent for Preventive Expense Control

SpendWise is a mobile-native AI agent built using the Droidrun framework that automatically logs expenses from bank SMS, tracks daily spending in real time, and proactively warns users before they overspend.

Unlike traditional expense apps that rely on manual input, SpendWise demonstrates how agentic mobile automation can reduce friction and influence better financial behavior.

🎯 Problem Statement 

Consumers lose money not because they don’t want to save, but because:

Expense tracking is manual and inconsistent

Overspending is detected after it has already happened

Daily financial discipline is hard to maintain

This problem exists at scale and directly impacts personal financial health.

💡 Solution Overview

SpendWise uses an autonomous mobile agent to:

Detect payment events from bank SMS

Log expenses automatically on a mobile device

Maintain a real-time daily spending total

Warn users when they approach their daily limit

Reinforce good habits using a streak-based system

The agent acts on the user’s behalf, not just as a passive tracker.

🤖 Agentic Behavior (Droidrun Focus)

SpendWise demonstrates agentic intelligence through:

Goal-driven execution (track spending without user intervention)

Conditional decision-making (trigger alerts near limits)

Stateful behavior (daily totals and streaks)

Autonomous mobile actions via Droidrun

The agent adapts its behavior based on real-time spending patterns.

📲 Mobile Workflow Automated

The agent automates a real mobile workflow:

Reads payment SMS from the device

Extracts transaction amount

Opens a mobile expense interface

Logs the expense automatically

Sends proactive alerts when needed

This workflow runs on a real Android device / cloud device, aligned with Droidrun’s mobile-first philosophy.

⚙️ System Architecture
Mobile Device (SMS, Apps)
        ↓
Droidrun Agent
        ↓
Python Logic Layer
        ↓
State & Decision Engine (JSON)


Droidrun handles mobile UI interactions

Agent logic handles reasoning and state

Architecture is modular and extensible

🧠 Core Features (MVP)

✅ Automatic expense logging from SMS

✅ Real-time daily expense tracking

✅ Near-limit overspending alerts

✅ Discipline streak tracking

All features are implemented with clear agent autonomy, not hardcoded scripts.

🛠️ Tech Stack

Droidrun Framework — mobile agent execution

Python — agent logic and decision-making

JSON — lightweight state persistence

Mobilerun Cloud — device infrastructure (optional)

▶️ Running the Project
python main.py


The agent simulates SMS intake and executes the full decision flow.
When connected to Droidrun/Mobilerun, the same logic drives real mobile interactions.

🌱 Future Scope

Subscription leakage detection

Gamified visual streak growth (sapling → tree)

Personalized spending insights

Deeper mobile automation across finance apps

👥 Team

Manya

Aditya

🏁 DevSprint Alignment

SpendWise aligns with Droidrun DevSprint goals by:

Using Droidrun as a core mobile automation layer

Demonstrating agentic behavior on mobile devices

Solving a real-world consumer problem

Presenting a scalable, product-ready idea