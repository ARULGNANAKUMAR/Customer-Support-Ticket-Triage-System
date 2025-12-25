# Customer Support Ticket Triage System

# Project Overview
Companies receive thousands of customer support tickets every day. Some issues are urgent and require immediate attention, while others can be handled later.  
This project automates the **initial triage of customer support tickets** by cleaning ticket messages, identifying issue types, assigning priority levels, calculating SLA deadlines, and generating a final report for support managers.

This project is developed as part of **Week-1 Internship Training** to simulate real-world industry workflows using Python.

# Objectives
- To understand how real customer support data is processed
- To clean and preprocess unstructured text data
- To classify customer issues using rule-based logic
- To assign priority levels based on urgency
- To calculate SLA response times and due dates
- To generate a manager-ready CSV report

# Tools & Technologies Used
- **Python 3**
- **Pandas** – data analysis and manipulation
- **Regular Expressions (re)** – text cleaning
- **Datetime** – SLA and due time calculation
- **Google Colab / Local Python Environment**
- **GitHub** – version control and project submission

# Dataset Description
The dataset contains real-world styled customer support ticket data with the following key fields:
- Ticket ID
- Ticket Subject
- Ticket Description (used as main message text)
- Ticket Type
- Ticket Status
- Ticket Priority
- Customer Details
- Response & Resolution Time
- Customer Satisfaction Rating

Total Records: **8469 tickets**

---

## ⚙️ Project Workflow

# Data Loading
- Load CSV dataset using Pandas
- Validate rows, columns, and missing values

# Data Cleaning
- Convert text to lowercase
- Remove special characters
- Remove extra spaces
- Handle missing values safely

# Issue Classification (Rule-Based)
Tickets are classified into the following categories:
- PAYMENT
- LOGIN
- DELIVERY
- REFUND
- BUG
- GENERAL  

Classification is done using keyword-based logic.

# Priority Assignment
Each ticket is assigned a priority based on urgency keywords:
- **P0** – Critical / Immediate
- **P1** – High
- **P2** – Medium
- **P3** – Low

# SLA Calculation
Service Level Agreement (SLA) hours are assigned based on priority:
| Priority | SLA Hours |
|--------|-----------|
| P0 | 2 hours |
| P1 | 6 hours |
| P2 | 24 hours |
| P3 | 48 hours |

A due date is calculated automatically for each ticket.

# Final Report Generation
- All processed data is combined into a final dataframe
- Exported as **final_ticket_report.csv**
- Ready for support managers and analysis teams

# Output Files
**final_ticket_report.csv**  
  Contains:
  - Cleaned ticket message
  - Issue type
  - Priority level
  - SLA hours
  - Ticket due time

# Key Features
- Handles real-world messy datasets
- Dynamic detection of message column
- Rule-based automation (no hardcoding)
- Industry-style data processing workflow
- Clean, readable, and well-commented code

# Learning Outcomes
- Practical experience with Pandas
- Understanding of customer support workflows
- Real-world problem solving with Python
- GitHub project structuring and documentation
- Writing production-style, readable code

# Internship Context
This project is part of **Week-1 Internship Training** and focuses on:
- Professional GitHub usage
- Clean coding practices
- Real-world data handling
- Industry-level problem solving

# Author
**Arul Gnanakumar**  
Python Intern | Learning Data & AI  

# Note
This project uses **rule-based logic** for simplicity and learning purposes.  
In real production systems, machine learning or NLP models may be used for advanced classification.
