

def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} marks: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid marks! Enter a number between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Collect student information
name = input("Enter student name: ")

print("\nWelcome", name)
print("Enter marks between 0 and 100.")

# Collect valid marks
math = get_valid_mark("Mathematics")
computer = get_valid_mark("Computer Science")
english = get_valid_mark("English")

# Calculate total and average
total = math + computer + english
average = total / 3

# Assign grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Determine pass or fail
if average >= 50:
    status = "PASS"
else:
    status = "FAIL"

# Display results
print("\n========== STUDENT RESULTS ==========")
print("Student Name:", name)
print("Mathematics:", math)
print("Computer Science:", computer)
print("English:", english)
print("-------------------------------------")
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Status:", status)
print("=====================================")
