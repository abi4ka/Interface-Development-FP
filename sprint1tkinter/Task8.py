import tkinter as tk

def show_text():
    text = entry_text.get()
    label_result.config(text=f"Has escrito: {text}")

def clear_text():
    entry_text.delete(0, tk.END)
    label_result.config(text="Texto:")

window = tk.Tk()
window.title("Ejercicio 8 - Frame")
window.geometry("350x250")

frame_top = tk.Frame(window, pady=10)
frame_top.pack()

label_title = tk.Label(frame_top, text="Introduce un texto:")
label_title.grid(row=0, column=0, pady=5)

entry_text = tk.Entry(frame_top, width=20)
entry_text.grid(row=0, column=1, padx=5, pady=5)

label_result = tk.Label(frame_top, text="Texto:")
label_result.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

frame_bottom = tk.Frame(window, pady=10)
frame_bottom.pack()

button_show = tk.Button(frame_bottom, text="Mostrar", command=show_text)
button_show.grid(row=0, column=0, padx=10)

button_clear = tk.Button(frame_bottom, text="Borrar", command=clear_text)
button_clear.grid(row=0, column=1, padx=10)


window.mainloop()