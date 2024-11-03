#код немного спиздил))) Но не все!

import requests
import sys
import os
import random
import tkinter as tk

def fetch_ip_information(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'}
    response = requests.get(url.strip(), headers=headers, timeout=5)
    return response

def start_logging():
    url = url_entry.get()
    response = fetch_ip_information(url)
    log_info_label.config(text="[+] IP logged successfully! You may now check the results on Grabify.\n\nURL: " + url)

def paste_from_clipboard(event):
    content = root.clipboard_get()
    url_entry.insert(tk.INSERT, content)

# Создание графического интерфейса
root = tk.Tk()
root.title("IPLOGGE")
root.configure(bg="black")

banner_label = tk.Label(root, text="█ █▀█   █░░ █▀█ █▀▀ █▀▀ █▀█\n█ █▀▀   █▄▄ █▄█ █▄█ ██▄ █▀▄", fg='red', bg='black', font='Helvetica 12 bold')
banner_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()
url_entry.bind("<Button-3>", paste_from_clipboard)  # Добавляем обработчик для вставки из буфера обмена

start_button = tk.Button(root, text="Start IP Logging", command=start_logging)
start_button.pack()

log_info_label = tk.Label(root, text="", bg="black", fg="white", font=("Helvetica", 12))
log_info_label.pack(expand=True, fill='both')

root.mainloop()