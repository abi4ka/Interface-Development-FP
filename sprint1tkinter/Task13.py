import random
import tkinter as tk


# --- Functions ---
def draw_circle(event):
    x, y = event.x, event.y
    r = 13
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "lime", "magenta"]
    color = random.choice(colors)
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")


def clear_canvas(event):
    if event.char == "c":
        canvas.delete("all")


# --- Main window ---
window = tk.Tk()
window.title("Ejercicio 13 - Eventos de teclado y ratón")
window.geometry("400x400")

# --- Canvas ---
canvas = tk.Canvas(window, bg="white")
canvas.pack(fill="both", expand=True)

# --- Event bindings ---
canvas.bind("<Button-1>", draw_circle)
window.bind("<Key>", clear_canvas)

# --- Run the application ---
window.mainloop()