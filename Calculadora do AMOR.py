from tkinter import *
import random
root = Tk()
root.title("Calculadora do Amor")
root.geometry("450x400")
root.resizable(0,0)

def app():
    v1 = selecionado_1.get()
    v2 = selecionado_2.get()
    nome_1 = e_seu_nome.get()
    nome_2 = e_parceiro_nome.get()
    st = '0123456789'
    digitos = 2
    resultado1 = "".join(random.sample(st, digitos))
    mesagem = f'Percentagem de amor entre:' \
              f'\n{v1} & {v2} \n{nome_1} & {nome_2}\n {resultado1}  % '
    resultado.set(mesagem)

frameCima = Frame( width=500, height=50, bg="#3d85c6",  relief="flat",)
frameCima.grid(row=0, column=0)
frameMeio = Frame( width=500, height=250, bg="#073763",  relief="solid",)
frameMeio.grid(row=1, column=0)
framefim = Frame( width=500, height=100, bg="#cfe2f3",  relief="solid",)
framefim.grid(row=2, column=0)
titulo = Label(frameCima,text="Calculadora do Amor",
               bg="#3d85c6",fg="red",font=("arial","15","bold"))
titulo.place(relx=0.25,rely=0.2)

textonome = Label(frameMeio,text="Digite o seu nome",
                  bg="#073763",fg="#bf9000",font=("arial","10","bold"))
textonome.place(relx=0.1,rely=0.15)
e_seu_nome = Entry(frameMeio,width=10,
                   font=('Ivy 14 '), justify='center',relief="solid")
e_seu_nome.place(relx=0.1,rely=0.3)
selecionado_1 = StringVar()
rad_1 = Radiobutton(frameMeio, text='Homem',
                    font=('Ivy 10'), value='Homem',
                    variable=selecionado_1).place(relx=0.15,rely=0.45)
rad_2 = Radiobutton(frameMeio, text='Mulher',font=('Ivy 10'), value='Mulher',
                    variable=selecionado_1).place(relx=0.15,rely=0.55)
texto2 = Label(frameMeio,text="Digite o nome do(a) parceiro(a)",bg="#073763",
               fg="#bf9000",font=("arial","10","bold"))
texto2.place(relx=0.45,rely=0.15)
e_parceiro_nome = Entry(frameMeio,width=10,
                        font=('Ivy 14 '), justify='center',relief="solid")
e_parceiro_nome.place(relx=0.55,rely=0.3)
selecionado_2 = StringVar()
rad_3 = Radiobutton(frameMeio, text='Homem', font=('Ivy 10'),
                    value='Homem', variable=selecionado_2).place(relx=0.55,rely=0.45)
rad_4 = Radiobutton(frameMeio, text='Mulher',font=('Ivy 10'),
                    value='Mulher', variable=selecionado_2).place(relx=0.55,rely=0.55)
bt_calcular = Button(frameMeio,text="Calcular o Amor",
                                   bd=2, bg='#107db2', fg='white',
                                   font=('verdana', 12, 'bold'),command=app)
bt_calcular.place(relx=0.3, rely=0.75, relwidth=0.3, relheight=0.1)
resultado = StringVar()
resultado_texto = Label(framefim,textvariable=resultado, font=("Arial", "12", "bold")
                                      , bg="#cfe2f3", fg='#107db2')
resultado_texto.place(relx=0.2, rely=0.15)
root.mainloop()