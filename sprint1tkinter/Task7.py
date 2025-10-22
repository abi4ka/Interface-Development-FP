import tkinter as tk

def draw_shapes():
    try:
        rx1 = int(entry_rx1.get())
        ry1 = int(entry_ry1.get())
        rx2 = int(entry_rx2.get())
        ry2 = int(entry_ry2.get())

        cx1 = int(entry_cx1.get())
        cy1 = int(entry_cy1.get())
        cx2 = int(entry_cx2.get())
        cy2 = int(entry_cy2.get())

        canvas.delete("all")
        canvas.create_rectangle(rx1, ry1, rx2, ry2, fill="lightblue", outline="black")
        canvas.create_oval(cx1, cy1, cx2, cy2, fill="pink", outline="black")
    except ValueError:
        pass

window = tk.Tk()
window.title("Ejercicio 7 - Canvas Mejorado")
window.geometry("500x450")

frame_inputs = tk.Frame(window)
frame_inputs.pack(pady=10)

frame_rect = tk.LabelFrame(frame_inputs, text="Rectángulo", padx=10, pady=10)
frame_rect.grid(row=0, column=0, padx=10)

label_rx1 = tk.Label(frame_rect, text="x1:")
label_rx1.grid(row=0, column=0)
entry_rx1 = tk.Entry(frame_rect, width=5)
entry_rx1.grid(row=0, column=1)

label_ry1 = tk.Label(frame_rect, text="y1:")
label_ry1.grid(row=1, column=0)
entry_ry1 = tk.Entry(frame_rect, width=5)
entry_ry1.grid(row=1, column=1)

label_rx2 = tk.Label(frame_rect, text="x2:")
label_rx2.grid(row=2, column=0)
entry_rx2 = tk.Entry(frame_rect, width=5)
entry_rx2.grid(row=2, column=1)

label_ry2 = tk.Label(frame_rect, text="y2:")
label_ry2.grid(row=3, column=0)
entry_ry2 = tk.Entry(frame_rect, width=5)
entry_ry2.grid(row=3, column=1)

frame_circle = tk.LabelFrame(frame_inputs, text="Círculo", padx=10, pady=10)
frame_circle.grid(row=0, column=1, padx=10)

label_cx1 = tk.Label(frame_circle, text="x1:")
label_cx1.grid(row=0, column=0)
entry_cx1 = tk.Entry(frame_circle, width=5)
entry_cx1.grid(row=0, column=1)

label_cy1 = tk.Label(frame_circle, text="y1:")
label_cy1.grid(row=1, column=0)
entry_cy1 = tk.Entry(frame_circle, width=5)
entry_cy1.grid(row=1, column=1)

label_cx2 = tk.Label(frame_circle, text="x2:")
label_cx2.grid(row=2, column=0)
entry_cx2 = tk.Entry(frame_circle, width=5)
entry_cx2.grid(row=2, column=1)

label_cy2 = tk.Label(frame_circle, text="y2:")
label_cy2.grid(row=3, column=0)
entry_cy2 = tk.Entry(frame_circle, width=5)
entry_cy2.grid(row=3, column=1)

button_draw = tk.Button(window, text="Dibujar", command=draw_shapes)
button_draw.pack(pady=10)

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack(pady=10)

window.mainloop()
