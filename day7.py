import pandas as pd
import matplotlib.pyplot as plt

student = {
    "Name": ["Amit","Priya","Rahul","Sneha","Rohan"],
    "Marks": [85,92,78,88,90]
}

df = pd.DataFrame(student)

print(df)

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Line Chart
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Performance")
plt.show()

# Pie Chart
plt.pie(df["Marks"],
        labels=df["Name"],
        autopct="%1.1f%%")
plt.title("Marks Percentage")
plt.show()

# Histogram
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

print("Visualization Completed Successfully!")