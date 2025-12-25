# ================================
# Customer Support Ticket Triage System
# ================================
# Indha project customer support tickets-a
# automatically classify, priority assign,
# SLA calculate panni final report generate pannum

# ---- Required libraries import pannrom ----
import pandas as pd          # CSV data handle panna
import re                    # Text clean panna
from datetime import datetime, timedelta  # Time & SLA calculation

# ---- Dataset load pannrom ----
# Local Windows system-la irukkura CSV file path
df = pd.read_csv(
    r"C:\Users\Admin\Desktop\nasa internship\Week 1\customer_support_tickets.csv"
)

# Dataset first 5 rows paakrom
print(df.head())

# Dataset size (rows, columns) paakrom
print(df.shape)

# ---- Dataset columns list paakrom ----
# Real-world dataset-la column name vary aagum
print("Columns:", df.columns)

# ---- Possible message column names ----
# Ticket text irukkura column edhu nu kandupidikka
possible_message_cols = [
    'message',
    'Message',
    'Ticket Description',
    'Customer Query',
    'Issue Description',
    'Support Message',
    'Ticket Text'
]

# ---- Actual message column auto-detect pannrom ----
for col in possible_message_cols:
    if col in df.columns:
        message_col = col
        break
else:
    # Endha message column-um illena error throw pannum
    raise Exception("Message column not found in dataset")

print("Using message column:", message_col)

# ---- Text clean panna function ----
# lowercase, special characters remove,
# extra spaces clean pannrom
def clean_text(text):
    text = str(text).lower()                   # lowercase convert
    text = re.sub(r'[^a-z0-9 ]', '', text)     # special characters remove
    text = re.sub(r'\s+', ' ', text).strip()   # extra spaces remove
    return text

# Cleaned message new column-la store pannrom
df['clean_message'] = df[message_col].apply(clean_text)

# ---- Issue classification function ----
# keywords base panni issue type decide pannrom
def classify_issue(text):
    if 'payment' in text or 'card' in text:
        return 'PAYMENT'
    elif 'login' in text or 'password' in text:
        return 'LOGIN'
    elif 'delivery' in text or 'shipping' in text:
        return 'DELIVERY'
    elif 'refund' in text:
        return 'REFUND'
    elif 'error' in text or 'bug' in text:
        return 'BUG'
    else:
        return 'GENERAL'

# Issue type column create pannrom
df['issue_type'] = df['clean_message'].apply(classify_issue)

# ---- Priority assign panna function ----
# Urgency keywords irundhaa higher priority
def assign_priority(text):
    if 'urgent' in text or 'immediately' in text:
        return 'P0'   # Critical
    elif 'asap' in text or 'soon' in text:
        return 'P1'   # High
    elif 'delay' in text:
        return 'P2'   # Medium
    else:
        return 'P3'   # Low

# Priority column create pannrom
df['priority'] = df['clean_message'].apply(assign_priority)

# ---- SLA hours calculate panna function ----
# Priority base panni response time decide pannrom
def sla_hours(priority):
    if priority == 'P0':
        return 2
    elif priority == 'P1':
        return 6
    elif priority == 'P2':
        return 24
    else:
        return 48

# SLA hours column add pannrom
df['sla_hours'] = df['priority'].apply(sla_hours)

# ---- Ticket created time & due time ----
# Current time ticket created time-aa set pannrom
df['created_time'] = datetime.now()

# SLA hours add panni due time calculate pannrom
df['due_time'] = df['created_time'] + df['sla_hours'].apply(
    lambda x: timedelta(hours=x)
)

# ---- Final report export ----
# Support manager use panna CSV generate pannrom
df.to_csv("final_ticket_report.csv", index=False)

print("Project completed successfully")
print("final_ticket_report.csv created")
