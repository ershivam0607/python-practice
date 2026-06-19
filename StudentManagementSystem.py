name = input(("Enter your name: "))
print(f"Hello {name}. Welcome to our Student Management System.\n Follow the instructions.")
students = []
while(True):
    print("Press 1 to add students.")
    print("Press 2 to search a student.")
    print("Press 3 to update a student.")
    print("Press 4 to view all the students.")
    print("Press 5 to delete a  student.")
    print("Press 6 to exit.")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        no = int(input("Enter number of students you want to add: "))
        for i in range(0,no):
            st_name = input("Enter name of the student: ")
            roll = input(f"Enter roll of student {st_name}: ")
            marks = input(f"Enter marks of student {st_name}: ")
            student_detail = {"name":st_name, "roll":roll, "marks":marks}
            students.append(student_detail)
    elif(choice==2):
        roll = input("Enter roll number of the student you want to search: ")
        for i in students:
            if(i["roll"]==roll):
                print("name: ",i["name"])
                print("roll: ",i["roll"])
                print("marks: ",i["marks"])
                break
        else:
            print("No Student found with the given roll number")
    elif(choice==3):
        roll = input("Enter roll number of the student you want to update: ")
        for i in students:
            if(i["roll"]==roll):
                mark_up = int(input("Enter Marks to update: "))
                i.update({"marks":mark_up})
                break
        else:
            print("No Student found with the given roll number")
    elif(choice==4):
        print("List of all students: ")
        for i in students:
            print("name: ",i["name"])
            print("roll: ",i["roll"])
            print("marks: ",i["marks"])
            print("_"*45)
    elif(choice==5):
        roll = input("Enter roll number of the student you want to delete: ")
        for i in students:
            if(i["roll"]==roll):
                students.remove(i)
                break
        else:
            print("No Student found with the given roll number")
    elif(choice==6):
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")