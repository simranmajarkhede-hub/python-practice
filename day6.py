import pandas as pd

student = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [85, 92, 78, 88, 90],
    "City": ["Nagpur", "Pune", "Mumbai", "Nagpur", "Pune"]
}

df = pd.DataFrame(student)

df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print("Student Data")
print(df)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nStudents Scoring Above 85")
print(df[df["Marks"] > 85])

print("\nStudents from Nagpur")
print(df[df["City"] == "Nagpur"])

df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 90 else
              "B" if x >= 80 else
              "C" if x >= 70 else
              "D"
)

print("\nFinal Report")
print(df)

df.to_csv("student_report.csv", index=False)

print("\nReport Saved Successfully!")