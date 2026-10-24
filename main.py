# ============================================================
# Project: ServiceNow Ticket Analytics
# Description:
# This Python project analyzes mock ServiceNow incident data
# to track ticket resolution rates, analyst performance,
# ticket volumes, and monthly trends.
#
# Dataset: January - December 2026
# Environment: 30 Analysts / ~20 calls per analyst daily
#
# Technologies: Python, pandas, openpyxl, Matplotlib
#
# Development Phases:
# Phase 1 - Data Import and Exploration
# Phase 2 - Ticket Analysis and Calculations
# Phase 3 - Reporting and Data Visualization
# Phase 4 - Interactive Dashboard
#
# Note: All ticket data is simulated for educational purposes.  NOT REAL DATA.
# ============================================================

import pandas as pd

# Read the excel file first, store it in a dataframe (df)
df = pd.read_excel("servicenow_mock_sample.xlsx")

# ================== test it first, =====================
# display the first 10 rows
print(df.head(10))
# display total number of tickets in the excel file. 
print(len(df))
# display all column names
print(df.columns)

# count ticket with given status
print((df["Status"] == "Resolved").sum())
print((df["Status"] == "On Hold").sum())

# count how many times each unique status appears in the column
print(df["Status"].value_counts())





