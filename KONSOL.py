import tkinter as tk
from tkinter import ttk
import os
import webbrowser
import random
import string
import subprocess
import platform
import psutil
import itertools

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def brute_force_password(target_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for length in range(1, 6):
        for attempt in itertools.product(characters, repeat=length):
            attempts += 1
            attempt_password = ''.join(attempt)
            if attempt_password == target_password:
                return attempt_password, attempts
    return None, attempts

def handle_command(event):
    command = command_entry.get()
    command_entry.delete(0, tk.END)

    if command == "!tg":
        url = "https://web.telegram.org/k/"
        webbrowser.open_new_tab(url)
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"Открытие ссылки: {url}\n")
        output_text.config(state=tk.DISABLED)
    elif command == "!wp":
        url = "https://web.whatsapp.com/"
        webbrowser.open_new_tab(url)
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"Открытие ссылки: {url}\n")
        output_text.config(state=tk.DISABLED)
    elif command == "!yt":
        url = "https://www.youtube.com/"
        webbrowser.open_new_tab(url)
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"Открытие ссылки: {url}\n")
        output_text.config(state=tk.DISABLED)
    elif command == "!what":
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, "ЭТО КОНСОЛЬ КОТОРАЯ ПОМОГАЕТ С РАБОТОЙ ПК, by D7head\n")
        output_text.config(state=tk.DISABLED)
    elif command.startswith("!create"):
        password = generate_password()
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"Сгенерированный пароль: {password}\n")
        output_text.config(state=tk.DISABLED)
    elif command == "!gg":
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, "Выключение компьютера через 5 секунд...\n")
        output_text.config(state=tk.DISABLED)
        subprocess.call(["shutdown", "/s", "/t", "5"])
    elif command == "!my_home":
        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"Информация о компьютере:\n")
        output_text.insert(tk.END, f"Операционная система: {platform.system()} {platform.release()}\n")
        output_text.insert(tk.END, f"Процессор: {platform.processor()}\n")
        output_text.insert(tk.END, f"Имя пользователя: {os.getlogin()}\n")
        output_text.insert(tk.END, f"Использование памяти: {psutil.virtual_memory().percent}%\n")
        output_text.insert(tk.END, f"Использование диска: {psutil.disk_usage('/').percent}%\n")
        output_text.config(state=tk.DISABLED)
    else: 
        output_text.config(state=tk.NORMAL) 
        output_text.insert(tk.END, "Пожалуйста, укажите верную команду\n") 
        output_text.config(state=tk.DISABLED)
    

root = tk.Tk()
root.title("Консоль")

command_entry = tk.Entry(root)
command_entry.pack(fill=tk.X, padx=5, pady=5)

send_button = ttk.Button(root, text="Отправить", command=lambda: handle_command(None))
send_button.pack(pady=5)

output_text = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

command_entry.bind("<Return>", handle_command)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def change_background_color():
    color = generate_random_color()
    root.configure(background=color)
    root.after(1000, change_background_color)


change_background_color()

root.mainloop()
