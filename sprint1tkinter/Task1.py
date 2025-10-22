import tkinter as tk

def change_text():
    label3.config(text="nuevo texto")

window = tk.Tk()
window.title("Ejercicio 1 - Label")
window.geometry("300x200")

label1 = tk.Label(window, text="Holla mundo!")
label1.pack(pady=5)

label2 = tk.Label(window, text="Nikita Tkalich")
label2.pack(pady=5)

label3 = tk.Label(window, text="texto original")
label3.pack(pady=5)

button = tk.Button(window, text="Cambiar texto", command=change_text)
button.pack(pady=10)

window.mainloop()
