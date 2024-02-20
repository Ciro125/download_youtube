import os
import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def baixar_video():
    url = url_entry.get()
    if url:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        status_label.config(text="Vídeo baixado com sucesso!")
    else:
        status_label.config(text="Por favor, insira uma URL válida.")

# Criar janela
root = tk.Tk()
root.title("Baixar Vídeo do Yoshi")

# Criar e posicionar widgets
url_label = ttk.Label(root, text="URL do vídeo:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

url_entry = ttk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Definir texto padrão no url_entry
url_entry.insert(0, "https://www.youtube.com/watch?v=Dd8EtqVGFR0&ab_channel=ojujuba.")

baixar_button = ttk.Button(root, text="Baixar Vídeo", command=baixar_video)
baixar_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

status_label = ttk.Label(root, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Iniciar loop de execução
root.mainloop()
