#Нахуй ты сюда залез? Лучше заходи в тгк: https://t.me/RigolDox

import tkinter as tk
from tkinter import ttk
import pandas as pd
import subprocess
import os
import csv

def search_in_databases():
    databases = ['card1', 'card2', 'card3']
    criteria = ['Name', 'Phone']

    current_directory = os.path.dirname(os.path.abspath(__file__))

    for db_name in databases:
        result_text.insert(tk.END, f"Searching in database: {db_name}\n")
        database_path = os.path.join(current_directory, 'Data_bases', f'{db_name}.csv')

        if os.path.exists(database_path):
            try:
                with open(database_path, 'r', encoding='cp1251') as file:
                    try:
                        csvreader = csv.reader(file)
                        header = next(csvreader)  

                        for criterion in criteria:
                            search_query = entry.get()
                            found_records = []

                            for row in csvreader:
                                if len(row) == len(header):  
                                    if criterion in header:
                                        criterion_index = header.index(criterion)
                                        if row[criterion_index] == search_query:
                                            found_records.append(row)
                            if found_records:
                                result_text.insert(tk.END, f"Found in {db_name}:\n")
                                for record in found_records:
                                    result_text.insert(tk.END, f"{record}\n")
                            else:
                                result_text.insert(tk.END, f"No matching records found in {db_name} for {criterion} {search_query}\n")
                    except pd.errors.ParserError as e:
                        result_text.insert(tk.END, f"Error reading database {db_name}: {str(e)}\n")
            except FileNotFoundError:
                result_text.insert(tk.END, f"Database {db_name} not found\n")

def copy_result():
    result = result_text.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()

def run_secondary_code():
    subprocess.Popen(["python", "bank_search.py"])

root = tk.Tk()
root.title("Your Title Here")
root.configure(bg='black')

banner_label = tk.Label(root, text="█▀▀ ▄▀█ █▀█ █▀▄   █▀ █▀▀ ▄▀█ █▀█ █▀▀ █░█\n█▄▄ █▀█ █▀▄ █▄▀   ▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█", fg='cyan', bg='black', font='Helvetica 12 bold')
banner_label.pack()

label = ttk.Label(root, text="Введите номер телефона или Имя:", foreground="red", background="black")
label.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=10)

search_button = ttk.Button(root, text='Поиск', command=search_in_databases)
search_button.pack(pady=10)

copy_button = ttk.Button(root, text='Копировать результат', command=copy_result)
copy_button.pack(pady=10)



result_text = tk.Text(root, height=20, width=50, bg='black', fg='blue')
result_text.pack(pady=10)

root.mainloop()