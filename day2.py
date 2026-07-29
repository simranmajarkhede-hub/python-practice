
import pandas as pd

# Step 1: Create DataFrame
students = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 88, 92],
    "City": ["Pune", "Mumbai", "Nagpur", "Delhi", "Nashik"]
}

df = pd.DataFrame(students)

# Display complete DataFrame
print("===== Student Data =====")
print(df)

# Step 2: Select One Column
print("\n===== Step 2: Name Column =====")
print(df["Name"])

# Step 3: Select Multiple Columns
print("\n===== Step 3: Name and Marks =====")
print(df[["Name", "Marks"]])

# Step 4: Select Row using loc[]
print("\n===== Step 4: Row using loc[] =====")
print(df.loc[2])

# Step 5: Select Row using iloc[]
print("\n===== Step 5: Row using iloc[] =====")
print(df.iloc[3])

# Step 6: Select Rows 1 to 3
print("\n===== Step 6: Rows 1 to 3 =====")
print(df.iloc[1:4])

# Step 7: Select Specific Rows and Columns
print("\n===== Step 7: Name and Marks (Rows 1 to 3) =====")
print(df.loc[1:3, ["Name", "Marks"]])

# Step 8: Difference between loc[] and iloc[]
print("\n===== Step 8: loc[0:2] =====")
print(df.loc[0:2])

print("\n===== Step 8: iloc[0:2] =====")
print(df.iloc[0:2])