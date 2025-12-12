import csv
from datetime import datetime

CSV_FILE = "tickets.csv"
DASHBOARD_FILE = "dashboard.md"

# Support agents to simulate assignments
AGENTS = ["Samantha", "Alex", "Jordan", "Taylor", "Morgan"]

def load_tickets():
    tickets = []
    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tickets.append(row)
    return tickets

def save_tickets(tickets):
    fieldnames = ["ticket_id","created_at","submitter","category","subcategory",
                  "summary","details","status","priority","assigned_to"]
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for t in tickets:
            writer.writerow(t)

def assign_unassigned_tickets(tickets):
    agent_index = 0
    for ticket in tickets:
        if ticket["assigned_to"] == "" or ticket["assigned_to"] is None:
            ticket["assigned_to"] = AGENTS[agent_index % len(AGENTS)]
            agent_index += 1
    return tickets

def build_dashboard(tickets):
    total = len(tickets)
    open_tickets = [t for t in tickets if t["status"] == "open"]

    # Count by priority
    prio_counts = {}
    for p in ["Critical","High","Medium","Low"]:
        prio_counts[p] = len([t for t in tickets if t["priority"] == p])

    # Count by category
    categories = {}
    for t in tickets:
        cat = t["category"]
        categories[cat] = categories.get(cat, 0) + 1

    # List 5 newest open tickets
    sorted_open = sorted(open_tickets, key=lambda x: x["created_at"], reverse=True)
    latest_open = sorted_open[:5]

    with open(DASHBOARD_FILE, "w") as f:
        f.write("# Ticket Dashboard\n\n")
        f.write(f"Generated: {datetime.now()}\n\n")
        f.write(f"**Total Tickets:** {total}\n\n")

        f.write("## Tickets by Priority\n")
        for p, count in prio_counts.items():
            f.write(f"- **{p}:** {count}\n")
        f.write("\n")

        f.write("## Tickets by Category\n")
        for c, count in categories.items():
            f.write(f"- **{c}:** {count}\n")
        f.write("\n")

        f.write("## Most Recent Open Tickets\n")
        for t in latest_open:
            f.write(f"- {t['ticket_id']} — {t['summary']} ({t['priority']})\n")

def main():
    tickets = load_tickets()
    tickets = assign_unassigned_tickets(tickets)
    save_tickets(tickets)
    build_dashboard(tickets)
    print("Tickets assigned and dashboard generated:", DASHBOARD_FILE)

if __name__ == "__main__":
    main()
