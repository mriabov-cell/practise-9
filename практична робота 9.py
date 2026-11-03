import math
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt


def calculate_and_plot():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        h = float(entry_h.get())

        if h <= 0:
            messagebox.showerror("Помилка", "Крок h повинен бути більше 0")
            return

        memo.delete("1.0", tk.END)


        memo.insert(tk.END, f"{'X':<10}\t{'Y':<10}\n")
        memo.insert(tk.END, "-" * 25 + "\n")

        x_values = []
        y_values = []


        x = a
        while x <= b + h / 2:
            y = math.sin(x) + 1

            x_values.append(x)
            y_values.append(y)


            if var_on_screen.get():
                memo.insert(tk.END, f"{x:<10.2f}\t{y:<10.2f}\n")

            x += h

        if var_plot.get():
            plt.figure(figsize=(6, 4))
            plt.plot(x_values, y_values, color="red", marker="o", linestyle="-")
            plt.title("Графік функції y = sin(x) + 1")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.grid(True)
            plt.show()

    except ValueError:
        messagebox.showerror(
            "Помилка", "Будь ласка, введіть коректні числові значення!"
        )


def clear_memo():
    """Аналог команди 'Очистити поле виведення'"""
    memo.delete("1.0", tk.END)



root = tk.Tk()
root.title("Табулювання функції")
root.geometry("450x550")


tk.Label(root, text="Ліва межа (a):").pack(anchor="w", padx=10, pady=2)
entry_a = tk.Entry(root)
entry_a.insert(0, "0.0")
entry_a.pack(fill="x", padx=10)


tk.Label(root, text="Права межа (b):").pack(anchor="w", padx=10, pady=2)
entry_b = tk.Entry(root)
entry_b.insert(0, "3.14")
entry_b.pack(fill="x", padx=10)


tk.Label(root, text="Крок (h):").pack(anchor="w", padx=10, pady=2)
entry_h = tk.Entry(root)
entry_h.insert(0, "0.2")
entry_h.pack(fill="x", padx=10)


frame_checks = tk.LabelFrame(root, text="Виведення та опції", padx=10, pady=5)
frame_checks.pack(fill="x", padx=10, pady=10)

var_on_screen = tk.BooleanVar(value=True)
chk_screen = tk.Checkbutton(
    frame_checks, text="На екран", variable=var_on_screen
)
chk_screen.pack(anchor="w")

var_plot = tk.BooleanVar(value=True)
chk_plot = tk.Checkbutton(
    frame_checks, text="Малювати графік", variable=var_plot
)
chk_plot.pack(anchor="w")


btn_frame = tk.Frame(root)
btn_frame.pack(fill="x", padx=10, pady=5)

btn_calc = tk.Button(
    btn_frame,
    text="Протабулювати",
    command=calculate_and_plot,
    bg="#4CAF50",
    fg="white",
)
btn_calc.pack(side="left", expand=True, fill="x", padx=2)

btn_clear = tk.Button(
    btn_frame, text="Очистити", command=clear_memo, bg="#f44336", fg="white"
)
btn_clear.pack(side="left", expand=True, fill="x", padx=2)


tk.Label(root, text="Результати (Memo):").pack(anchor="w", padx=10, pady=2)
memo = tk.Text(root, height=12)
memo.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()