import pandas as pd

def generate_monthly_report(transactions):
  df = pd.DataFrame(transactions)
  df.to_excel("monthly_report.xlsx", index=False)
  return "monthly_report.xlsx"