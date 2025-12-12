📌 Project Overview

This project simulates a real IT Help Desk environment by combining ticket data, troubleshooting documentation, and automation scripts. It demonstrates my ability to:
	•	Diagnose and resolve technical issues
	•	Document processes clearly and professionally
	•	Write automation scripts in Python and Bash
	•	Organize and manage IT operations workflows
	•	Apply structured troubleshooting methods
	•	Work with real-world ticketing concepts used in IT support teams
	# IT Support Ticket Simulator

A simulated IT help desk ticketing environment demonstrating practical troubleshooting, automation, and documentation skills for IT Support, Help Desk, and Systems Administration roles.

This repo contains:
- `tickets.csv` — sample dataset (25 realistic tickets)
- `generate_ticket.sh` — Bash script to generate a new fake ticket
- `assign_tickets.py` — Python script to auto-assign open tickets and generate `dashboard.md`
- `playbook/` — troubleshooting checklists for common categories
- `dashboard.md` — auto-generated summary (created by `assign_tickets.py`)

---

## Quick start (Linux / macOS / WSL)

1. Clone the repo:
```bash
git clone https://github.com/sturull/it-support-ticket-simulator.git
cd it-support-ticket-simulator
  2.	Make the generator executable (one-time on your machine):
chmod +x generate_ticket.sh
	3.	Inspect the sample tickets:
head -n 10 tickets.csv
	4.	Create a new ticket:
./generate_ticket.sh
This appends a new ticket to tickets.csv and prints the new ticket ID.
	5.	Assign unassigned tickets and build the dashboard:
python3 assign_tickets.py
This script:
	•	Assigns open/unassigned tickets to a short list of agents
	•	Updates tickets.csv with assigned_to values
	•	Writes dashboard.md with counts by priority, category, and agent

	6.	View the dashboard:
cat dashboard.md
Demo script (what to show in an interview)
	1.	Show README.md and playbook/ to demonstrate process & SOPs.
	2.	Open tickets.csv and explain ticket fields (id, priority, category).
	3.	Run ./generate_ticket.sh to show a ticket being created live.
	4.	Run python3 assign_tickets.py to auto-assign and produce dashboard.md.
	5.	Open dashboard.md to discuss ticket distribution, priorities, and recent tickets.
	6.	Explain how this could connect to Slack/email notifications, a Flask UI, or a database.

⸻

Files & purpose (short)
	•	tickets.csv — dataset of realistic support tickets
	•	generate_ticket.sh — creates a new fake ticket (bash)
	•	assign_tickets.py — assigns tickets & generates dashboard.md (python)
	•	playbook/ — troubleshooting guides (Wi-Fi, hardware, email, phishing)
	•	dashboard.md — a human-readable ticket summary (auto-generated)

⸻

Requirements
	•	Python 3.7+
	•	Bash shell (Linux / macOS / WSL)
	•	Optional: Git (for cloning and local changes)

⸻

Extend this project (ideas)
	•	Add a simple Flask UI to view and change ticket status
	•	Replace CSV with SQLite for persistence and history
	•	Add Slack or email notification simulation for critical tickets
	•	Add SLA timers and escalation rules

⸻

Contact / About

Built by Samantha Turull — IT & Cybersecurity professional.
GitHub: https://github.com/sturull
LinkedIn: https://www.linkedin.com/in/samantha-t-2a9644307
