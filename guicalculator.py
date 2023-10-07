import tkinter as tk

def button_click(event):
    current = result_var.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif text == "C":
        result_var.set("")
    else:
        result_var.set(current + text)

root = tk.Tk()
root.title("Calculator")

result_var = tk.StringVar()
result_var.set("")

entry = tk.Entry(root, textvar=result_var, font="lucida 20 bold")
entry.pack(fill=tk.X, padx=10, pady=10, ipadx=8, ipady=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row, col = 0, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="lucida 15 bold", padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
