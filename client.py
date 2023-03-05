import json
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

# HOST = input("Server IP: ")
# PORT = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
text_area_chat = ScrolledText()
label_peca = Label()
b1 = b2 = b3 = b4 = b5 = b6 = Button()


def conexao_cliente():
    newWindow = Toplevel(root)
    newWindow.title("INICIAR JOGO")
    newWindow.geometry("280x155")

    newWindow.protocol("WM_DELETE_WINDOW", lambda: fecha_janela(newWindow))

    label_nome_cliente = Label(newWindow, width=276, height=151)
    label_nome_cliente.place(x=0, y=0)

    jogador_name_input = Entry(newWindow, width=27)
    jogador_name_input.place(x=98, y=62)

    # https://python-forum.io/thread-26854.html <--- Como fazer o texto de um botão do tkinter ficar em Negrito
    jogar_button = Button(newWindow, text='JOGAR', font='sans 11 bold', width=12, height=int(1.5),
                          command=lambda: conectar_jogador(str(jogador_name_input.get()), newWindow))
    jogar_button.place(x=140, y=96)


def fecha_janela(Toplevel):
    Toplevel.destroy()
    Toplevel.quit()
    root.destroy()
    # os._exit(1)


def fecha_tela(Toplevel):
    Toplevel.destroy()


def conectar_jogador(jogador_name_input, toplevel):
    try:
        global username
        global message
        username = jogador_name_input
        client.connect((HOST, PORT))
        threading.Thread(target=receiveMessage, args=()).start()
        threading.Thread(target=sendMessage, args=()).start()
        print(f'Conexao bem sucedido no endereco {HOST}:{PORT}')
        fecha_tela(toplevel)
        janela_chat()
    except:
        print(f'ERROR: Por favor revise seu endereco: {HOST}:{PORT}')


def janela_chat():
    global text_area_chat, label_peca
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,\
        b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36
    newWindow = Toplevel(root)
    newWindow.title("BEM VINDO!")
    newWindow.geometry("660x390")
    #    newWindow.configure(bg="#3b3b3b")

    frame_chat = Frame(newWindow, width=310, height=390, bg="#808080", pady=0, padx=0)
    frame_chat.grid(row=1, column=0)

    #    newWindow.protocol("WM_DELETE_WINDOW", mostra_janela_SAIR_PARTIDA)

    # CHAT
    # Abaixo instanciamos o campo de texto aonde as mensagens são mostradas no chat.
    text_area_chat = ScrolledText(frame_chat, wrap=WORD, width=38, height=12, font=("Callibri", 8))
    text_area_chat.place(x=20, y=150)
    text_area_chat.focus()

    label_mensagem = Entry(frame_chat, width=30)
    label_mensagem.pack(padx=10, pady=10)
    label_mensagem.place(x=20, y=300)

    button_envia_mensagem = Button(frame_chat, text='ENVIAR', command=lambda: sendMessage(
        '{"event":"CHAT", "message":"' + str(label_mensagem.get()) + '"}'))
    button_envia_mensagem.place(x=200, y=350)

    text_area_chat.insert(tk.INSERT, f'Bem vindo ao chat {username}!\n', 'msg')
    text_area_chat.tag_config('msg', foreground='blue')

    # TABULEIRO
    frame_tabuleiro = Frame(newWindow, width=350, height=390, bg="#3b3b3b", pady=0, padx=10)
    frame_tabuleiro.grid(row=1, column=1)

    # Configurando as linhas do tabuleiro -----------------

    #### Vertical lines
    #### height tamanho x esquerda y topo
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=50, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=90, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
                  font=('Ivy 1 bold'), bg="#FFFFFF", fg="#FFFFFF")
    app_b.place(x=130, y=90)
    app_b = Label(frame_tabuleiro, text="   ", height=78, padx=0, pady=5, relief="flat", anchor="center",
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
    b1 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(1))
    b1.place(x=50, y=93)
    b2 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(2))
    b2.place(x=90, y=93)
    b3 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(3))
    b3.place(x=130, y=93)
    b4 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(4))
    b4.place(x=170, y=93)
    b5 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(5))
    b5.place(x=210, y=93)
    b6 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                 font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(6))
    b6.place(x=250, y=93)

    b7 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(7))
    b7.place(x=50, y=133)
    b8 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(8))
    b8.place(x=90, y=133)
    b9 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(9))
    b9.place(x=130, y=133)
    b10 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(10))
    b10.place(x=170, y=133)
    b11 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(11))
    b11.place(x=210, y=133)
    b12 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(12))
    b12.place(x=250, y=133)

    b13 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(13))
    b13.place(x=50, y=173)
    b14 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(14))
    b14.place(x=90, y=173)
    b15 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(15))
    b15.place(x=130, y=173)
    b16 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(16))
    b16.place(x=170, y=173)
    b17 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(17))
    b17.place(x=210, y=173)
    b18 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(18))
    b18.place(x=250, y=173)

    b19 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(19))
    b19.place(x=50, y=213)
    b20 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(20))
    b20.place(x=90, y=213)
    b21 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(21))
    b21.place(x=130, y=213)
    b22 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(22))
    b22.place(x=170, y=213)
    b23 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(23))
    b23.place(x=210, y=213)
    b24 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(24))
    b24.place(x=250, y=213)

    b25 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(25))
    b25.place(x=50, y=253)
    b26 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(26))
    b26.place(x=90, y=253)
    b27 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(27))
    b27.place(x=130, y=253)
    b28 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(28))
    b28.place(x=170, y=253)
    b29 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(29))
    b29.place(x=210, y=253)
    b30 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(30))
    b30.place(x=250, y=253)

    b31 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(31))
    b31.place(x=50, y=293)
    b32 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(32))
    b32.place(x=90, y=293)
    b33 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(33))
    b33.place(x=130, y=293)
    b34 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(34))
    b34.place(x=170, y=293)
    b35 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(35))
    b35.place(x=210, y=293)
    b36 = Button(frame_tabuleiro, text="", width=1, height=1, bg="#000000", fg="#000000",
                font=('Ivy 15 bold'), relief=FLAT, overrelief=RIDGE, command=lambda: efetuar_jogada(36))
    b36.place(x=250, y=293)

    #BG cor de fundo  FG cor da letra
    label_peca = Label(frame_tabuleiro, text="Peças disponíveis: 8", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 15 bold'),
                   bg="#808080", fg="#FFFFFF")
    label_peca.place(x=50, y=340)

