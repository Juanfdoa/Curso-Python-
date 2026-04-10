import tkinter as tk

# ── Paleta de colores ──────────────────────────────────────────────
BG        = "#1e1e2e"
FG        = "#cdd6f4"
WORK_COL  = "#a6e3a1"   # verde
BREAK_COL = "#fab387"   # naranja
LONG_COL  = "#89b4fa"   # azul
BTN_BG    = "#313244"
BTN_FG    = "#cdd6f4"
BTN_ACT   = "#45475a"

# ── Variables globales ─────────────────────────────────────────────
session_count = 0
timer_running = False
after_id      = None

# ── Lógica del temporizador ────────────────────────────────────────
def countdown(seconds):
    global timer_running, after_id
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        after_id = window.after(1000, countdown, seconds - 1)
    else:
        timer_running = False
        start_timer()

def start_timer():
    global session_count, timer_running
    if not timer_running:
        timer_running = True
        if session_count % 8 == 7:
            status_label.config(text="Descanso largo", fg=LONG_COL)
            countdown(15 * 60)
        elif session_count % 2 == 0:
            status_label.config(text="¡A trabajar!", fg=WORK_COL)
            countdown(25 * 60)
        else:
            status_label.config(text="Descanso corto", fg=BREAK_COL)
            countdown(5 * 60)
        session_count += 1
        sessions_label.config(text=f"Sesión {session_count}")

def reset_timer():
    global session_count, timer_running, after_id
    if after_id:
        window.after_cancel(after_id)
    session_count = 0
    timer_running = False
    timer_label.config(text="25:00")
    status_label.config(text="Listo", fg=FG)
    sessions_label.config(text="Sesión 0")

# ── Ventana principal ──────────────────────────────────────────────
window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("300x320")
window.resizable(False, False)
window.config(bg=BG)

# ── Widgets ────────────────────────────────────────────────────────
status_label = tk.Label(window, text="Listo", font=("Arial", 14), bg=BG, fg=FG)
status_label.pack(pady=(24, 0))

timer_label = tk.Label(window, text="25:00", font=("Arial", 52, "bold"), bg=BG, fg=FG)
timer_label.pack(pady=10)

sessions_label = tk.Label(window, text="Sesión 0", font=("Arial", 11), bg=BG, fg="#6c7086")
sessions_label.pack()

# Separador visual
sep = tk.Frame(window, height=1, bg="#45475a")
sep.pack(fill="x", padx=30, pady=16)

# Botones
btn_frame = tk.Frame(window, bg=BG)
btn_frame.pack()

btn_cfg = dict(font=("Arial", 13), bg=BTN_BG, fg=BTN_FG, activebackground=BTN_ACT, activeforeground=FG, relief="flat", bd=0, padx=18, pady=8, cursor="hand2")

start_button = tk.Button(btn_frame, text="▶  Iniciar", command=start_timer, **btn_cfg)
start_button.pack(side="left", padx=8)

reset_button = tk.Button(btn_frame, text="↺  Reiniciar",command=reset_timer, **btn_cfg)
reset_button.pack(side="left", padx=8)

window.mainloop()