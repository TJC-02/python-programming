def display_menu():
	print("The Course List Program V.2")
	print("COMMAND MENU")
	print("list - lists all courses")
	print("add - adds a course")
	print("del - deletes a course")
	print("exit - Exits the program")
	print()

def list_courses(my_course_list):
    if len(my_course_list) == 0:
        print("There are no courses in the list.\n")
    else:
        my_course_number = 1
        for course in my_course_list:
            print(my_course_number, str(course[0]), course[1], "(" + str(course[2]) + " Credits)")
            my_course_number = my_course_number + 1
        print()

def add_courses(my_course_list):
    course_number = input("Course #: ")
    course_name = input("Course Name: ")
    credits = input("Credits: ")
    my_course = [course_number, course_name, credits]
    my_course_list.append(my_course)
    print(f"{my_course[0]} was added.\n")

def delete_courses(my_course_list):
	my_course_number = int(input("Enter the number of the course you would like to delete: "))
	
	if my_course_number < 1 or my_course_number > len(my_course_list):
		print("Invalid course number.\n")
	else:	
		my_course = my_course_list.pop(my_course_number - 1)
		print(f"{my_course[0]} was deleted.\n")

def main():
    courses = [["CIST 3470", "Programming in Python", "4"],
                    ["CIST 2010", "Computer Information Systems: An Overview", "4"],
                    ["CIST 3450", "Business Intelligence", "4"]]

    display_menu()

    while True:
        command = input("Commad: ")

        if command.lower() == "exit":
            break

        if command.lower() == "list":
            list_courses(courses)
        elif command.lower() == "add":
            add_courses(courses)
        elif command.lower() == "del":
            delete_courses(courses)
        else:
            print("Not a valid command. Try again.\n")

    print("Have a nice day!")
if __name__ == "__main__": 
    main()