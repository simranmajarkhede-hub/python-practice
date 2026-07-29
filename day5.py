import pandas as pd

students = pd.DataFrame({
    "ID":[101,102,103,104,105],
    "Name":["Amit","Priya","Rahul","Sneha","Rohan"],
    "Department":["IT","IT","HR","HR","Sales"]
})

marks = pd.DataFrame({
    "ID":[101,102,103,104,105],
    "Marks":[85,92,78,88,90]
})

result = pd.merge(students, marks, on="ID")

print("Merged Data")
print(result)

print("\nAverage Marks by Department")
print(result.groupby("Department")["Marks"].mean())

print("\nDepartment Count")
print(result["Department"].value_counts())

pivot = result.pivot_table(values="Marks",
                           index="Department",
                           aggfunc="mean")

print("\nPivot Table")
print(pivot)

pivot.to_csv("student_report.csv")

print("\nReport Saved Successfully")