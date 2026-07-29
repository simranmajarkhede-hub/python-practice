import pandas as pd

# Step 1: Create DataFrame
students = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan", "Pooja"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [85, 90, 78, 88, 92, 75],
    "City": ["Pune", "Mumbai", "Nagpur", "Delhi", "Nashik", "Pune"]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

# Step 2: Students with Marks greater than 80
print("\n===== Marks > 80 =====")
print(df[df["Marks"] > 80])

# Step 3: Students from Pune
print("\n===== Students from Pune =====")
print(df[df["City"] == "Pune"])

# Step 4: Students Age greater than or equal to 21
print("\n===== Age >= 21 =====")
print(df[df["Age"] >= 21])

# Step 5: Multiple Conditions
print("\n===== Marks > 80 AND City = Pune =====")
print(df[(df["Marks"] > 80) & (df["City"] == "Pune")])

# Step 6: Sort by Marks (Ascending)
print("\n===== Sort by Marks (Ascending) =====")
print(df.sort_values(by="Marks"))

# Step 7: Sort by Marks (Descending)
print("\n===== Sort by Marks (Descending) =====")
print(df.sort_values(by="Marks", ascending=False))

# Step 8: Sort by Name
print("\n===== Sort by Name =====")
print(df.sort_values(by="Name"))