import tkinter as tk

def change_color():
    window.config(bg=color_var.get())

window = tk.Tk()
window.title("Ejercicio 5 - Radiobutton")
window.geometry("300x200")

label = tk.Label(window, text="Elige tu color favorito:")
label.pack(pady=10)

color_var = tk.StringVar(value="white")

radio_red = tk.Radiobutton(window, text="Rojo", variable=color_var, value="red", command=change_color)
radio_green = tk.Radiobutton(window, text="Verde", variable=color_var, value="green", command=change_color)
radio_blue = tk.Radiobutton(window, text="Azul", variable=color_var, value="blue", command=change_color)

radio_red.pack(pady=5)
radio_green.pack(pady=5)
radio_blue.pack(pady=5)

window.mainloop()
