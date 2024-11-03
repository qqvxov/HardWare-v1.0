import tkinter as tk
import requests
import tkinter.messagebox

def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

def show_ip_info():
    ip_address = entry.get()
    ip_info = get_ip_info(ip_address)
    info_text.delete(1.0, tk.END)
    for key, value in ip_info.items():
        info_text.insert(tk.END, f"[R] {key}: {value}\n")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(info_text.get(1.0, tk.END))
    root.update()

root = tk.Tk()
root.title("IP Info")
root.configure(bg='black')

# Banner
banner_text = "█ █▀█   █▀▀ █▀█ █░█ █▄░█ █▀▄ █▀▀ █▀█\n█ █▀▀   █▀░ █▄█ █▄█ █░▀█ █▄▀ ██▄ █▀▄"
banner = tk.Label(root, text=banner_text, bg='black', fg='cyan', font=("Courier", 12))
banner.pack(fill=tk.X)

label = tk.Label(root, text="Enter IP Address:", bg='black', fg='white')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Info", command=show_ip_info, bg='black', fg='white')
button.pack()

info_text = tk.Text(root, height=10, width=50, bg='black', fg='white')
info_text.pack()

copy_button = tk.Button(root, text="Copy Result", command=copy_to_clipboard, bg='black', fg='white')
copy_button.pack()

root.mainloop()