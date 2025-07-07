#Calculating the Grade
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >=80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

#Checking the honor roll or not
def honor_roll_eligibility(marks, average):
    if average >= 90 and all(mark >= 85 for mark in marks):
        return True
    return False

#display the summary
def display_student_summary(name, total, average, grade, honor_roll):
    print("\n---Student Performance Summary---")
    print(f"Name : {name}")
    print(f"Total Marks : {total}")
    print(f"Average Marks : {average:.2f}")
    print(f"Grade : {grade}")
    if honor_roll:
        print("Congratulations! You have qualified for the Honor Roll.")
    else :
        print("You did not qualify for the Honor Roll this time.")
    print("------------------------------\n")


#This is the main program
print("Welcome to the Student Grading System!")

#Taken input
name = input("Enter the Studen's name: ")
marks = []
for i in range(1,4):
    mark = float(input(f"Enter marks for subject {i} (0 - 100): "))
    marks.append(mark)


total_marks = sum(marks)  # calcultaing the total
average_marks = total_marks / len(marks) #calculating the average

grade = calculate_grade(average_marks) # calculating the grade
honor_roll = honor_roll_eligibility(marks, average_marks) #calculating is it honor roll or not

#display the summary
display_student_summary(name, total_marks, average_marks, grade, honor_roll) 