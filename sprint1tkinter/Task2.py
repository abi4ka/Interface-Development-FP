import tkinter as tk

def change_text():
    label.config(text="un mensaje")

def quit():
    window.quit()

window = tk.Tk()
window.title("Ejercicio 1 - Button")
window.geometry("300x200")

label = tk.Label(window, text="")
label.pack(pady=5)

button1 = tk.Button(window, text="Cambiar texto", command=change_text)
button1.pack(pady=10)

button2 = tk.Button(window, text="Salir", command=quit)
button2.pack(pady=10)

window.mainloop()
