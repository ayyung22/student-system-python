#  Student Grades Management System
# • Create a program that allows users to input student names and grades. The program should be
# able to calculate the class average, highest and lowest grades, and display all students' grades.
# • Bonus: Add features such as grade categorization (e.g., A, B, C) and handling missing data.
# • Focus Areas: Lists, dictionaries, loops, conditional logic, and file handling (optional).


# THIS FUNCTION WILL ADD STUDENT INFORMATION.
# THE INFORMATION ADDED WILL BE STORE IN THE STUDENT LIST, AND CAN BE DISPLAY OR SEARCH LATER.
# START BY ASSUMING THE STUDENT IS NOT IN THE SYSTEM.
# THE P VARIABLE WILL CHECK IF THE STUDENT-ID IS ALREADY EXIST, TO AVOID REPEAT VALUES.
def add_std():
    found = False  # Start by assuming the student is not found
    print()
    print("--------------------")
    student_Id = input("Enter Student_Id: ")

    # Check if the student ID already exists
    for p in student:
        if student_Id == p["Student_Id"]:
            found = True  # Student ID found, so no need to add again
            break

    # If not found, add a new student
    if not found:
        name = input("Enter Name: ")
        sub = input("Enter Subject: ")
        grade = input("Enter Grade: ")
        rec = {"Student_Id": student_Id, "Name": name, "Subject": sub, "Grade": grade}
        student.append(rec)
        print("--------------------")
        print("Student record added successfully!")
        print("--------------------")
    else:
        print()
        print("--------------------")
        print("Student-ID is already in the system.")
        print("--------------------")
        print()


# THIS FUNCTION WILL DISPLAY STUDENT INFORMATION.
# THE FOR LOOP IS IMPLEMENTED IN THIS FUNCTION IN ORDER TO DISPLAY STUDENT INFORMATION.
# THE FOR LOOP WILL BE EXECUTED 10 TIMES.
# THE VARIABLE i IS DECLARED TO STORE STUDENT LIST THAT CONTAIN ALL STUDENT DATA.
# NULL PRINT FUNCTION CONTAIN EMPTY STRING AND IS IMPLEMENT HERE TO SEPARATE ONE OUTPUT TO OTHER OUTPUT.

def dis_std():
    found = False
    print()
    print("--------------------------------")
    for i in student:
        found=True
        print("Student_Id: ",i["Student_Id"])
        print("Name: ", i["Name"])
        print("Subject: ", i["Subject"])
        print("Grade: ", i["Grade"])
        print("--------------------")
        print()
        break

    if found == False:
        print()
        print("-----------------------------------------")
        print("No Student data Found. Please Add Student")
        print("-----------------------------------------")
        print()


# THIS DEFINE THE SEARCH FUNCTION THAT WILL BE SEARCH FOR THE INFORMATION OF A SPECIFIC STUDENT.
# usi (USER STUDENT ID) IS A FUNCTION THAT WILL HELP TO MATCH WHEN THE USER SEARCH WITH THE STUDENT ID THAT IS STORE IN THE STUDENT LIST.
# IF THERE IS AN INVALID STUDENT ID, THE USER WILL BE GET A MESSAGE.
def search():
    found=False
    print()
    print("--------------------------------")
    usi=input("Enter a Specific Student Id:")
    for j in student:
        if usi==j["Student_Id"]:
            found=True
            print("Student_Id: ", j["Student_Id"])
            print("Name: ", j["Name"])
            print("Subject: ", j["Subject"])
            print("Grade: ", j["Grade"])
            print("--------------------")
            print()
            break
    if found == False:
        print()
        print("--------------------")
        print("Student Not Found")
        print("--------------------")
        print()


#
# THERE ARE 4 OPTIONS THAT THE USER CAN CHOOSE.
# THE PRINT FUNCTION DISPLAY THE DIFFERENT OPTIONS FOR THE USER.
# IF THERE IS AN INVALID VALUE, THE USER WILL BE GET A MESSAGE.

student=[]
print()
print("-----------------------------------------------")
print("Welcome to the Student Grades Management System")
print("------------------------------------------------")
print()
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("0. Exit")
    op=int(input("Enter Your Choice: "))
    print("--------------------")
    print()

    if op==1:
        add_std()
    elif op==2:
        dis_std()
    elif op==3:
        search()
    elif op==0:
        print("Thank you, have a nice day! \n")
        break

    #elif op==0:
     #   break
    else:
        print()
        print("--------------------")
        print("Invalid input")
        print("--------------------")
        print()