import tkinter as tk

def update_hobbies():
    selected = []
    if var_read.get() == 1:
        selected.append("Leer")
    if var_sport.get() == 1:
        selected.append("Deporte")
    if var_music.get() == 1:
        selected.append("Música")

    if not selected:
        label_result.config(text="No hay aficiones seleccionados")
    else:
        label_result.config(text="Aficiones seleccionados: " + ", ".join(selected))


window = tk.Tk()
window.title("Ejercicio 4 - Checkbutton")
window.geometry("300x250")

var_read = tk.IntVar()
var_sport = tk.IntVar()
var_music = tk.IntVar()

check_read = tk.Checkbutton(window, text="Leer", variable=var_read, command=update_hobbies)
check_sport = tk.Checkbutton(window, text="Deporte", variable=var_sport, command=update_hobbies)
check_music = tk.Checkbutton(window, text="Música", variable=var_music, command=update_hobbies)

check_read.pack(pady=5)
check_sport.pack(pady=5)
check_music.pack(pady=5)

label_result = tk.Label(window, text="No hay aficiones seleccionados")
label_result.pack(pady=20)

window.mainloop()
