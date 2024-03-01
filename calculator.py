import tkinter as tk
def button_click(symbol):
    if symbol == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except ZeroDivisionError:
            display.delete(0, tk.END)
            display.insert(tk.END, "Math Error")
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif symbol == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)

def make_button(root, text, row, column, width=7, height=2, bg='gray', fg='white'):
    button = tk.Button(root, text=text, width=width, height=height, bg=bg, fg=fg, font=('Arial', 14), command=lambda: button_click(text), relief=tk.RAISED, borderwidth=2, padx=10, pady=10)
    button.grid(row=row, column=column, padx=5, pady=5)

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=20, font=('Arial', 14), bd=10, relief=tk.FLAT, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    if button == '=':
        make_button(root, button, row, col, 2)
    else:
        make_button(root, button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
