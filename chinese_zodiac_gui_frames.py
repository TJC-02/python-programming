"""A forest-themed zodiac calculator with optional SMTP email delivery."""

import os
import queue
import smtplib
import ssl
import threading
from datetime import date
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox


def zodiac_sign(year):
    """Return the traditional year-cycle animal (using the calendar year)."""
    animals = ("Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
               "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig")
    return animals[(year - 4) % 12]


def send_zodiac_email(recipient, year, sign):
    """Send via STARTTLS; keep account credentials outside the source code."""
    sender = os.getenv("SMTP_USERNAME", "").strip()
    password = os.getenv("SMTP_PASSWORD", "")  # Set your app password privately.
    host = os.getenv("SMTP_HOST", "smtp.gmail.com").strip()
    port = int(os.getenv("SMTP_PORT", "587"))
    if not sender or not password:
        raise ValueError("Set SMTP_USERNAME and SMTP_PASSWORD before sending email.")
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "Your Chinese Zodiac Sign"
    message.set_content(
        f"For birth year {year}, your Chinese zodiac animal is the {sign}.\n\n"
        "This educational calculator uses calendar years; birthdays before "
        "Chinese New Year may belong to the previous zodiac year."
    )
    with smtplib.SMTP(host, port, timeout=20) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(sender, password)
        if server.send_message(message):
            raise smtplib.SMTPException("Recipient refused")



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
    results = queue.Queue()

    def finish_delivery():
        try:
            error = results.get_nowait()
        except queue.Empty:
            window.after(100, finish_delivery)
            return
        calculate_button.configure(state="normal", text="Find My Zodiac")
        if error:
            messagebox.showerror("Email not sent", error, parent=window)
        else:
            messagebox.showinfo("Email sent", "Your zodiac result was sent.", parent=window)

    def calculate():
        try:
            year = int(year_entry.get().strip())
            if not 1 <= year <= date.today().year:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid year", "Enter a birth year from 1 through the current year.", parent=window)
            return
        recipient = email_entry.get().strip()
        if recipient and (recipient.count("@") != 1 or any(c.isspace() for c in recipient)
                          or not all(recipient.split("@"))):
            messagebox.showerror("Invalid email", "Enter a valid email address or leave it blank.", parent=window)
            return
        sign = zodiac_sign(year)
        messagebox.showinfo(
            "Your zodiac", f"{year}: {sign}\n\nUses calendar years; birthdays before Chinese New Year may differ.",
            parent=window,
        )
        if not recipient:
            return
        calculate_button.configure(state="disabled", text="Sending…")

        def deliver():
            try:
                send_zodiac_email(recipient, year, sign)
            except ValueError:
                results.put("Check SMTP_USERNAME, SMTP_PASSWORD, and SMTP_PORT in your environment settings.")
            except smtplib.SMTPAuthenticationError:
                results.put("Email login failed. Check your sender account and app password.")
            except (OSError, smtplib.SMTPException):
                results.put("Email delivery failed. Check your SMTP settings and network connection before retrying.")
            else:
                results.put(None)

        threading.Thread(target=deliver, daemon=True).start()
        window.after(100, finish_delivery)

    calculate_button.configure(command=calculate)
    tk.Label(
        button_frame, text="Developed for educational purposes",
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
