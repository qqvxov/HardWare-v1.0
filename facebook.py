import csv
import tkinter as tk
import os
import codecs

def search_in_csv(search_query):
    results = []
    directory = "Data_bases"
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            try:
                with codecs.open(os.path.join(directory, file_name), 'r', encoding='utf-8-sig', errors='replace') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        if any(search_query.lower() in value.lower() for value in row.values()):
                            results.append(f"Match found in {file_name}: {', '.join(row.values())}")
            except Exception as e:
                results.append(f"Error reading {file_name}: {str(e)}")
    return results if results else ["No matching results found."]

def search_button_clicked():
    search_query = search_entry.get()
    search_results = search_in_csv(search_query)
    
    result_text.delete(1.0, tk.END)
    for result in search_results:
        result_text.insert(tk.END, result + "\n")

# Create the main application window
root = tk.Tk()
root.title("CSV Data Search")
root.geometry("400x300")
root.configure(bg='black')

banner_label = tk.Label(
    root,
    text="█▀▀ ▄▀█ █▀▀ █▀▀ █▄▄ █▀█ █▀█ █▄▀\n█▀░ █▀█ █▄▄ ██▄ █▄█ █▄█ █▄█ █░█",
    fg='cyan',
    bg='black'
)
banner_label.pack()

search_label = tk.Label(root, text="Enter search query:")
search_label.pack()

search_entry = tk.Entry(root, width=30)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_button_clicked)
search_button.pack()

result_text = tk.Text(root, height=10, width=50)
result_text.pack()

root.mainloop()