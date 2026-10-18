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

from lunardate import LunarDate


def zodiac_sign(birth_date):
    """Return the animal for the Chinese lunar year containing birth_date."""
    if not date(1900, 1, 31) <= birth_date <= date(2099, 12, 31):
        raise ValueError("Supported birth dates are 1900-01-31 through 2099-12-31.")
    lunar_year = LunarDate.fromSolarDate(
        birth_date.year, birth_date.month, birth_date.day
    ).year
    animals = ("Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
               "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig")
    return animals[(lunar_year - 4) % 12]


def send_zodiac_email(recipient, birth_date, sign):
    """Send via STARTTLS; keep account credentials outside the source code."""
    sender = os.getenv("SMTP_USERNAME", "guywalkingupwalls@gmail.com").strip()
    password = os.getenv("SMTP_PASSWORD", "mfep vmbp qled difs")  # Set your app password privately.
    host = os.getenv("SMTP_HOST", "smtp.gmail.com").strip()
    port = int(os.getenv("SMTP_PORT", "587"))
    if not sender or not password:
        raise ValueError("Set SMTP_USERNAME and SMTP_PASSWORD before sending email.")
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "Your Chinese Zodiac Sign"
    message.set_content(
        f"For birth date {birth_date.isoformat()}, your Chinese zodiac animal "
        f"is the {sign}.\nCalculated using the Chinese lunar calendar."
    )
    with smtplib.SMTP(host, port, timeout=20) as server:
        server.starttls(context=ssl.create_default_context())
        server.login(sender, password)
        if server.send_message(message):
            raise smtplib.SMTPException("Recipient refused")



def create_window():
    """Build and return the Chinese Zodiac Calculator window."""
    window = tk.Tk()
    window.title("Chinese Zodiac Teller")
    window.geometry("560x460")
    window.minsize(560, 460)
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
        280, 44, text="W E L C O M E",
        fill="#b7c69b", font=("Arial", 10, "bold"),
    )
    title_label = tk.Label(
        title_frame,
        text="Chinese Zodiac Teller",
        font=("Arial", 22, "bold"),
        fg="#e7dcbf",
        bg="#142e26",
    )
    title_label.pack(pady=(8, 6))
    tk.Label(
        title_frame, text="CIST 3470 — Chenyen Xu",
        font=("Arial", 11), fg="#b7c69b", bg="#142e26",
    ).pack()

    # Grid aligns the labels and entries inside the input frame.
    input_frame = tk.Frame(window, bg="#142e26")
    input_frame.pack(pady=8)
    year_label = tk.Label(
        input_frame, text="Birth Date:", font=("Arial", 11), fg="#e7dcbf", bg="#142e26"
    )
    year_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    year_entry = tk.Entry(input_frame, width=25, font=("Arial", 12),
        bg="#edf0df", fg="#203b2e", insertbackground="#203b2e",
        relief="flat", highlightthickness=2, highlightbackground="#526d4b",
        highlightcolor="#b7c69b", selectbackground="#526d4b",
        selectforeground="#ffffff")
    year_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(
        input_frame, text="YYYY-MM-DD", font=("Arial", 9),
        fg="#b7c69b", bg="#142e26",
    ).grid(row=1, column=1, padx=10, sticky="w")

    email_label = tk.Label(
        input_frame, text="Email Address:", font=("Arial", 11), fg="#e7dcbf", bg="#142e26"
    )
    email_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
    email_entry = tk.Entry(input_frame, width=25, font=("Arial", 12),
        bg="#edf0df", fg="#203b2e", insertbackground="#203b2e",
        relief="flat", highlightthickness=2, highlightbackground="#526d4b",
        highlightcolor="#b7c69b", selectbackground="#526d4b",
        selectforeground="#ffffff")
    email_entry.grid(row=2, column=1, padx=10, pady=10)

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
            birth_date = date.fromisoformat(year_entry.get().strip())
            if birth_date > date.today():
                raise ValueError("Birth date cannot be in the future.")
            sign = zodiac_sign(birth_date)
        except ValueError:
            messagebox.showerror(
                "Invalid birth date",
                "Enter a valid birth date as YYYY-MM-DD, from 1900-01-31 "
                "through today (latest supported date: 2099-12-31).",
                parent=window,
            )
            return
        recipient = email_entry.get().strip()
        if recipient and (recipient.count("@") != 1 or any(c.isspace() for c in recipient)
                          or not all(recipient.split("@"))):
            messagebox.showerror("Invalid email", "Enter a valid email address or leave it blank.", parent=window)
            return
        messagebox.showinfo(
            "Your zodiac", f"{birth_date.isoformat()}: {sign}",
            parent=window,
        )
        if not recipient:
            return
        calculate_button.configure(state="disabled", text="Sending…")

        def deliver():
            try:
                send_zodiac_email(recipient, birth_date, sign)
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
