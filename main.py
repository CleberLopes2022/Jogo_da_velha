import tkinter
from tkinter import *
from tkinter import ttk


# cores ---------------------------------------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black



# criando janela principal

janela = Tk()
janela.title('   Jogo da Velha')
janela.geometry('260x370')
janela.iconphoto(False, PhotoImage(file='jogo-da-velha.png'))
janela.configure(bg=fundo)



# Dividindo a janela em 2 frames

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief=RAISED)
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# configurando o frama_cima
text1 = StringVar()
text2 = StringVar()

app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=26, y=10)

app_x = Label(frame_cima, textvariable=text1, height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=25, y=70)

app_xp = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_xp.place(x=80, y=20)


app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_separador.place(x=110, y=20)


app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=170, y=10)

app_o = Label(frame_cima, textvariable=text2, height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=175, y=70)

app_op = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_op.place(x=130, y=20)


# configurando o frama_baixo


# criando funções do app

Jogador_1 = "X"
Jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [[1,2,3],[4,5,6],[7,8,9]]

jogando = 'X'
contador = 0
jogar = ''
contador_de_rodadas = 0
nome1_label = ''
nome1_entry = ''
nome1_label = ''
nome2_entry = ''

def iniciar_jogo():

    # pra controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar
        global cor


        # comparando o valor recebido
        if i==str(1):
            # verificando se aquela posicao esta vazia ou não
            if b_0['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_0['fg']= cor
                b_0['text']= jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')

        if i==str(2):
            # verificando se aquela posicao esta vazia ou não
            if b_1['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_1['fg']= cor
                b_1['text']= jogando
                tabela[0][1] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')

        if i==str(3):
            # verificando se aquela posicao esta vazia ou não
            if b_2['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_2['fg']= cor
                b_2['text']= jogando
                tabela[0][2] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
        if i==str(4):
            # verificando se aquela posicao esta vazia ou não
            if b_3['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_3['fg']= cor
                b_3['text']= jogando
                tabela[1][0] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
        if i==str(5):
            # verificando se aquela posicao esta vazia ou não
            if b_4['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_4['fg']= cor
                b_4['text']= jogando
                tabela[1][1] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
        if i==str(6):
            # verificando se aquela posicao esta vazia ou não
            if b_5['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_5['fg']= cor
                b_5['text']= jogando
                tabela[1][2] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
        if i==str(7):
            # verificando se aquela posicao esta vazia ou não
            if b_6['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_6['fg']= cor
                b_6['text']= jogando
                tabela[2][0] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
        if i==str(8):
            # verificando se aquela posicao esta vazia ou não
            if b_7['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_7['fg']= cor
                b_7['text']= jogando
                tabela[2][1] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
        if i==str(9):
            # verificando se aquela posicao esta vazia ou não
            if b_8['text']=='':
                # verificando quem esta jogando e assim definir simbolo
                if jogando =='X':
                    cor=co7
                if jogando == 'O':
                    cor=co8

                # definindo a cor do text do botao e marcar aquela posição da tabela 
                b_8['fg']= cor
                b_8['text']= jogando
                tabela[2][2] = jogando

                # verificando quem esta jogando para trocar de simbolo
                if jogando == 'X':
                    jogando = 'O' 
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X' 
                    jogar = 'Jogador 2'
                # incrementar o contador
                contador+=1

                # apos o contador ser maior ou igual a 5, verificar se houve algum vencedor
                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1]==tabela[0][2]!="":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                        vencedor(jogando)

                    # diagonal
                    if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                        vencedor(jogando)

                    # Empate
                    if contador>=9:
                        vencedor('foi empate')
    
    
    # decidir o vencedor 

    def vencedor(i):
        global score_1
        global score_2
        global tabela
        global contador_de_rodadas
        global contador


        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=40, y=220)

        if i=='X':
            score_2+=1
            app_vencedor['text'] = app_o['text'] + ' venceu'
            app_op['text'] = score_2

        if i==('O'):
            score_1+=1
            app_vencedor['text'] = app_x['text'] + ' venceu'
            app_xp['text'] = score_1

        if i == 'foi empate': 
            app_vencedor['text'] = ' foi um empate'

        def start():
            # limpando os botoes

            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''

            b_0['state'] = 'normal'
            b_1['state'] = 'normal'
            b_2['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'


            app_vencedor.destroy()
            b_jogar.destroy()

        b_jogar = Button(frame_baixo,command=start, text='Proxima rodada', padx=5,pady=2, font=('Ivy 10 bold'), overrelief=RIDGE,relief=RAISED, bg=fundo, fg=co0)
        b_jogar.place(x=70, y=195)

        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()
            terminar()

        if contador_de_rodadas>=2:
            if score_1 > score_2:
                app_fim = Label(frame_baixo, text= app_x['text'] + ' venceu', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
                app_fim.place(x=30, y=120)

            elif score_1 == score_2:
                app_fim = Label(frame_baixo, text='Empatou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
                app_fim.place(x=30, y=120)
            elif score_2 > score_1:
                app_fim = Label(frame_baixo, text= app_o['text'] + 'venceu', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
                app_fim.place(x=30, y=120)
            jogo_acabou()
        else:
            contador_de_rodadas+=1
            tabela = [[1,2,3],[4,5,6],[7,8,9]]
            contador = 0


    # pra terminar o jogo atual
    def terminar():
        global tabela
        global contador_de_rodadas
        global score_1
        global score_2
        global contador

        tabela = [[1,2,3],[4,5,6],[7,8,9]]
        contador_de_rodadas = 0
        score_1 = 0
        score_2 = 0
        contador = 0

        # bloqueando os botoes

        b_0['state'] = 'disable'
        b_1['state'] = 'disable'
        b_2['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_fim = Label(frame_baixo, text='O jogo acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_fim.place(x=25, y=90)

        # jogar de novo

        def jogar_denovo():
            app_xp['text'] = '0'
            app_op['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            iniciar_jogo()

        

        b_jogar = Button(frame_baixo,command=jogar_denovo, text='Jogar de novo', width=10, padx=5,pady=2, font=('Ivy 10 bold'), overrelief=RIDGE,relief=RAISED, bg=fundo, fg=co0)
        b_jogar.place(x=85, y=197)


    # linhas verticais

    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=90, y=15)

    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=160, y=15)


    # linhas horizontais

    app_ = Label(frame_baixo, text=' ', width=47, relief='flat', padx=2,pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=30, y=63)

    app_ = Label(frame_baixo, text=' ', width=47, relief='flat', padx=2,pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
    app_.place(x=30, y=127)

    # linha 0

    b_0 = Button(frame_baixo, text='',command=lambda:controlar('1'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_0.place(x=30, y=15)

    b_1 = Button(frame_baixo, text='',command=lambda:controlar('2'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_1.place(x=97, y=15)

    b_2 = Button(frame_baixo, text='',command=lambda:controlar('3'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_2.place(x=164, y=15)

    # linha 1

    b_3 = Button(frame_baixo, text='',command=lambda:controlar('4'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_3.place(x=30, y=75)

    b_4 = Button(frame_baixo, text='',command=lambda:controlar('5'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_4.place(x=97, y=75)

    b_5 = Button(frame_baixo, text='',command=lambda:controlar('6'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_5.place(x=164, y=75)

    # linha 0

    b_6 = Button(frame_baixo, text='',command=lambda:controlar('7'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_6.place(x=30, y=135)

    b_7 = Button(frame_baixo, text='',command=lambda:controlar('8'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_7.place(x=97, y=135)

    b_8 = Button(frame_baixo, text='',command=lambda:controlar('9'), width=3, relief='flat', padx=5,pady=2, font=('Ivy 19 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
    b_8.place(x=165, y=135)



def entrada_nome():


    nome1_label = Label(frame_baixo, width=13,  text ='Nome Jogador 1', font=('Ivy 7 bold'))
    nome1_entry = Entry(frame_baixo, textvariable=text1, width=20, font=('Ivy 7 bold'))
    nome1_label.place(x=30, y=50)
    nome1_entry.place(x=115, y= 50 )


    nome2_label = Label(frame_baixo,width=13, text ='Nome Jogador 2', font=('Ivy 7 bold'))
    nome2_entry = Entry(frame_baixo,textvariable=text2, width=20, font=('Ivy 7 bold'))
    nome2_label.place(x=30,y=90 )
    nome2_entry.place(x=115, y=90)
    

    nome1_entry.get()
    nome2_entry.get()
      
entrada_nome()


# botão jogar

b_jogar = Button(frame_baixo,command=iniciar_jogo, text='Jogar', width=10, padx=5,pady=2, font=('Ivy 10 bold'), overrelief=RIDGE,relief=RAISED, bg=fundo, fg=co0)
b_jogar.place(x=85, y=197)

janela.mainloop()