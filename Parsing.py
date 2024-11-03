import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def parse_social_media(login, social_media_url):
    url = social_media_url.format(login)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if 'telegram.org' in social_media_url:
            result_label.config(text=f"Found on Telegram: {login}")
        
        elif 'vk.com' in social_media_url:
            result_label.config(text=f"Found on VK: {login}")
        
        elif 'youtube.com' in social_media_url:
            result_label.config(text=f"Found on YouTube: {login}")
        
        elif 'rutube.ru' in social_media_url:
            result_label.config(text=f"Found on RuTube: {login}")
        
        elif 'ok.ru' in social_media_url:
            result_label.config(text=f"Found on Odnoklassniki: {login}")
        
        elif 'tiktok.com' in social_media_url:
            result_label.config(text=f"Found on TikTok: {login}")
        
        elif 'likee.video' in social_media_url:
            result_label.config(text=f"Found on Likee: {login}")
        
        elif 'discord.com' in social_media_url:
            result_label.config(text=f"Found on Discord: {login}")
        
        elif 'skype.com' in social_media_url:
            result_label.config(text=f"Found on Skype: {login}")
        
        elif 'steampowered.com' in social_media_url:
            result_label.config(text=f"Found on Steam: {login}")
        
        elif 'instagram.com' in social_media_url:
            result_label.config(text=f"Found on Instagram: {login}")
        
        elif 'facebook.com' in social_media_url:
            result_label.config(text=f"Found on Facebook: {login}")
        
        elif 'twitter.com' in social_media_url:
            result_label.config(text=f"Found on Twitter: {login}")
        
        elif 'snapchat.com' in social_media_url:
            result_label.config(text=f"Found on Snapchat: {login}")
        
        elif 'linkedin.com' in social_media_url:
            result_label.config(text=f"Found on LinkedIn: {login}")
    
    else:
        result_label.config(text='Failed to fetch data')

def search_user():
    login = login_entry.get()

    social_media_urls = {
        'Telegram': 'https://telegram.org/{}',
        'VK': 'https://vk.com/{}',
        'YouTube': 'https://www.youtube.com/user/{}',
        'RuTube': 'https://rutube.ru/video/person/{}',
        'Odnoklassniki': 'https://ok.ru/profile/{}',
        'TikTok': 'https://www.tiktok.com/@{}',
        'Likee': 'https://likee.video/u/{}',
        'Discord': 'https://discord.com/users/{}',
        'Skype': 'https://www.skype.com/en/{}',
        'Steam': 'https://store.steampowered.com/user/{}',
        'Instagram': 'https://www.instagram.com/{}',
        'Facebook': 'https://www.facebook.com/{}',
        'Twitter': 'https://twitter.com/{}',
        'Snapchat': 'https://www.snapchat.com/add/{}',
        'LinkedIn': 'https://www.linkedin.com/in/{}'
    }

    for social_media, url in social_media_urls.items():
        parse_social_media(login, url)

# GUI
root = tk.Tk()
root.title('Social Media Parser')
root.geometry('400x300')
root.configure(bg='black')

banner_label = ttk.Label(root, text="█▀█ ▄▀█ █▀█ █▀ █ █▄░█ █▀▀\n█▀▀ █▀█ █▀▄ ▄█ █ █░▀█ █▄█", foreground='cyan', background='black')
banner_label.pack(pady=10)

login_label = ttk.Label(root, text='Enter Login:', foreground='red', background='black')
login_label.pack(pady=10)

login_entry = ttk.Entry(root, width=30)
login_entry.pack(pady=5)

search_button = ttk.Button(root, text='Search User', command=search_user)
search_button.pack(pady=10)

result_label = ttk.Label(root, text='', foreground='blue', background='black')
result_label.pack(pady=20)

root.mainloop()