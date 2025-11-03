import tkinter as tk
from tkinter import messagebox
import random

class PiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra Papel Tijera")
        self.root.resizable(False, False)

        self.player_score = tk.IntVar(value=0)
        self.cpu_score = tk.IntVar(value=0)
        self.result_text = tk.StringVar(value="¡Haz tu elección!")

        self.images = {
            "piedra": "🪨",
            "papel": "📜",
            "tijera": "✂️"
        }

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Piedra Papel Tijera", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        score_frame = tk.Frame(self.root)
        score_frame.pack(pady=5)

        tk.Label(score_frame, text="Jugador:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
        tk.Label(score_frame, textvariable=self.player_score, font=("Arial", 12, "bold")).grid(row=0, column=1)
        tk.Label(score_frame, text="Máquina:", font=("Arial", 12)).grid(row=0, column=2, padx=10)
        tk.Label(score_frame, textvariable=self.cpu_score, font=("Arial", 12, "bold")).grid(row=0, column=3)

        player_frame = tk.LabelFrame(self.root, text="Tu jugada", font=("Arial", 12))
        player_frame.pack(pady=10)

        self.player_buttons = {}
        col = 0
        for name in ["piedra", "papel", "tijera"]:
            btn = tk.Button(
                player_frame,
                text=f"{self.images[name]} {name.capitalize()}",
                width=12,
                command=lambda n=name: self.play(n),
                font=("Arial", 11, "bold")
            )
            btn.grid(row=0, column=col, padx=5, pady=5)
            self.player_buttons[name] = btn
            col += 1

        image_frame = tk.Frame(self.root)
        image_frame.pack(pady=5)
        for name in ["piedra", "papel", "tijera"]:
            tk.Label(image_frame, text=self.images[name], font=("Arial", 20)).pack(side="left", expand=True, padx=35)

        cpu_frame = tk.LabelFrame(self.root, text="Elección de la máquina", font=("Arial", 12))
        cpu_frame.pack(pady=10)

        self.cpu_buttons = {}
        col = 0
        for name in ["piedra", "papel", "tijera"]:
            btn = tk.Button(
                cpu_frame,
                text=f"{self.images[name]} {name.capitalize()}",
                width=12,
                state="disabled",
                font=("Arial", 11, "bold")
            )
            btn.grid(row=0, column=col, padx=5, pady=5)
            self.cpu_buttons[name] = btn
            col += 1

        result_label = tk.Label(
            self.root,
            textvariable=self.result_text,
            font=("Arial", 13, "bold"),
            wraplength=300,
            justify="center"
        )
        result_label.pack(pady=10)

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Nuevo juego", command=self.new_game, width=12).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="Salir", command=self.root.quit, width=12).grid(row=0, column=1, padx=5)

    def play(self, player_choice):
        cpu_choice = random.choice(["piedra", "papel", "tijera"])
        result = self.determine_winner(player_choice, cpu_choice)

        self.result_text.set(result)

        # Highlight buttons based on result
        self.update_button_colors(player_choice, cpu_choice, result)

        # Check if someone reached 3 points
        if self.player_score.get() == 3 or self.cpu_score.get() == 3:
            self.end_game()

    def determine_winner(self, player, cpu):
        if player == cpu:
            return "¡Empate!"
        rules = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}
        if rules[player] == cpu:
            self.player_score.set(self.player_score.get() + 1)
            return "¡Ganaste!"
        else:
            self.cpu_score.set(self.cpu_score.get() + 1)
            return "Perdiste..."

    # --- Update button colors to show round result ---
    def update_button_colors(self, player_choice, cpu_choice, result):
        # Reset all buttons
        for btn in self.player_buttons.values():
            btn.config(bg="SystemButtonFace", fg="black")
        for btn in self.cpu_buttons.values():
            btn.config(bg="SystemButtonFace", fg="black")

        # Define color scheme
        if "Empate" in result:
            color_player = color_cpu = "#FFD700"  # yellow
            text_color = "black"
        elif "Ganaste" in result:
            color_player, color_cpu = "#32CD32", "#DC143C"  # green/red
            text_color = "white"
        else:
            color_player, color_cpu = "#DC143C", "#32CD32"  # red/green
            text_color = "white"

        # Apply colors
        self.player_buttons[player_choice].config(bg=color_player, fg=text_color)
        self.cpu_buttons[cpu_choice].config(bg=color_cpu, fg=text_color)

    def end_game(self):
        if self.player_score.get() == 3:
            messagebox.showinfo("Fin de la partida", "¡Felicidades! Ganaste la partida 🎉")
        else:
            messagebox.showinfo("Fin de la partida", "La máquina ganó 😢")

        for btn in self.player_buttons.values():
            btn.config(state="disabled")

    def new_game(self):
        self.player_score.set(0)
        self.cpu_score.set(0)
        self.result_text.set("¡Haz tu elección!")
        for btn in self.player_buttons.values():
            btn.config(state="normal", bg="SystemButtonFace", fg="black")
        for btn in self.cpu_buttons.values():
            btn.config(bg="SystemButtonFace", fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijera(root)
    root.mainloop()