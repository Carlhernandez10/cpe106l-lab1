student = {
  "id": "2025-001",
  "name": "Juan Dela Cruz",
  "grades": [86, 90, 85]
}

# To add new grades
student["grades"].append(92)

# To update the student's name
student["name"] = "Juan Dela Cruz Jr."

# To calculate the average grade
average = sum(student["grades"]) / len(student["grades"])

# Print the updated student record and average grade
print("Student ID: ", student["id"])
print("Student Name: ", student["name"])
print("Grades: ", student["grades"])
print("Average: ", average)