def efetuar_jogada(posicao):
    global peca_disponivel, numero_jogador, ultima_jogada
    if(peca_disponivel == 0):
        janela_aviso()
        print("Você nao tem mais peça disponivel")
    else:
        if int(numero_jogador) == int(ultima_jogada):
            print("Nao é sua vez de jogar, aguarde o próximo jogador")
        else:
            peca_disponivel -= 1
            sendMessage('{"event":"JOGADA1", "posicao":"' + str(posicao) + '"}')
            valida_empurrao(posicao)


def valida_empurrao(posicao):
    #Movendo a peça superior
    if (int(posicao) - 6 ) < 0:
        pass
    elif (int(posicao) - 12) < 0 and globals()[f"p{(int(posicao) - 6)}"] != -1:
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao - 6) + '", "value": "' + str(globals()[f"p{(int(posicao) - 6)}"]) + '"}')
    elif (int(posicao) - 6) > 0 and (int(posicao) - 12) > 0 and globals()[f"p{(int(posicao) - 6)}"] != -1 and globals()[f"p{(int(posicao) - 12)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao-6) + '", "posicaofinal": "' + str(posicao-12) +'", "value": "' + str(globals()[f"p{(int(posicao) - 6)}"]) +'"}')

    # Movendo a peça inferior
    if (int(posicao) + 6 ) > 36:
        pass
    elif (int(posicao) + 12) > 36 and globals()[f"p{(int(posicao) + 6)}"] != -1:
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao + 6) + '", "value": "' + str(globals()[f"p{(int(posicao) + 6)}"]) + '"}')
    elif (int(posicao) + 6) > 0 and (int(posicao) + 12) > 0 and globals()[f"p{(int(posicao) + 6)}"] != -1 and globals()[f"p{(int(posicao) + 12)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao+6) + '", "posicaofinal": "' + str(posicao+12) +'", "value": "' + str(globals()[f"p{(int(posicao) + 6)}"]) +'"}')

    # Movendo a peça esquerda
    if (int(posicao-1) % 6) == 1 and globals()[f"p{(int(posicao) - 1)}"] != -1:
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao - 1) + '", "value": "' + str(globals()[f"p{(int(posicao) - 1)}"]) + '"}')
    elif (int(posicao) - 1) > 0 and (int(posicao) - 2) > 0 and globals()[f"p{(int(posicao) - 1)}"] != -1 and globals()[f"p{(int(posicao) - 2)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao-1) + '", "posicaofinal": "' + str(posicao-2) +'", "value": "' + str(globals()[f"p{(int(posicao) - 1)}"]) +'"}')

    # Movendo a peça direita
    if (int(posicao+1) % 6) == 0 and globals()[f"p{(int(posicao) + 1)}"] != -1:
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao + 1) + '", "value": "' + str(globals()[f"p{(int(posicao) + 1)}"]) + '"}')
    elif (int(posicao) + 1) > 0 and (int(posicao) + 2) > 0 and globals()[f"p{(int(posicao) + 1)}"] != -1 and \
            globals()[f"p{(int(posicao) + 2)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao+1) + '", "posicaofinal": "' + str(posicao+2) +'", "value": "' + str(globals()[f"p{(int(posicao) + 1)}"]) +'"}')

    # Movendo a peça diagonal superior esquerda
    if ((int(posicao) - 7) < 0):
        pass
    elif ((int(posicao) - 14) < 0 and globals()[f"p{(int(posicao) - 7)}"] != -1) or ((int(posicao-7) % 6) == 1 and globals()[f"p{(int(posicao) - 7)}"] != -1):
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao - 7) + '", "value": "' + str(globals()[f"p{(int(posicao) - 7)}"]) + '"}')
    elif (int(posicao) - 7) > 0 and (int(posicao) - 14) > 0 and globals()[f"p{(int(posicao) - 7)}"] != -1 and \
            globals()[f"p{(int(posicao) - 14)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao - 7) + '", "posicaofinal": "' + str(
            posicao - 14) + '", "value": "' + str(globals()[f"p{(int(posicao) - 7)}"]) + '"}')

    # Movendo a peça diagonal superior direita
    if ((int(posicao) - 5) < 0):
        pass
    elif ((int(posicao) - 10) < 0 and globals()[f"p{(int(posicao) - 5)}"] != -1) or ((int(posicao-5) % 6) == 0 and globals()[f"p{(int(posicao) - 5)}"] != -1):
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao - 5) + '", "value": "' + str(globals()[f"p{(int(posicao) - 5)}"]) + '"}')
    elif (int(posicao) -5) > 0 and (int(posicao) - 10) > 0 and globals()[f"p{(int(posicao) - 5)}"] != -1 and \
            globals()[f"p{(int(posicao) - 10)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao - 5) + '", "posicaofinal": "' + str(
            posicao - 10) + '", "value": "' + str(globals()[f"p{(int(posicao) - 5)}"]) + '"}')

    # Movendo a peça diagonal inferior esquerda
    if ((int(posicao) + 5) > 36):
        pass
    elif ((int(posicao) + 10) > 36 and globals()[f"p{(int(posicao) + 5)}"] != -1) or ((int(posicao+5) % 6) == 0 and globals()[f"p{(int(posicao) + 5)}"] != -1):
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao + 5) + '", "value": "' + str(globals()[f"p{(int(posicao) + 5)}"]) + '"}')
    elif (int(posicao) + 5) < 36 and (int(posicao) + 10) < 36 and globals()[f"p{(int(posicao) + 5)}"] != -1 and globals()[f"p{(int(posicao) + 10)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao + 5) + '", "posicaofinal": "' + str(
            posicao + 10) + '", "value": "' + str(globals()[f"p{(int(posicao) + 5)}"]) + '"}')

    # Movendo a peça diagonal inferior direita
    if ((int(posicao) + 7) > 36):
        pass
    elif ((int(posicao) + 14) > 36 and globals()[f"p{(int(posicao) + 7)}"] != -1) or ((int(posicao+7) % 6) == 0 and globals()[f"p{(int(posicao) + 7)}"] != -1):
        sendMessage('{"event":"MOVEPECAPARAMAO", "posicaoinicial":"' + str(posicao + 7) + '", "value": "' + str(globals()[f"p{(int(posicao) + 7)}"]) + '"}')
    elif (int(posicao) + 7) < 36 and (int(posicao) + 14) < 36 and globals()[f"p{(int(posicao) + 7)}"] != -1 and globals()[
        f"p{(int(posicao) + 14)}"] == -1:
        sendMessage('{"event":"MOVEPECA", "posicaoinicial":"' + str(posicao + 7) + '", "posicaofinal": "' + str(
            posicao + 14) + '", "value": "' + str(globals()[f"p{(int(posicao) + 7)}"]) + '"}')


