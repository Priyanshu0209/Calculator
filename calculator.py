import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x400")
        self.root.config(bg="lightgray")

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Simple Calculator", font=("Helvetica", 24, "bold"), bg="lightgray")
        self.title_label.pack(pady=20)

        self.input_frame = tk.Frame(self.root, bg="lightgray")
        self.input_frame.pack(pady=10)

        self.num1_label = tk.Label(self.input_frame, text="Number 1:", font=("Helvetica", 14), bg="lightgray")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(self.input_frame, font=("Helvetica", 14))
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        self.num2_label = tk.Label(self.input_frame, text="Number 2:", font=("Helvetica", 14), bg="lightgray")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(self.input_frame, font=("Helvetica", 14))
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        self.operation_frame = tk.Frame(self.root, bg="lightgray")
        self.operation_frame.pack(pady=10)

        self.add_button = tk.Button(self.operation_frame, text="+", font=("Helvetica", 14), width=5, command=lambda: self.calculate('+'))
        self.add_button.grid(row=0, column=0, padx=10, pady=10)

        self.sub_button = tk.Button(self.operation_frame, text="-", font=("Helvetica", 14), width=5, command=lambda: self.calculate('-'))
        self.sub_button.grid(row=0, column=1, padx=10, pady=10)

        self.mul_button = tk.Button(self.operation_frame, text="*", font=("Helvetica", 14), width=5, command=lambda: self.calculate('*'))
        self.mul_button.grid(row=0, column=2, padx=10, pady=10)

        self.div_button = tk.Button(self.operation_frame, text="/", font=("Helvetica", 14), width=5, command=lambda: self.calculate('/'))
        self.div_button.grid(row=0, column=3, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18), bg="lightgray")
        self.result_label.pack(pady=20)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
