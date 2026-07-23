import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import os


# =========================
# App Configuration
# =========================

APP_NAME = "Persian Radio Manager"
VERSION = "v0.1.0"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================
# Button Functions
# =========================

def install_radio():
    messagebox.showinfo(
        "Install",
        "Radio Pack installation module will be added soon."
    )


def check_update():
    messagebox.showinfo(
        "Update",
        "Checking latest version..."
    )


def backup_radio():
    messagebox.showinfo(
        "Backup",
        "Backup system will be added soon."
    )


def restore_radio():
    messagebox.showinfo(
        "Restore",
        "Restore system will be added soon."
    )


def open_game_folder():
    path = os.path.expanduser(
        "~/Documents/Euro Truck Simulator 2"
    )

    if os.path.exists(path):
        os.startfile(path)
    else:
        messagebox.showwarning(
            "Not Found",
            "Euro Truck Simulator 2 folder not found."
        )


def open_github():
    import webbrowser
    webbrowser.open(
        "https://github.com/yoosefzeynali-ship-it/Persian-Radio-Pack"
    )


# =========================
# Main Window
# =========================

app = ctk.CTk()

app.title(APP_NAME)

app.geometry("520x600")

app.resizable(False, False)


# =========================
# Header
# =========================

title = ctk.CTkLabel(
    app,
    text="🎙 Persian Radio Manager",
    font=("Arial", 24, "bold")
)

title.pack(pady=25)


version = ctk.CTkLabel(
    app,
    text=f"Version {VERSION}",
    font=("Arial", 14)
)

version.pack()


# =========================
# Status Box
# =========================

status_frame = ctk.CTkFrame(app)

status_frame.pack(
    pady=25,
    padx=40,
    fill="x"
)


status = ctk.CTkLabel(
    status_frame,
    text=
    """
📻 Persian Radio Pack

Latest Version: v1.0.0

Installed:
Checking...

ETS2:
Unknown

ATS:
Unknown
""",
    font=("Arial",14),
    justify="left"
)

status.pack(
    padx=20,
    pady=20
)


# =========================
# Buttons
# =========================

buttons = [

    ("Install Radio Pack", install_radio),

    ("Check for Update", check_update),

    ("Backup", backup_radio),

    ("Restore", restore_radio),

    ("Open ETS2 Folder", open_game_folder),

    ("GitHub", open_github)

]


for text, command in buttons:

    btn = ctk.CTkButton(
        app,
        text=text,
        width=280,
        height=40,
        command=command
    )

    btn.pack(
        pady=7
    )


# =========================
# Footer
# =========================

footer = ctk.CTkLabel(
    app,
    text="Created by @yoosef110",
    font=("Arial",12)
)

footer.pack(
    pady=25
)


# =========================
# Run
# =========================

app.mainloop()
