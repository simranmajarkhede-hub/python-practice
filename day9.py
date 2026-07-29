import pandas as pd

student = {
    "ID": [101,102,103,104,105],
    "Name": ["Amit","Priya","Rahul","Sneha","Rohan"],
    "Marks": [85,92,78,88,90],
    "City": ["Nagpur","Pune","Mumbai","Nagpur","Pune"]
}

df = pd.DataFrame(student)

print("Original Data")
print(df)

print("\nUsing loc")
print(df.loc[:, ["Name","Marks"]])

print("\nUsing iloc")
print(df.iloc[0:3, 0:3])

df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 90 else
              "B" if x >= 80 else
              "C"
)

df["City"] = df["City"].replace({
    "Nagpur":"Nagpur City",
    "Pune":"Pune City"
})

print("\nStudents with Marks > 85")
print(df.query("Marks > 85"))

print("\nSorted by Marks")
print(df.sort_values(by="Marks", ascending=False))

df.to_csv("advanced_student_report.csv", index=False)

print("\nReport Saved Successfully!")