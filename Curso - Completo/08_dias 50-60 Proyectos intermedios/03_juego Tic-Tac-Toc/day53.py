import tkinter as tk
from tkinter import font as tkfont

# ── Paleta ──────────────────────────────────────────────────────────────────
BG        = "#0f0f1a"   # fondo oscuro casi negro
SURFACE   = "#1a1a2e"   # superficie de las celdas
BORDER    = "#2a2a4a"   # borde de las celdas
X_COLOR   = "#e94560"   # rojo-rosa para X
O_COLOR   = "#0f9b8e"   # verde-teal para O
TEXT_MAIN = "#e0e0ff"   # texto principal
TEXT_DIM  = "#7070a0"   # texto secundario
ACCENT    = "#f5a623"   # acento naranja (hover / reset)
WIN_GLOW  = "#ffe066"   # destaque de victoria

# ── Estado del juego ────────────────────────────────────────────────────────
board          = [[""] * 3 for _ in range(3)]
current_player = "X"
buttons        = [[None] * 3 for _ in range(3)]
score          = {"X": 0, "O": 0, "Draw": 0}

# ── Ventana principal ────────────────────────────────────────────────────────
window = tk.Tk()
window.title("Tic · Tac · Toe")
window.geometry("480x800")
window.resizable(False, False)
window.configure(bg=BG)

# ── Fuentes ──────────────────────────────────────────────────────────────────
title_font   = tkfont.Font(family="Courier New", size=22, weight="bold")
symbol_font  = tkfont.Font(family="Courier New", size=36, weight="bold")
status_font  = tkfont.Font(family="Courier New", size=14)
score_font   = tkfont.Font(family="Courier New", size=11)
btn_font     = tkfont.Font(family="Courier New", size=13, weight="bold")

# ── Cabecera ─────────────────────────────────────────────────────────────────
header_frame = tk.Frame(window, bg=BG)
header_frame.pack(pady=(28, 6))

title_label = tk.Label(
    header_frame,
    text="TIC · TAC · TOE",
    font=title_font,
    fg=TEXT_MAIN,
    bg=BG,
)
title_label.pack()

underline = tk.Frame(header_frame, height=2, width=240, bg=X_COLOR)
underline.pack(pady=(4, 0))

# ── Marcador ─────────────────────────────────────────────────────────────────
score_frame = tk.Frame(window, bg=BG)
score_frame.pack(pady=6)

def make_score_box(parent, player, color):
    f = tk.Frame(parent, bg=SURFACE, bd=0, highlightthickness=1, highlightbackground=color)
    f.pack(side="left", padx=14, ipadx=14, ipady=6)
    tk.Label(f, text=player, font=score_font, fg=color, bg=SURFACE).pack()
    lbl = tk.Label(f, text="0", font=btn_font, fg=color, bg=SURFACE)
    lbl.pack()
    return lbl

score_x_lbl    = make_score_box(score_frame, "X", X_COLOR)
score_draw_lbl = make_score_box(score_frame, "·", TEXT_DIM)
score_o_lbl    = make_score_box(score_frame, "O", O_COLOR)

# ── Estado del turno ─────────────────────────────────────────────────────────
status_frame = tk.Frame(window, bg=BG)
status_frame.pack(pady=10)

status_label = tk.Label(
    status_frame,
    text="▶  Turno de X",
    font=status_font,
    fg=X_COLOR,
    bg=BG,
    width=22,
)
status_label.pack()

# ── Tablero ───────────────────────────────────────────────────────────────────
board_frame = tk.Frame(window, bg=BORDER, bd=0)
board_frame.pack(padx=40, pady=8)

def cell_color(player):
    return X_COLOR if player == "X" else O_COLOR

def on_enter(btn):
    if btn["text"] == "" and btn["state"] == "normal":
        btn.configure(bg="#252545")

def on_leave(btn):
    if btn["text"] == "":
        btn.configure(bg=SURFACE)

def on_click(row, col):
    global current_player
    btn = buttons[row][col]
    if btn["text"] != "" or btn["state"] == "disabled":
        return

    color = cell_color(current_player)
    btn.configure(text=current_player, fg=color, disabledforeground=color)
    board[row][col] = current_player

    winner, winning_cells = check_winner(board)
    if winner:
        score[winner] += 1
        update_score()
        highlight_winner(winning_cells, winner)
        status_label.config(
            text=f"🏆  ¡Gana {winner}!",
            fg=WIN_GLOW,
        )
        disable_buttons()
    elif is_draw(board):
        score["Draw"] += 1
        update_score()
        status_label.config(text="🤝  ¡Empate!", fg=TEXT_DIM)
    else:
        current_player = "O" if current_player == "X" else "X"
        c = cell_color(current_player)
        status_label.config(text=f"▶  Turno de {current_player}", fg=c)

def highlight_winner(cells, winner):
    color = cell_color(winner)
    for r, c in cells:
        buttons[r][c].configure(bg=color, fg=BG)

def disable_buttons():
    for row in buttons:
        for b in row:
            b.configure(state="disabled")

def update_score():
    score_x_lbl.config(text=str(score["X"]))
    score_o_lbl.config(text=str(score["O"]))
    score_draw_lbl.config(text=str(score["Draw"]))

for r in range(3):
    for c in range(3):
        btn = tk.Button(
            board_frame,
            text="",
            font=symbol_font,
            width=4, height=2,
            bg=SURFACE,
            fg=TEXT_MAIN,
            activebackground="#252545",
            activeforeground=TEXT_MAIN,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda row=r, col=c: on_click(row, col),
        )
        btn.grid(row=r, column=c, padx=3, pady=3)
        btn.bind("<Enter>", lambda e, b=btn: on_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: on_leave(b))
        buttons[r][c] = btn

# ── Lógica del juego ──────────────────────────────────────────────────────────
def check_winner(board):
    lines = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],  # filas
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],  # cols
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)],                        # diags
    ]
    for line in lines:
        vals = [board[r][c] for r, c in line]
        if vals[0] and vals[0] == vals[1] == vals[2]:
            return vals[0], line
    return None, []

def is_draw(board):
    return all(board[r][c] for r in range(3) for c in range(3))

def reset_game():
    global current_player, board
    current_player = "X"
    board = [[""] * 3 for _ in range(3)]
    status_label.config(text="▶  Turno de X", fg=X_COLOR)
    for row in buttons:
        for btn in row:
            btn.configure(text="", state="normal", bg=SURFACE, fg=TEXT_MAIN)

# ── Botón Reset ───────────────────────────────────────────────────────────────
reset_btn = tk.Button(
    window,
    text="↺  Nueva partida",
    font=btn_font,
    bg=SURFACE,
    fg=ACCENT,
    activebackground=ACCENT,
    activeforeground=BG,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=20, pady=10,
    command=reset_game,
)
reset_btn.pack(pady=18)
reset_btn.bind("<Enter>", lambda e: reset_btn.configure(bg=ACCENT, fg=BG))
reset_btn.bind("<Leave>", lambda e: reset_btn.configure(bg=SURFACE, fg=ACCENT))

# ── Footer ────────────────────────────────────────────────────────────────────
tk.Label(window, text="X vs O", font=score_font, fg=TEXT_DIM, bg=BG).pack(side="bottom", pady=10)

window.mainloop()