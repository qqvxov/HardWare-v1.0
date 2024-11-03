import requests
import tkinter as tk

def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    if response.status_code == 200:
        bot_data = response.json()
        bot_id = bot_data['result']['id']
        bot_username = bot_data['result']['username']
        bot_name = bot_data['result']['first_name']
        bot_info = bot_data['result'].get('description', 'No information available about the bot')
        return bot_id, bot_username, bot_name, bot_info
    else:
        return None

def get_info_from_token():
    token = entry.get()
    bot_id, bot_username, bot_name, bot_info = get_bot_info(token)
    if bot_id:
        result_text.set(f"Bot ID: {bot_id}\nBot Username: @{bot_username}\nBot Name: {bot_name}\nBot Info: {bot_info}")
    else:
        result_text.set("Failed to retrieve bot information. Please check the token.")


root = tk.Tk()
root.title("Getting information about a Telegram bot")
root.configure(bg='black')

banner_label = tk.Label(root, text="█▄▄ █▀█ ▀█▀ █▀   █▀█ █▀ █ █▄░█ ▀█▀\n█▄█ █▄█ ░█░ ▄█   █▄█ ▄█ █ █░▀█ ░█░", fg="cyan", bg="black")
banner_label.pack()

label = tk.Label(root, text="Enter the Telegram bot token:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button_get_info = tk.Button(root, text="Get Info", command=get_info_from_token)
button_get_info.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

root.mainloop()