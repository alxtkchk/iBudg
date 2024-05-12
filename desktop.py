import tkinter as tk
from tkinter import messagebox


class BudgetManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Budget Manager")
        self.geometry("600x400")

        self.init_ui()

    def init_ui(self):
        # Main frame
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Budget info label
        self.budget_label = tk.Label(main_frame, text="Budget: $1000")
        self.budget_label.pack()

        # Add expense button
        add_expense_button = tk.Button(main_frame, text="Add Expense", command=self.open_add_expense_window)
        add_expense_button.pack()

        # View statistics button
        view_statistics_button = tk.Button(main_frame, text="View Statistics", command=self.open_statistics_window)
        view_statistics_button.pack()

        # Settings button
        settings_button = tk.Button(main_frame, text="Settings", command=self.open_settings_window)
        settings_button.pack()

    def open_add_expense_window(self):
        add_expense_window = AddExpenseWindow(self)
        add_expense_window.grab_set()

    def open_statistics_window(self):
        statistics_window = StatisticsWindow(self)
        statistics_window.grab_set()

    def open_settings_window(self):
        settings_window = SettingsWindow(self)
        settings_window.grab_set()

class AddExpenseWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Add Expense")
        self.geometry("300x200")

        tk.Label(self, text="Enter expense details:").pack()

        # Entry fields
        tk.Label(self, text="Amount:").pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        tk.Label(self, text="Category:").pack()
        self.category_entry = tk.Entry(self)
        self.category_entry.pack()

        tk.Label(self, text="Date:").pack()
        self.date_entry = tk.Entry(self)
        self.date_entry.pack()

        # Buttons
        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(side=tk.LEFT)

        cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        cancel_button.pack(side=tk.LEFT)

class StatisticsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Statistics")
        self.geometry("300x200")

        tk.Label(self, text="Display statistics here...").pack()

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack()

class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Settings")
        self.geometry("300x200")

        tk.Label(self, text="Adjust settings here...").pack()

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack()

if __name__ == "__main__":
    app = BudgetManagerApp()
    app.mainloop()
