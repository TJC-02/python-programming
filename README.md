# Python Programming

A collection of Python applications built for practice. Each application provides hands-on experience with Python concepts, problem solving, and writing runnable programs.

This repository grows as new applications are added and existing ones are improved while learning.

## Applications

| Application | Description | Concepts demonstrated |
| --- | --- | --- |
| [Course List](course_list_2d.py) | A Python course-list example. | Two-dimensional lists. |
| [Grade Calculator](grade_calculator_python.py) | Converts a numeric percentage into a letter grade using the program's custom grading scale. | Variables, strings, f-strings, input/output, float conversion, rounding, comparisons, and if/elif conditionals. |

## Run an application

Install Python 3, then run this command from the repository root:

```bash
python grade_calculator_python.py
```

Use `python3` if that is your Python command. No third-party packages are required.

Enter a percentage such as `96.25` (meaning 96.25%, rather than 0.9625).

## Add more applications

1. Add a new `.py` file to this folder using a descriptive filename such as `loops_example.py`.
2. Add a row to the table above describing its purpose and the concepts it demonstrates.
3. Run the application and commit the file and README update.

Future applications could explore loops, functions, lists, dictionaries, file handling, and exceptions.

## Grade calculator development notes

The calculator is preserved as originally uploaded. Its current conditional chain does not assign a grade when the rounded input is from 68 through 72.99, causing a `NameError`. The intended grade for that interval needs to be defined in a future revision. Non-numeric input also raises an error, and percentages outside 0–100 are not rejected.
