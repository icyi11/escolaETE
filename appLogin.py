import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.config(bg="#2B2C2D")
    
janela.geometry('400x200')
janela.resizable(False, False)

janela.title("Login")

titulo = tk.Label(text="Login", font=("Arial", 18, "bold"), bg="#2B2C2D", fg="#FFFFFF")
titulo.place(rely=0.1, relx=0.5, anchor='center')

labelUser = tk.Label(text="Insira seu nome", bg="#2B2C2D", fg="#FFFFFF")
labelUser.place(rely=0.33, relx=0.5, anchor="center")

entraUser = tk.Entry()
entraUser.place(rely=0.45, relx=0.5, anchor='center')

labelSenha = tk.Label(text="Insira sua senha", bg="#2B2C2D", fg="#FFFFFF")
labelSenha.place(rely=0.60, relx=0.5, anchor='c')

entraSenha = tk.Entry()
entraSenha.place(rely=0.72, relx=0.5, anchor='center')

def abrecadcliente():
    nelacliente = tk.Toplevel()
    nelacliente.title("Cadastro de Cliente")
    nelacliente.geometry('500x300')
    nelacliente.config(bg='#2B2C2D')
    nelacliente.resizable(False, False)
    titcadcliente = tk.Label(nelacliente, text='Cadastro de Cliente', bg="#2B2C2D", fg="#FFFFFF", font=("Arial", 18))
    titcadcliente.place(rely=0.05, relx=0.5, anchor='c')
    labNome = tk.Label(nelacliente, text="Nome", bg="#2B2C2D", fg="#FFFFFF")
    labNome.place(rely=0.35, relx=0.2, anchor='c')
    entryNome = tk.Entry(nelacliente)
    entryNome.place(rely=0.35, relx=0.5, anchor='c')
    labEdrc = tk.Label(nelacliente, text="Endereço", bg="#2B2C2D", fg="#FFFFFF")
    labEdrc.place(rely=0.45, relx=0.2, anchor='c')
    entryEdrc = tk.Entry(nelacliente)
    entryEdrc.place(rely=0.45, relx=0.5, anchor='c')
    labEmail = tk.Label(nelacliente, text="Email", bg="#2B2C2D", fg="#FFFFFF")
    labEmail.place(rely=0.55, relx=0.2, anchor='c')
    entryEmail = tk.Entry(nelacliente)
    entryEmail.place(rely=0.55, relx=0.5, anchor='c')
    labTele = tk.Label(nelacliente, text="Telefone", bg="#2B2C2D", fg="#FFFFFF")
    labTele.place(rely=0.65, relx=0.2, anchor='c')
    entryTele = tk.Entry(nelacliente)
    entryTele.place(rely=0.65, relx=0.5, anchor='c')
    butSave = tk.Button(nelacliente, text="Salvar", bg="#2B2C2D", fg="#FFFFFF")
    butSave.place(rely=0.9, relx= 0.33, anchor='c')
    butCancel = tk.Button(nelacliente, text="Cancelar", bg="#2B2C2D", fg="#FFFFFF")
    butCancel.place(rely=0.9, relx= 0.66, anchor='c')

def checklogin():
    nome = entraUser.get()
    senha = entraSenha.get()
    if nome == "admin" and senha == "1234":
        novjanela = tk.Toplevel()
        novjanela.config(bg='#2B2C2D')
        novjanela.resizable(False, False)
        novjanela.geometry('800x600')
        novjanela.title("Principal")
        titcads = tk.Label(novjanela, text='Menu Principal', bg="#2B2C2D", fg="#FFFFFF", font=("Arial", 18))
        titcads.place(rely=0.05, relx=0.5, anchor='c')
        cadCliente = tk.Button(novjanela, text="Cliente", bg="#2B2C2D", fg="#FFFFFF", command=abrecadcliente)
        cadCliente.place(rely=0.15, relx=0.5, anchor='c')
    else:
        messagebox.showerror("Erro", "Nome e/ou senha incorreto(a)")

butLogin = tk.Button(text="Entrar", bg="#2B2C2D", fg="#FFFFFF", command=checklogin)
butLogin.place(rely=0.9, relx=0.5, anchor='c')

janela.mainloop()