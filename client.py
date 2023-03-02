import socket
import threading

from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
import tkinter as tk

from const import *

"""
Cria objeto "Tkinter"/"Tk"
"""
root = tk.Tk()
root.withdraw()

#HOST = input("Server IP: ")
#PORT = int(input("Port: "))

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
        client.connect((HOST,PORT))
        threading.Thread(target=receiveMessage, args=()).start()
        threading.Thread(target=sendMessage, args=()).start()
        print(f'Conexao bem sucedido no endereco {HOST}:{PORT}')
        fecha_tela(toplevel)
        janela_chat()
    except:
        print(f'ERROR: Por favor revise seu endereco: {HOST}:{PORT}')


def janela_chat():
    global text_area_chat
    newWindow = Toplevel(root)
    newWindow.title("BEM VINDO!")
    newWindow.geometry("660x390")
#    newWindow.configure(bg="#3b3b3b")

    frame_chat = Frame(newWindow, width=310, height=390, bg="#808080", pady=0, padx=0 )
    frame_chat.grid(row=1, column=0)

#    newWindow.protocol("WM_DELETE_WINDOW", mostra_janela_SAIR_PARTIDA)

    #CHAT
    # Abaixo instanciamos o campo de texto aonde as mensagens são mostradas no chat.
    text_area_chat = ScrolledText(frame_chat, wrap=WORD, width=38, height=12, font=("Callibri", 8))
    text_area_chat.place(x=20, y=150)
    text_area_chat.focus()

    label_mensagem = Entry(frame_chat, width=30)
    label_mensagem.pack(padx=10, pady=10)
    label_mensagem.place(x=20, y=300)

    button_envia_mensagem = Button(frame_chat, text='ENVIAR', command=lambda:sendMessage(str(label_mensagem.get())))
    button_envia_mensagem.place(x=200, y=350)

    text_area_chat.insert(tk.INSERT, f'Bem vindo ao chat {username}!\n', 'msg')
    text_area_chat.tag_config('msg', foreground='blue')


    # TABULEIRO
    frame_tabuleiro = Frame(newWindow, width=350, height=390, bg="#3b3b3b", pady=0, padx=10 )
    frame_tabuleiro.grid(row=1, column=1)

    # Configurando as linhas do tabuleiro -----------------

    #### Vertical lines
    #### height tamanho x esquerda y topo
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0,pady=5, relief="flat", anchor="center",
                   font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0,pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=90, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0,pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=130, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0,pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=170, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=210, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=250, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=290, y=90)

    ### Horizontal lines
    ### width lateral x esquerda y top
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=90)
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=130)
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=170)
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=210)
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=250)
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=290)
    app_b = Label(frame_tabuleiro, text="  ", width=240, padx=0, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=330)

    ### Botões do tabuleiro
    b_1 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT,overrelief=RIDGE, command=lambda:efetuar_jogada())
    b_1.place(x=50, y=93)
    b_2 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT,overrelief=RIDGE)
    b_2.place(x=90, y=93)
    b_3 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE)
    b_3.place(x=130, y=93)
    b_4 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE)
    b_4.place(x=170, y=93)
    b_5 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE)
    b_5.place(x=210, y=93)
    b_6 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE)
    b_6.place(x=250, y=93)


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