def receiveMessage():
    global text_area_chat, numero_jogador, ultima_jogada, label_peca, peca_disponivel

    while True:
        try:
            message = client.recv(2048).decode(DEFAULT_ENCODING)
            entrada = []
            for i in list(message):
                entrada.append(i)
                if(i == '}'):
                    #print(message)
                    jsonData = json.loads(str("".join(entrada)))
                    print("ReceiveMessageClient")
                    print(jsonData)
                    if jsonData['event'] == 'getUser':
                        client.send(username.encode(DEFAULT_ENCODING))
                        usernames.append(username)
                        numero_jogador = jsonData['index']
                        #print("Novo numero do jogador")
                        #print(numero_jogador)

                    elif jsonData['event'] == 'CHAT':
                        text_area_chat.insert(tk.INSERT, jsonData['name'] + ':' + jsonData['message'] + '\n')

                    elif jsonData['event'] == 'JOGADA1':
                        posicao = jsonData['posicao']
                        ultima_jogada = jsonData['index']
                        globals()[f"b{posicao}"]['bg'] = cors[jsonData['index']]
                        globals()[f"b{posicao}"]['fg'] = cors[jsonData['index']]
                        globals()[f"p{posicao}"] = jsonData['index']

                        label_peca['text'] = "Peças disponíveis: " + str(peca_disponivel)

                    elif jsonData['event'] == 'JOGADA2':
                        print("JOGADA2")
                        #text_area_chat.insert(tk.INSERT, jsonData['name'] + ':' + jsonData['message'] + '\n')

                    elif jsonData['event'] == 'MOVEPECA':
                        posicaoinicial = int(jsonData['posicaoinicial'])
                        posicaofinal = int(jsonData['posicaofinal'])
                        #Setando casa nova
                        globals()[f"b{posicaofinal}"]['bg'] = cors[int(jsonData['value'])]
                        globals()[f"b{posicaofinal}"]['fg'] = cors[int(jsonData['value'])]
                        globals()[f"p{posicaofinal}"] = int(jsonData['value'])
                        # Liberando casa antiga
                        globals()[f"b{posicaoinicial}"]['bg'] = "#000000"
                        globals()[f"b{posicaoinicial}"]['fg'] = "#000000"
                        globals()[f"p{posicaoinicial}"] = -1

                    elif jsonData['event'] == 'MOVEPECAPARAMAO':
                        posicaoinicial = int(jsonData['posicaoinicial'])
                        if(jsonData['value'] == numero_jogador):
                            peca_disponivel += 1
                        # Liberando casa antiga
                        globals()[f"b{posicaoinicial}"]['bg'] = "#000000"
                        globals()[f"b{posicaoinicial}"]['fg'] = "#000000"
                        globals()[f"p{posicaoinicial}"] = -1

                        label_peca['text'] = "Peças disponíveis: " + str(peca_disponivel)


                    else:
                        print("Else")

                    entrada = []
        except:
            print('ERROR: Check your connection or server might be offline')
            exit()


def sendMessage(message = ''):
    client.send(message.encode(DEFAULT_ENCODING))



# JANELAS
def janela_aviso():
    newWindow = Toplevel(root)
    newWindow.title("Servidor: Aviso!")
    newWindow.geometry("360x205")

    nao_button = Button(newWindow, text='OK', width=12, command=lambda:action_nao(newWindow))
    nao_button.place(x=240, y=154)


def action_nao(Toplevel):
    Toplevel.destroy()








if __name__ == "__main__":
    conexao_cliente()
    root.mainloop()
