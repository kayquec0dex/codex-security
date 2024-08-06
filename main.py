import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import json
import os
import requests

def API_VIRUSTOTAL():
    dir_now = os.path.dirname(__file__)
    arq_json = os.path.join(dir_now, 'config.json')
    with open(arq_json, 'r') as arq:
        data = json.load(arq)
    return data.get('API_KEY')

API_KEY = API_VIRUSTOTAL()
API_URL = 'https://www.virustotal.com/vtapi/v2/url/report'


def check_url():
    url = entry_url.get()
    if not API_KEY:
        messagebox.showerror("Erro", "Chave da API não encontrada.")
        return
        
    params = {'apikey': API_KEY, 'resource': url}
    response = requests.get(API_URL, params=params)
    response.raise_for_status() 
    result = response.json()
        
    if result.get('response_code') == 1:
        positives = result['positives']
        total = result['total']
        scan_date = result.get('scan_date', 'Desconhecida')
            
        if positives > 0:
            mensagem = (f"URL: {url}\n"
                        f"Status: Não segura\n"
                        f"Motivo: {positives} dos {total} motores de antivírus marcaram como suspeita\n"
                        f"Última verificação: {scan_date}")
        else:
            mensagem = (f"URL: {url}\n"
                        f"Status: Segura\n"
                        f"Nenhum motor de antivírus marcou a URL como suspeita\n"
                        f"Última verificação: {scan_date}")
    else:
        mensagem = "URL não encontrada no VirusTotal"
        
    messagebox.showinfo("Resultado da Verificação", mensagem)

root = tk.Tk()
root.title("KayqueC0dex")

icon = PhotoImage(file='./icon.png')
root.iconphoto(False, icon)

root.geometry("500x300")  
root.configure(bg='#f0f0f0') 

frame = tk.Frame(root, bg='#ffffff', bd=2, relief='solid', padx=20, pady=20)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Estilizar os widgets
title_label = tk.Label(frame, text="Digite a URL que você deseja verificar:", font=("Arial", 14, "bold"), bg='#ffffff')
title_label.pack(pady=10)

entry_url = tk.Entry(frame, width=50, font=("Arial", 12))
entry_url.pack(pady=10)

btn_verificar = tk.Button(frame, text="Verificar", command=check_url, font=("Arial", 12, "bold"), bg='#007bff', fg='#ffffff', relief='flat', padx=10, pady=5)
btn_verificar.pack(pady=10)

root.mainloop()
