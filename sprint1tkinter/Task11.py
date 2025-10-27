import tkinter as tk

def update_label(value):
    label_value.config(text=f"Valor seleccionado: {value}")

window = tk.Tk()
window.title("Ejercicio 11 - Scale")
window.geometry("300x200")

label_title = tk.Label(window, text="Selecciona un número:")
label_title.pack(pady=10)

scale = tk.Scale(window, from_=0, to=100, orient="horizontal", command=update_label)
scale.pack(pady=10)

label_value = tk.Label(window, text="Valor seleccionado: 0")
label_value.pack(pady=10)

window.mainloop()
