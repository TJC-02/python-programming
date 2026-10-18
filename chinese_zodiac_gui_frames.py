"""Practice arranging a Tkinter GUI using title, input, and button frames.

This layout exercise does not calculate a zodiac sign or send email.
"""

import tkinter as tk


def create_window():
    """Build and return the Chinese Zodiac Calculator window."""
    window = tk.Tk()
    window.title("Chinese Zodiac Calculator")
    window.geometry("560x440")
    window.minsize(560, 440)
    window.configure(bg="#142e26")

    # Pack the three frames vertically in the main window.
    title_frame = tk.Frame(window, bg="#142e26")
    title_frame.pack(fill="x", pady=(0, 18))
    canopy = tk.Canvas(title_frame, height=90, bg="#142e26", highlightthickness=0)
    canopy.pack(fill="x")
    # Layered evergreen silhouettes form a quiet forest canopy.
    for x, height, color in [
        (20, 65, "#254b3b"), (85, 83, "#315943"),
        (150, 55, "#254b3b"), (415, 60, "#254b3b"),
        (480, 83, "#315943"), (545, 65, "#254b3b"),
    ]:
        canopy.create_line(x, 90, x, 90 - height, fill="#8f9c73", width=3)
        for level in range(3):
            top = 90 - height + level * height * 0.22
            half_width = 18 + level * 8
            canopy.create_polygon(
                x, top, x - half_width, top + height * 0.48,
                x + half_width, top + height * 0.48, fill=color, outline="",
            )
    canopy.create_text(
        280, 44, text="W O O D L A N D   /   Z O D I A C",
        fill="#b7c69b", font=("Arial", 10, "bold"),
    )
    title_label = tk.Label(
        title_frame,
        text="Chinese Zodiac Calculator",
        font=("Arial", 22, "bold"),
        fg="#e7dcbf",
        bg="#142e26",
    )
    title_label.pack(pady=(8, 6))
    tk.Label(
        title_frame, text="A little curiosity, rooted in nature.",
        font=("Arial", 11), fg="#b7c69b", bg="#142e26",
    ).pack()

    # Grid aligns the labels and entries inside the input frame.
    input_frame = tk.Frame(window, bg="#142e26")
    input_frame.pack(pady=8)
    year_label = tk.Label(
        input_frame, text="Birth Year:", font=("Arial", 11), fg="#e7dcbf", bg="#142e26"
    )
    year_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    year_entry = tk.Entry(input_frame, width=25, font=("Arial", 12),
        bg="#edf0df", fg="#203b2e", insertbackground="#203b2e",
        relief="flat", highlightthickness=2, highlightbackground="#526d4b",
        highlightcolor="#b7c69b", selectbackground="#526d4b",
        selectforeground="#ffffff")
    year_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = tk.Label(
        input_frame, text="Email Address:", font=("Arial", 11), fg="#e7dcbf", bg="#142e26"
    )
    email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(input_frame, width=25, font=("Arial", 12),
        bg="#edf0df", fg="#203b2e", insertbackground="#203b2e",
        relief="flat", highlightthickness=2, highlightbackground="#526d4b",
        highlightcolor="#b7c69b", selectbackground="#526d4b",
        selectforeground="#ffffff")
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    button_frame = tk.Frame(window, bg="#142e26")
    button_frame.pack(pady=(20, 0))
    calculate_button = tk.Button(
        button_frame,
        text="Find My Zodiac",
        font=("Arial", 12, "bold"),
        fg="#142e26",
        bg="#b7c69b",
        activebackground="#d1dcb8",
        activeforeground="#142e26",
        relief="flat",
        borderwidth=0,
        cursor="hand2",
        padx=20,
        pady=12,
        width=18,
    )
    calculate_button.pack()
    tk.Label(
        button_frame, text="G U I   L A Y O U T   P R A C T I C E",
        font=("Arial", 8), fg="#a9bc99", bg="#142e26",
    ).pack(pady=(16, 0))
    year_entry.focus_set()
    return window


def main():
    """Start the GUI event loop."""
    window = create_window()
    window.mainloop()


if __name__ == "__main__":
    main()
