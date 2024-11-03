import tkinter as tk
from bs4 import BeautifulSoup as htmlparser
import requests

# Red banner
red_banner = """
█▀█ █░█ █▀█ █▄░█ █▀▀   █░░ █▀█ █▀█ █▄▀ █░█ █▀█
█▀▀ █▀█ █▄█ █░▀█ ██▄   █▄▄ █▄█ █▄█ █░█ █▄█ █▀▀
"""

def lookup(phone_number):
    http = requests.get(f"https://free-lookup.net/{phone_number}")
    html = htmlparser(http.text, "html.parser")
    infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")

    return {f"[R] {k.text.strip()}": infos[i+1].text.strip() if infos[i+1].text.strip() else "No information" for i, k in enumerate(infos) if not i % 2}

def main():
    def on_submit():
        phone_number = entry.get().strip().replace("-", "").replace(" ", "").replace("+", "")

        try:
            infos = lookup(phone_number)
            result_text.delete(1.0, tk.END)
            for info in infos:
                result_text.insert(tk.END, f"{info}: {infos[info]}\n")
        except AttributeError:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error: Invalid phone number\n")

    root = tk.Tk()
    root.title("Phone Number Lookup")
    root.configure(bg='black')  # Setting a black background
    
    banner_label = tk.Label(root, text=red_banner, bg='black', fg='red')
    banner_label.pack()

    label = tk.Label(root, text="Enter Phone Number:", bg='black', fg='white')
    label.pack()

    entry = tk.Entry(root, bg='black', fg='white')
    entry.pack()

    submit_button = tk.Button(root, text="Lookup", command=on_submit, bg='black', fg='white')
    submit_button.pack()

    result_text = tk.Text(root, height=10, width=50, bg='black', fg='white')
    result_text.pack()

    root.mainloop()

if __name__ == "__main__":
    main()