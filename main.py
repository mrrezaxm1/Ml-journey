import pandas as pd

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Sara", "Reza", "Mina", "Hossein"],
    "department": ["IT", "HR", "IT", "Finance", "IT"]
})

salaries = pd.DataFrame({
    "emp_id": [1, 2, 4],
    "salary": [45000, 52000, 110000]
})

merged = employees.merge(salaries, on="emp_id", how="left")
print(merged)

print(merged.isna().sum())
print(merged["salary"].mean())
print(merged["salary"].dropna().mean())