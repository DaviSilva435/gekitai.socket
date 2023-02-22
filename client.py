import socket
import threading

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
import tkinter as tk

"""
Cria objeto "Tkinter"/"Tk"
"""
root = tk.Tk()
root.withdraw()

#ServerIP = input("Server IP: ")
#PORT = int(input("Port: "))

ServerIP = '127.0.0.1'
PORT = 210

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text_area_chat = ScrolledText()
username = ''


def conexao_cliente():
    newWindow = Toplevel(root)
    newWindow.title("INICIAR JOGO")
    newWindow.geometry("280x155")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_janela(newWindow))

    label_nome_cliente = Label(newWindow, width=276, height=151)
    label_nome_cliente.place(x=0, y=0)

    jogador_name_input = Entry(newWindow,width = 27)
    jogador_name_input.place(x=98, y=62)

    # https://python-forum.io/thread-26854.html <--- Como fazer o texto de um botão do tkinter ficar em Negrito
    jogar_button = Button(newWindow, text='JOGAR', font='sans 11 bold', width=12, height=int(1.5), command=lambda:conectar_jogador(str(jogador_name_input.get()), newWindow))
    jogar_button.place(x=140, y=96)


def fecha_janela(Toplevel):
    Toplevel.destroy()
    Toplevel.quit()
    root.destroy()
    #os._exit(1)


def fecha_tela(Toplevel):
    Toplevel.destroy()

def conectar_jogador(jogador_name_input, toplevel):
    try:
        global username
        username = jogador_name_input
        client.connect((ServerIP,PORT))
        threading.Thread(target=receiveMessage, args=()).start()
        threading.Thread(target=sendMessage, args=()).start()
        print(f'Conexao bem sucedido no endereco {ServerIP}:{PORT}')
        fecha_tela(toplevel)
        janela_chat()
    except:
        print(f'ERROR: Por favor revise seu endereco: {ServerIP}:{PORT}')


def janela_chat():
    global text_area_chat
    newWindow = Toplevel(root)
    newWindow.title("BEM VINDO!")
    newWindow.geometry("310x390")

#    bg_label = Label(newWindow, image=JANELA_PRINCIPAL_asset)
#    bg_label.place(x=0, y=0)

#    newWindow.protocol("WM_DELETE_WINDOW", mostra_janela_SAIR_PARTIDA)

    # Abaixo instanciamos o widget aonde as mensagens são mostradas no chat.
    text_area_chat = ScrolledText(newWindow, wrap=WORD, width=38, height=12, font=("Callibri", 8))
    text_area_chat.place(x=20, y=150)
    text_area_chat.focus()

    faz_jogada_button = Button(newWindow)
    faz_jogada_button.place(x=150, y=13)
    faz_jogada_button.bind("<Enter>")

    label_mensagem = Entry(newWindow, width=30)
    label_mensagem.pack(padx=10, pady=10)
    label_mensagem.place(x=20, y=300)

    button_envia_mensagem = Button(newWindow, text='ENVIAR', command=lambda:sendMessage(str(label_mensagem.get())))
    button_envia_mensagem.place(x=200, y=350)

    text_area_chat.insert(tk.INSERT, f'Bem vindo ao chat {username}!\n', 'msg')
    text_area_chat.tag_config('msg', foreground='blue')

def receiveMessage():
    global text_area_chat
    while True:
        try:
            message = client.recv(2048).decode('ascii')
            if message=='getUser':
                client.send(username.encode('ascii'))
            else:
                text_area_chat.insert(tk.INSERT, message + '\n')
        except:
            print('ERROR: Check your connection or server might be offline')
            exit()

def sendMessage(message):
    client.send(message.encode('ascii'))

if __name__ == "__main__":
    conexao_cliente()
    root.mainloop()

