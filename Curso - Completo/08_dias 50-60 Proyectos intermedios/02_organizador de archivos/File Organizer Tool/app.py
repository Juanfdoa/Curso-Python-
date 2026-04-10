import tkinter as tk
from tkinter import filedialog
from services import create_folder
from theme import *

root = tk.Tk()
root.title("File Organizer Tool")
root.geometry("480x280")
root.resizable(False, False)
root.configure(bg=BG_MAIN)

root.update_idletasks()
x = (root.winfo_screenwidth()  - 480) // 2
y = (root.winfo_screenheight() - 280) // 2
root.geometry(f"480x280+{x}+{y}")

#  CONTENEDOR 1 — Contenido (blanco)
content = tk.Frame(root, bg=BG_CONTENT)
content.place(x=0, y=0, width=480, height=220)

# Título azul
tk.Label(
    content,
    text="Select a Destination and Organize Files",
    font=("Segoe UI", 11,),
    bg=BG_CONTENT, fg=FG_TITLE, anchor="w"
).place(x=24, y=28)

# Etiqueta descripción
tk.Label(
    content,
    text="Files will be organized into this folder:",
    font=("Segoe UI", 9),
    bg=BG_CONTENT, fg=FG_LABEL, anchor="w"
).place(x=24, y=72)

# ── Entry + Browse ──
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)
        status_label.config(text="")

# Borde del campo
entry_border = tk.Frame(content, bg="#aaaaaa")
entry_border.place(x=24, y=95, width=330, height=28)

entry_inner = tk.Frame(entry_border, bg=BG_CONTENT)
entry_inner.place(x=1, y=1, width=328, height=26)

path_entry = tk.Entry(
    entry_inner,
    font=("Segoe UI", 9),
    relief="flat", bd=0,
    bg=BG_CONTENT, fg="#111",
    insertbackground="#333"
)
path_entry.place(x=4, y=3, width=320, height=20)

def _browse_hover(e, hover):
    browse_btn.config(bg="#d8d8d8" if hover else "#e8e8e8")

browse_btn = tk.Button(
    content,
    text="Browse…",
    command=browse_folder,
    font=("Segoe UI", 9),
    bg="#e8e8e8", fg="#111",
    relief="flat", bd=0,
    cursor="hand2",
    activebackground="#d0d0d0"
)
browse_btn.place(x=362, y=95, width=90, height=28)
browse_btn.bind("<Enter>", lambda e: _browse_hover(e, True))
browse_btn.bind("<Leave>", lambda e: _browse_hover(e, False))

# Status label
status_label = tk.Label(
    content, text="",
    font=("Segoe UI", 9),
    bg=BG_CONTENT, anchor="w"
)
status_label.place(x=24, y=140, width=430)

#  CONTENEDOR 2 — Footer gris (botones)
tk.Frame(root, bg=BORDER, height=1).place(x=0, y=220, width=480)

footer = tk.Frame(root, bg=BG_FOOTER)
footer.place(x=0, y=221, width=480, height=59)

def execute():
    path = path_entry.get().strip()
    if path:
        create_folder(path)
        root.after(1500, root.destroy)
        status_label.config(text="✔  Files organized successfully.", fg="#217346")
        path_entry.delete(0, tk.END)
    else:
        status_label.config(text="⚠  Please select a valid folder.", fg="#c42b1c")

def _ok_hover(e, hover):
    ok_btn.config(bg="#005fa3" if hover else "#0078d4")

def _cancel_hover(e, hover):
    cancel_btn.config(bg="#d8d8d8" if hover else "#e8e8e8")

ok_btn = tk.Button(
    footer,
    text="Organize",
    command=execute,
    font=("Segoe UI", 9, "bold"),
    bg="#0078d4", fg="white",
    relief="flat", bd=0,
    cursor="hand2",
    activebackground="#005fa3"
)
ok_btn.place(x=264, y=14, width=90, height=30)
ok_btn.bind("<Enter>", lambda e: _ok_hover(e, True))
ok_btn.bind("<Leave>", lambda e: _ok_hover(e, False))

cancel_btn = tk.Button(
    footer,
    text="Cancel",
    command=root.destroy,
    font=("Segoe UI", 9),
    bg="#e8e8e8", fg="#111",
    relief="flat", bd=0,
    cursor="hand2",
    activebackground="#d0d0d0"
)
cancel_btn.place(x=364, y=14, width=90, height=30)
cancel_btn.bind("<Enter>", lambda e: _cancel_hover(e, True))
cancel_btn.bind("<Leave>", lambda e: _cancel_hover(e, False))

root.mainloop()