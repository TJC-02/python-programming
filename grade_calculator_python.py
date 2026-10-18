program_name = "Tyler's Grade Calculator"
developer_name = "Tyler"
date = "Sept. 13th, 2026"

print(f"Program name: {program_name}\n"
      f"Developer: {developer_name} \n"
      f"Date: {date}\n")

print("This program's purpose is to calculate a grade based on the given percentage...")
number_grade = round(float(input("Enter your grade percentage as a decimal to the nearest hundreth: ")), 2)

if number_grade >= 96:
	final_grade = (f"A+,\n" 
	               f"Nice!")
elif number_grade >= 93:
	final_grade = (f"A,\n"
	               f"Nice!")
elif number_grade >=90:
	final_grade = (f"A-,\n"
	               f"Nice!")
elif number_grade >=88:
	final_grade = (f"B+,\n"
	               f"Okay!")
elif number_grade >= 85:
	final_grade = (f"B,\n"
	               f"Okay!")
elif number_grade >= 83:
	final_grade = (f"B-,\n"
	               f"Okay!")
elif number_grade >= 80:
	final_grade = (f"C,\n"
	               f"Barely Passed.")
elif number_grade >= 73:
    final_grade = (f"D,\n"
                   f"Did not pass.")
elif number_grade < 68:
    final_grade = (f"F,\n"
                   f"Failed!")

print()
print(f"Final Grade:\n"
      f"{final_grade}")

 