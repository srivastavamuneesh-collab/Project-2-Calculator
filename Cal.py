import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        
        # Display screen
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")
        
        # Define buttons (Scientific + Standard)
        buttons = [
            'C', '√', '/', 'ln',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            'sin', '0', '.', '=',
            'cos', 'tan', 'log', '^'
        ]
        
        # Create and place buttons in a grid
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_click(x)
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
                      command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_click(self, char):
        current_text = self.display.get()
        
        if char == '=':
            try:
                # Replace visual symbols with Python-compatible operators
                expr = current_text.replace('^', '**').replace('√', 'math.sqrt')
                # Use eval carefully or replace with a safer parser for production
                result = eval(expr, {"__builtins__": None}, {
                    "math": math, "sin": math.sin, "cos": math.cos, 
                    "tan": math.tan, "log": math.log10, "ln": math.log
                })
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char in ('sin', 'cos', 'tan', 'log', 'ln'):
            self.display.insert(tk.END, f"{char}(")
        elif char == '√':
            self.display.insert(tk.END, "√(")
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    obj = ScientificCalculator(root)
    root.mainloop()
