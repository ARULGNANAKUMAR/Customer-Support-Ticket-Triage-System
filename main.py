import pandas as pd
import re
from datetime import datetime, timedelta

df = pd.read_csv(
    r"C:\Users\Admin\Desktop\nasa internship\Week 1\customer_support_tickets.csv"
)

print(df.head())
print(df.shape)

print("Columns:", df.columns)

possible_message_cols = [
    'message',
    'Message',
    'Ticket Description',
    'Customer Query',
    'Issue Description',
    'Support Message',
    'Ticket Text'
]

for col in possible_message_cols:
    if col in df.columns:
        message_col = col
        break
else:
    raise Exception(" Message column not found in dataset")

print("Using message column:", message_col)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9 ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['clean_message'] = df[message_col].apply(clean_text)

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

df['issue_type'] = df['clean_message'].apply(classify_issue)

def assign_priority(text):
    if 'urgent' in text or 'immediately' in text:
        return 'P0'
    elif 'asap' in text or 'soon' in text:
        return 'P1'
    elif 'delay' in text:
        return 'P2'
    else:
        return 'P3'

df['priority'] = df['clean_message'].apply(assign_priority)

def sla_hours(priority):
    if priority == 'P0':
        return 2
    elif priority == 'P1':
        return 6
    elif priority == 'P2':
        return 24
    else:
        return 48

df['sla_hours'] = df['priority'].apply(sla_hours)

df['created_time'] = datetime.now()
df['due_time'] = df['created_time'] + df['sla_hours'].apply(
    lambda x: timedelta(hours=x)
)

df.to_csv("final_ticket_report.csv", index=False)

print("Project completed successfully")
print("final_ticket_report.csv created")

