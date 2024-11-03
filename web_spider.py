import requests
from bs4 import BeautifulSoup
import tkinter as tk

def web_crawler(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [f"[R] {link.get('href')}" for link in soup.find_all('a')]
    return links

def crawl_and_display():
    url = url_entry.get()
    links = web_crawler(url)
    for link in links:
        result_text.insert(tk.END, link + '\n')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_text.get("1.0", tk.END))

root = tk.Tk()
root.title("Web Spider")
root.geometry("700x400")
root.configure(bg='black')

banner = tk.Label(root, text="▒█░░▒█ ▒█▀▀▀ ▒█▀▀█ 　 ▒█▀▀▀█ ▒█▀▀█ ▀█▀ ▒█▀▀▄ ▒█▀▀▀ ▒█▀▀█ \n▒█▒█▒█ ▒█▀▀▀ ▒█▀▀▄ 　 ░▀▀▀▄▄ ▒█▄▄█ ▒█░ ▒█░▒█ ▒█▀▀▀ ▒█▄▄▀ \n▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ 　 ▒█▄▄▄█ ▒█░░░ ▄█▄ ▒█▄▄▀ ▒█▄▄▄ ▒█░▒█", bg='black', fg='cyan')
banner.pack()

url_label = tk.Label(root, text="Введите URL:", bg='black', fg='white')
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

crawl_button = tk.Button(root, text="Начать краулинг", command=crawl_and_display, bg='black', fg='white')
crawl_button.pack()

result_text = tk.Text(root, height=15, width=80)
result_text.pack()

copy_button = tk.Button(root, text="Копировать результат", command=copy_to_clipboard, bg='black', fg='white')
copy_button.pack()

root.mainloop()