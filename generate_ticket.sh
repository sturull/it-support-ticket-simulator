#!/bin/bash

# File: generate_ticket.sh
# Purpose: Generate a new fake IT ticket and append it to tickets.csv

CSV_FILE="tickets.csv"

if [[ ! -f "$CSV_FILE" ]]; then
    echo "Error: tickets.csv not found!"
    exit 1
fi

# Generate a new ticket ID based on the number of lines
NEXT_ID=$(($(wc -l < "$CSV_FILE")))
TICKET_ID=$(printf "TCKT-%03d" "$NEXT_ID")

TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
SUBMITTERS=("Susan M" "Devon P" "Alex R" "Kelly G" "Mark T" "Olivia S" "Jason B" "Erika L" "Victor H" "Nina K")
CATEGORIES=("Networking" "Hardware" "Software" "Access" "Security")
SUBCATEGORIES=("Wi-Fi" "Laptop" "Email" "Permissions" "Phishing" "VPN" "Printer" "Switch" "Browser" "Storage")
SUMMARIES=("System running slow" "Wi-Fi issues" "Application error" "Access denied" "Phishing suspicion" "Hardware malfunction")
DETAILS=("User reports intermittent issue." "Problem occurs randomly." "User attempted reboot but problem persists." "Needs investigation.")
PRIORITIES=("Low" "Medium" "High" "Critical")

# Pick random values
SUBMITTER=${SUBMITTERS[$RANDOM % ${#SUBMITTERS[@]}]}
CATEGORY=${CATEGORIES[$RANDOM % ${#CATEGORIES[@]}]}
SUBCATEGORY=${SUBCATEGORIES[$RANDOM % ${#SUBCATEGORIES[@]}]}
SUMMARY=${SUMMARIES[$RANDOM % ${#SUMMARIES[@]}]}
DETAIL=${DETAILS[$RANDOM % ${#DETAILS[@]}]}
PRIORITY=${PRIORITIES[$RANDOM % ${#PRIORITIES[@]}]}

# Append new ticket
echo "$TICKET_ID,$TIMESTAMP,$SUBMITTER,$CATEGORY,$SUBCATEGORY,$SUMMARY,\"$DETAIL\",open,$PRIORITY," >> "$CSV_FILE"

echo "New ticket created: $TICKET_ID"
