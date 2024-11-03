import tkinter as tk

root = tk.Tk()
root.title("Text Display")
root.configure(bg='black')

banner = """
█▀▄ █▀▀ █░█ █▀▀ █░░ █▀█ █▀█ █▀▀ █▀█ █▀
█▄▀ ██▄ ▀▄▀ ██▄ █▄▄ █▄█ █▀▀ ██▄ █▀▄ ▄█
"""

banner_label = tk.Label(root, text=banner, bg='cyan', fg='white')
banner_label.pack()

text1 = tk.Label(root, text="[R] Разработчик: qqvx", bg='black', fg='white')
text1.pack()

text2 = tk.Label(root, text="[R] Youtube-канал: @qqvxov | Telegram-канал: @channel_qqvx \n blasthack: https://www.blast.hk/members/538818/", bg='black', fg='white')
text2.pack()

text3 = tk.Label(root, text="[R] Решение проблем с багами, фикс утановки компонентов: @userqqvx", bg='black', fg='white')
text3.pack()

root.mainloop()