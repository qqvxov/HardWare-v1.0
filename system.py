import platform
import tkinter as tk

system_info = platform.uname()

root = tk.Tk()
root.title("Информация о системе")

banner_text = "█▄█ █▀█ █░█ █▀█   █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█\n░█░ █▄█ █▄█ █▀▄   ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█"
banner_label = tk.Label(root, text=banner_text, fg="cyan", bg="black", font=("Courier", 12))
banner_label.pack(side="top", fill="x")

info_label = tk.Label(root, text=f"Система: {system_info.system}\nУзел сети: {system_info.node}\nВерсия: {system_info.version}\nМашина: {system_info.machine}\nПроцессор: {system_info.processor}", bg="black", fg="white")
info_label.pack()

root.configure(bg='black')
root.mainloop()