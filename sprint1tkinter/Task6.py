import tkinter as tk


def show_selected():
    selection = listbox.curselection()
    if selection:
        fruit = listbox.get(selection)
        label_result.config(text=f"Has seleccionado: {fruit}")
    else:
        label_result.config(text="No has seleccionado ninguna fruta.")


window = tk.Tk()
window.title("Ejercicio 6 - Listbox")
window.geometry("300x250")

label_title = tk.Label(window, text="Elige una fruta:")
label_title.pack(pady=10)

listbox = tk.Listbox(window, height=5)
fruits = ["Manzana", "Banana", "Naranja"]
for fruit in fruits:
    listbox.insert(tk.END, fruit)
listbox.pack(pady=5)

button = tk.Button(window, text="Mostrar selección", command=show_selected)
button.pack(pady=10)

label_result = tk.Label(window, text="")
label_result.pack(pady=10)

window.mainloop()
