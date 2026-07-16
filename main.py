import customtkinter as ctk
from tkinter import filedialog, messagebox
from tkinter import filedialog
from tkinter import filedialog
from organizer import organize_folder

# ---------------- Appearance ----------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# ---------------- Window ----------------
app = ctk.CTk()
app.title("Smart File Organizer")
app.geometry("700x500")
app.resizable(False, False)

# ---------------- Variable ----------------
folder_path = ctk.StringVar()
folder_path.set("No folder selected")

# ---------------- Functions ----------------
def browse_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_path.set(folder)

def organize():

    if folder_path.get() == "No folder selected":
        return

    result = organize_folder(folder_path.get())

    total = sum(result.values())

    text = f"""
Images      : {result['Images']}
Documents   : {result['Documents']}
Videos      : {result['Videos']}
Music       : {result['Music']}
Archives    : {result['Archives']}
Others      : {result['Others']}

Total Files : {total}
"""

    stats_label.configure(text=text)

    messagebox.showinfo(
        "Success",
        f"Successfully organized {total} files!"
    )

# ---------------- Widgets ----------------
title = ctk.CTkLabel(
    app,
    text="📂 Smart File Organizer",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

label = ctk.CTkLabel(
    app,
    textvariable=folder_path,
    wraplength=600
)
label.pack(pady=10)

browse_btn = ctk.CTkButton(
    app,
    text="Browse Folder",
    command=browse_folder
)
browse_btn.pack(pady=20)

organize_btn = ctk.CTkButton(
    app,
    text="Organize Files",
    command=organize
)

organize_btn.pack(pady=10)

stats_label = ctk.CTkLabel(
    app,
    text="No files organized yet.",
    justify="left",
    font=("Arial", 16)
)

stats_label.pack(pady=20)

# ---------------- Run ----------------
app.mainloop()