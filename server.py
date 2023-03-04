import json
import socket
import threading
from const import *

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.font as font
import os

#HOST = input("Host: ")
#PORT = int(input("Port: "))

# kill -9 $(lsof -t -i:210)

print("Vai rodar de novo")
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'O servidor está ativo no endereço {HOST}:{PORT}')

root = tk.Tk()
root.withdraw()

def get_usernames(jogador_logado_socket):
    return usernames[clients.index(jogador_logado_socket)]

def globalMessage(message):
    print("globalMessage: " + str(message))
    for client in clients:
        client.send(message)

def handleMessages(client):
    while True:
        try:
            mensagemRecebida = client.recv(2048).decode(DEFAULT_ENCODING)
            entrada = []
            for i in list(mensagemRecebida):
                entrada.append(i)
                if(i == '}'):
                    print("handleMessage: " + str("".join(entrada)))
                    jsonData = json.loads(str("".join(entrada)))
                    jsonData['name'] = usernames[clients.index(client)]
                    jsonData['index'] = clients.index(client)
                    resultMessage = json.dumps(jsonData)
                    globalMessage(f'{resultMessage}'.encode(DEFAULT_ENCODING))
                    entrada = []
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} saiu do chat...')
            usernames.remove(clientLeavedUsername)


def conexao(text_area):
    text_area.insert(tk.INSERT, "Servidor conectado!\n")
    while True:
        try:
            # Aceitando a conexao
            client, address = server.accept()

            # Adicionando a conexao a uma lista
            print(f"Nova conexao no endereco: {str(address)}")
            clients.append(client)
            response = '{"event":"getUser", "index": "'+str(clients.index(client))+'"}'
            client.send(response.encode(DEFAULT_ENCODING))
            username = client.recv(2048).decode(DEFAULT_ENCODING)
            usernames.append(username)

            # Printa no terminal e no servidor
            text_area.insert(tk.INSERT, f'{username} acaba de entrar no chat!\n'.encode(DEFAULT_ENCODING))
            #globalMessage(f'{"event":"CHAT, "message": {username} acaba de entrar no chat!}\n'.encode(DEFAULT_ENCODING))

            user_thread = threading.Thread(target=handleMessages,args=(client,))
            user_thread.start()
        except:
            pass


def janela_servidor():
    newWindow = Toplevel(root)
    newWindow.title("Socket: Servidor")
    newWindow.geometry("476x220")

    newWindow.protocol("WM_DELETE_WINDOW", janela_aviso)

    text_area = ScrolledText(newWindow, wrap=WORD, fg='blue', width=42, height=7, font=("Callibri", 9))
    text_area.place(x=120, y=79)
    text_area.focus()

    conexao(text_area)

def janela_aviso():
    newWindow = Toplevel(root)
    newWindow.title("Servidor: Aviso!")
    newWindow.geometry("360x205")

    sim_button = Button(newWindow, text='SIM', width=12, command=lambda:action_sim(newWindow))
    sim_button.place(x=124, y=154)

    nao_button = Button(newWindow, text='NÃO', width=12, command=lambda:action_nao(newWindow))
    nao_button.place(x=240, y=154)

def action_sim(Toplevel):
    Toplevel.destroy()
    Toplevel.quit()
    root.destroy()

def action_nao(Toplevel):
    Toplevel.destroy()

if __name__ == "__main__":
    threading.Thread(target=janela_servidor).start() # Mostrar janela do servidor
    root.mainloop()