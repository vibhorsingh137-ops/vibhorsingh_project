import numpy as np
import pandas as pd

# List
names = ["Aman", "Rahul", "Priya", "Riya", "Vikash"]

# Tuple
subjects = ("Math", "English", "Science")

# Set
classes = {10, 11, 12}

# Dictionary
student = {
    "Aman": [80, 70, 90],
    "Rahul": [60, 75, 80],
    "Priya": [90, 85, 95],
    "Riya": [70, 80, 75],
    "Vikash": [55, 65, 60]
}

# Function for total
def total(marks):
    return sum(marks)

# Function for average
def average(marks):
    return np.mean(marks)

# Function for result
def result(marks):
    if min(marks) >= 33:
        return "Pass"
    else:
        return "Fail"

# Create DataFrame
data = []

for name, marks in student.items():

    data.append({
        "Name": name,
        "Math": marks[0],
        "English": marks[1],
        "Science": marks[2],
        "Total": total(marks),
        "Average": average(marks),
        "Result": result(marks)
    })

df = pd.DataFrame(data)

# Display data
print(df)

# NumPy array
arr = np.array(list(student.values()))

print("\n2D Array:")
print(arr)

# Indexing and slicing
print("\nFirst student marks:")
print(arr[0])

print("\nFirst 2 students:")
print(arr[:2])

# Analysis
print("\nHighest Marks:", np.max(arr))
print("Lowest Marks:", np.min(arr))
print("Class Average:", np.mean(arr))

# Save CSV
df.to_csv("students.csv", index=False)

# Read CSV
new_df = pd.read_csv("students.csv")

print("\nCSV File Data:")
print(new_df)

# Pandas filtering
print("\nStudents who passed:")
print(df[df["Result"] == "Pass"])

# Sorting
print("\nTop Students:")
print(df.sort_values("Total", ascending=False))

# Dictionary methods
print("\nStudent Names:")
print(student.keys())

print("\nTotal Students:", len(names))