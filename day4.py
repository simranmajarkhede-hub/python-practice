import pandas as pd

student = {
    "Name": ["Amit", "Priya", "Rahul", None, "Sneha", "Rahul"],
    "Age": [20, 21, None, 22, 20, None],
    "Marks": [85, 90, 75, 60, None, 75]
}

df = pd.DataFrame(student)

print("Original Data")
print(df)

print("\nMissing Values")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(0)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].fillna("Unknown")

df = df.drop_duplicates()

df = df.sort_values(by="Marks", ascending=False)

df = df.rename(columns={"Marks": "Score"})

print("\nClean Data")
print(df)

df.to_csv("clean_students.csv", index=False)

print("\nData Saved Successfully!")