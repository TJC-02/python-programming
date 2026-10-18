# Python Programming

A collection of Python applications built for practice. Each application provides hands-on experience with Python concepts, problem solving, and writing runnable programs.

This repository grows as new applications are added and existing ones are improved while learning.

## Applications

| Application | Description | Concepts demonstrated |
| --- | --- | --- |
| [Chinese Zodiac GUI](chinese_zodiac_gui_frames.py) | Calculates a zodiac animal and optionally emails the result. | Tkinter widgets, frames, pack/grid layouts, fonts, and colors. |
| [Course List](course_list_2d.py) | A Python course-list example. | Two-dimensional lists. |
| [Grade Calculator](grade_calculator_python.py) | Converts a numeric percentage into a letter grade using the program's custom grading scale. | Variables, strings, f-strings, input/output, float conversion, rounding, comparisons, and if/elif conditionals. |

## Run an application

Install Python 3, then run this command from the repository root:

```bash
python grade_calculator_python.py
```

Use `python3` if that is your Python command. The grade calculator and course list require no third-party packages.

Enter a percentage such as `96.25` (meaning 96.25%, rather than 0.9625).

## Chinese Zodiac GUI

Run the application with:

```bash
python -m pip install -r requirements.txt
python chinese_zodiac_gui_frames.py
```

Requires Tkinter and a graphical desktop. On Debian/Ubuntu, install `python3-tk` if Tkinter is missing. The interface uses three frames (title, input, and button) and adapts the Week 6 tutorial layout with a forest palette and evergreen silhouettes. The button calculates the zodiac animal and emails it if an email address is entered. Leave the email field blank to calculate only. Enter your full Gregorian birth date as `YYYY-MM-DD`. The `lunardate` library converts it to the Chinese lunar calendar so the animal changes on Chinese New Year. Supported birth dates start at 1900-01-31 and end at today (or 2099-12-31, whichever is earlier).

### Email setup

The program uses Python's built-in `smtplib`, `ssl`, and `email.message` modules. Set these environment variables privately before launching it:

- `SMTP_USERNAME`: your sending account's email address.
- `SMTP_PASSWORD`: your sending account's app-specific password, when required by your provider.
- `SMTP_HOST`: defaults to `smtp.gmail.com`; change it for another provider.
- `SMTP_PORT`: defaults to `587` and uses STARTTLS.

The password is read by `password = os.getenv("SMTP_PASSWORD", "")` in `send_zodiac_email`. Do not paste it into the source code or commit it to GitHub. Set variables through your IDE's private run configuration or your operating system's environment settings, then restart the application. Recipients do not need the sender's password. Sending runs in the background to keep the window responsive.

![Running Chinese Zodiac Calculator GUI](screenshots/Screenshot 2026-10-18 160403.png)

## Add more applications

1. Add a new `.py` file to this folder using a descriptive filename such as `loops_example.py`.
2. Add a row to the table above describing its purpose and the concepts it demonstrates.
3. Run the application and commit the file and README update.

Future applications could explore loops, functions, lists, dictionaries, file handling, and exceptions.

## Grade calculator development notes

The calculator is preserved as originally uploaded. Its current conditional chain does not assign a grade when the rounded input is from 68 through 72.99, causing a `NameError`. The intended grade for that interval needs to be defined in a future revision. Non-numeric input also raises an error, and percentages outside 0–100 are not rejected.
