import tkinter as tk
import csv
import pandas as pd
import matplotlib.pyplot as plt
last_budget=0
def clmn():
    file=open("data.csv", mode="a", newline="")
    writer = csv.writer(file)    
    writer.writerow(["Date","Expense","Budget_left"])

def save_to_csv():
    global last_budget
    date = date_entry.get()
    expense = float(expense_entry.get())
    budget_entry_value=budget_entry.get()
    if not budget_entry_value:
       budget=last_budget
    elif budget_entry_value=="map":
        df=pd.read_csv('data.csv')
        plt.figure(figsize=(10, 6))
        plt.plot(df["Date"], df["Expense"], marker='o', linestyle='-')
        plt.xlabel("Date")
        plt.ylabel("Expense")
        plt.title("Expense vs. Date")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout() 
        plt.show()
    else:   
      budget= float(budget_entry.get())
    budget=budget-expense
    last_budget=budget
    file=open("data.csv", mode="a", newline="")
    writer = csv.writer(file)
    writer.writerow([date, expense, budget])
    
    date_entry.delete(0, "end")
    expense_entry.delete(0, "end")
    budget_entry.delete(0, "end")

app = tk.Tk()
app.title("Data Entry App")
clmn()

date_label = tk.Label(app, text="Date:")
date_label.grid(row=0, column=0)
date_entry = tk.Entry(app)
date_entry.grid(row=0, column=1)

expense_label = tk.Label(app, text="Expense:")
expense_label.grid(row=1, column=0)
expense_entry = tk.Entry(app)
expense_entry.grid(row=1, column=1)

budget_label = tk.Label(app, text="Budget:")
budget_label.grid(row=2, column=0)
budget_entry = tk.Entry(app)
budget_entry.grid(row=2, column=1)

save_button = tk.Button(app, text="Save to CSV", command=save_to_csv)
save_button.grid(row=3, column=0, columnspan=2)

app.mainloop()