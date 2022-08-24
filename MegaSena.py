from tkinter import *
from random import randint

def mega():
    global c
    lista = []
    qnt = valor.get()
    num = 0
    jogo1["text"] = ""
    jogo2["text"] = ""
    jogo3["text"] = ""
    jogo4["text"] = ""
    jogo5["text"] = ""
    jogo6["text"] = ""

    while num < qnt:
        cont = 0
        while True:
            rand = randint(1,60)
            if rand not in lista:
                lista.append(rand)
                cont += 1
            if cont >= 6:
                break
        
        lista.sort()
        if num == 0:
            jogo1["text"] = f"Jogo 1: {lista}"
            main.geometry("500x400+700+150")
        elif num == 1:
            jogo2["text"] = f"Jogo 2: {lista}"
            main.geometry("500x460+700+150")
        elif num == 2:
            jogo3["text"] = f"Jogo 3: {lista}"
            main.geometry("500x520+700+150")
        elif num == 3:
            jogo4["text"] = f"Jogo 4: {lista}"
            main.geometry("500x580+700+150")
        elif num == 4:
            jogo5["text"] = f"Jogo 5: {lista}"
            main.geometry("500x640+700+150")
        elif num == 5:
            jogo6["text"] = f"Jogo 6: {lista}"
            main.geometry("500x700+700+150")

        lista.clear()
        num += 1
    c += 1
    if c == 1:
        tela()
         
def tela():
    
    menu = Tk()
    menu.title("")
    menu.geometry("375x100")
    menu.config(bg = corbg)
    menu.resizable(width = False, height = False)

    msg = Label(menu, text="se ganhar...quero uma parte, hein?", bg=corbg, fg="white", font=("Courier 12"))
    msg.place(x=10, y=35)

c = 0
corbg = "#282829"

main = Tk()
main.title("Sorteador")
main.geometry("500x350+700+150")
main.config(bg = corbg)
main.resizable(width = False, height = False)


title = Label(main, width=2000, text= "MEGA-SENA", bg="#e6e215", fg="black", font=("Courier 25 bold"))
title.pack(side="top")

qntjogos = Label(main, text="Quantidade de Jogos:", bg="#282829", fg="white", font=("Impact 20"))
qntjogos.place(x=125, y=80)

jogo1 = Label(main, text="", bg=corbg, fg="white", font="Courier 18 bold")
jogo1.place(x=30, y=340)
jogo2 = Label(main, text="", bg=corbg, fg="white", font="Courier 18 bold")
jogo2.place(x=30, y=400)
jogo3 = Label(main, text="", bg=corbg, fg="white", font="Courier 18 bold")
jogo3.place(x=30, y=460)
jogo4 = Label(main, text="", bg=corbg, fg="white", font="Courier 18 bold")
jogo4.place(x=30, y=520)
jogo5 = Label(main, text="", bg=corbg, fg="white", font="Courier 18 bold")
jogo5.place(x=30, y=580)
jogo6 = Label(main, text="", bg=corbg, fg="white", font="Courier 18 bold")
jogo6.place(x=30, y=640)


valor = IntVar()

rad1 = Radiobutton(main, text="1", width=3, font="bold 20", value=1, variable=valor, bg=corbg, fg="#9c3030")
rad1.place(x=110, y=140)
rad2 = Radiobutton(main, text="2", width=3, font="Bold 20", value=2, variable=valor, bg=corbg, fg="#9c3030")
rad2.place(x=110, y=180)
rad3 = Radiobutton(main, text="3", width=3, font="Bold 20", value=3, variable=valor, bg=corbg, fg="#9c3030")
rad3.place(x=110, y=220)
rad4 = Radiobutton(main, text="4", width=3, font="Bold 20", value=4, variable=valor, bg=corbg, fg="#9c3030")
rad4.place(x=300, y=140)
rad5 = Radiobutton(main, text="5", width=3, font="Bold 20", value=5, variable=valor, bg=corbg, fg="#9c3030")
rad5.place(x=300, y=180)
rad6 = Radiobutton(main, text="6", width=3, font="Bold 20", value=6, variable=valor, bg=corbg, fg="#9c3030")
rad6.place(x=300, y=220)


button = Button(main, text="SORTEAR", command = mega, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
button.place(x=195, y=270)


main.mainloop()