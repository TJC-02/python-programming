"""Practice arranging a Tkinter GUI using title, input, and button frames.

This layout exercise does not calculate a zodiac sign or send email.
"""

import tkinter as tk


def create_window():
    """Build and return the Chinese Zodiac Calculator window."""
    window = tk.Tk()
    window.title("Chinese Zodiac Calculator")
    window.geometry("500x300")
    window.minsize(500, 300)
    window.configure(bg="lightblue")

    # Pack the three frames vertically in the main window.
    title_frame = tk.Frame(window, bg="lightblue")
    title_frame.pack(pady=20)
    title_label = tk.Label(
        title_frame,
        text="Chinese Zodiac Calculator",
        font=("Arial", 18, "bold"),
        fg="darkblue",
        bg="lightblue",
    )
    title_label.pack()

    # Grid aligns the labels and entries inside the input frame.
    input_frame = tk.Frame(window, bg="lightblue")
    input_frame.pack(pady=10)
    year_label = tk.Label(
        input_frame, text="Birth Year:", font=("Arial", 12), bg="lightblue"
    )
    year_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    year_entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
    year_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = tk.Label(
        input_frame, text="Email Address:", font=("Arial", 12), bg="lightblue"
    )
    email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    button_frame = tk.Frame(window, bg="lightblue")
    button_frame.pack(pady=20)
    calculate_button = tk.Button(
        button_frame,
        text="Find My Zodiac",
        font=("Arial", 12, "bold"),
        fg="white",
        bg="darkblue",
        width=18,
    )
    calculate_button.pack()
    year_entry.focus_set()
    return window


def main():
    """Start the GUI event loop."""
    window = create_window()
    window.mainloop()


if __name__ == "__main__":
    main()
