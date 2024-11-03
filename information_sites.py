import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk

def gather_info():
    url = url_entry.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    output_text.delete(1.0, tk.END)

    output_text.insert(tk.END, "[R] Статус код: " + str(response.status_code) + "\n")
    output_text.insert(tk.END, "[R] Заголовки: " + str(response.headers) + "\n")
    output_text.insert(tk.END, "[R] Текст: " + soup.get_text() + "\n")

    last_updated = soup.find('meta', attrs={'name': 'last-modified'})
    if last_updated:
        output_text.insert(tk.END, "[R] Дата последнего обновления: " + last_updated['content'] + "\n")
    else:
        output_text.insert(tk.END, "[R] Дата последнего обновления не найдена.\n")

    ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', response.text)
    output_text.insert(tk.END, "[R] Найденные IP-адреса на странице:\n")
    for ip in ip_addresses:
        output_text.insert(tk.END, ip + "\n")

    ports = re.findall(r'(?<=:)\d{1,5}', response.text)
    output_text.insert(tk.END, "[R] Найденные порты на странице:\n")
    for port in ports:
        output_text.insert(tk.END, port + "\n")

root = tk.Tk()
root.title("Сбор информации о сайте")
root.configure(bg='black')

banner = tk.Label(root, text="▒█░▒█ ▒█▀▀█ ▒█░░░ 　 ░█▀▀█ ▒█▄░▒█ ░█▀▀█ ▒█░░░ ▒█░▒█ ▒█▀▀▀█ ▀█▀ ▒█▀▀▀█\n▒█░▒█ ▒█▄▄▀ ▒█░░░ 　 ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ ▒█░░░ ▒█▄▄▄█ ░▀▀▀▄▄ ▒█░ ░▀▀▀▄▄\n░▀▄▄▀ ▒█░▒█ ▒█▄▄█ 　 ▒█░▒█ ▒█░░▀█ ▒█░▒█ ▒█▄▄█ ░░▒█░░ ▒█▄▄▄█ ▄█▄ ▒█▄▄▄█", bg='black', fg='cyan')
banner.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

fetch_button = tk.Button(root, text="Получить информацию", command=gather_info)
fetch_button.pack()

output_text = tk.Text(root, height=20, width=70, bg='black', fg='white')
output_text.pack()

root.mainloop()