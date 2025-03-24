import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.calculation = ""
        
        self.text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
        self.text_result.grid(columnspan=5)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
            ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
            ('7', 4, 1), ('8', 4, 2), ('9', 4, 3),
            ('0', 5, 2), ('+', 2, 4), ('-', 3, 4),
            ('*', 4, 4), ('/', 5, 4), ('(', 5, 1),
            (')', 5, 3), ('C', 6, 1, 2), ('=', 6, 3, 2)
        ]
        
        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1
            
            if text in {'C', '='}:
                command = self.clear_field if text == 'C' else self.evaluate_calculation
                self.create_button(text, row, col, command, colspan)
            else:
                self.create_button(text, row, col, lambda x=text: self.add_to_calculation(x))

    def create_button(self, text, row, col, command, colspan=1):
        btn = tk.Button(root, text=text, command=command, width=5, font=("Arial", 14))
        btn.grid(row=row, column=col, columnspan=colspan)

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.update_display()

    def evaluate_calculation(self):
        try:
            self.calculation = str(eval(self.calculation))
            self.update_display()
        except Exception:
            self.clear_field()
            self.text_result.insert(1.0, "error")

    def clear_field(self):
        self.calculation = ""
        self.update_display()

    def update_display(self):
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x275")
    calculator = Calculator(root)
    root.mainloop()