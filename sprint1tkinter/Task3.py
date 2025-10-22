import tkinter as tk

def show_greeting():
    name = entry.get()
    label_greeting.config(text=f"Holla, {name}!")

window = tk.Tk()
window.title("Ejercicio 3 - Entry")
window.geometry("300x200")

label_instruction = tk.Label(window, text="Escriba tu nombre:")
label_instruction.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

button = tk.Button(window, text="Holla", command=show_greeting)
button.pack(pady=10)

label_greeting = tk.Label(window, text="")
label_greeting.pack(pady=5)

window.mainloop()
