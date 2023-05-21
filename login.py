import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import bcrypt
import gerenciadorBanco as banco
from gerenciadorBanco import validacaoSenhaUsuario

janela = ctk.CTk()
class Aplicacao():

    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaPrincipal()
        janela.mainloop()

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("380x396")
        janela.title("Login")
        # janela.iconbitmap("login.ico")
        janela.resizable(False, False) # Trava a janela em tamanho unico

        # Calcula as dimensoes da tela
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        # Calcula a posicao central da janela
        largura_janela = 380
        altura_janela = 396
        posicao_x = int((largura_tela / 2) - (largura_janela / 2))
        posicao_y = int((altura_tela / 2) - (altura_janela / 2))

        # Define a posicao central
        janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

    def telaPrincipal(self):
        # Frame
        loginFrame = ctk.CTkFrame(master=janela, width=360, height=376)
        loginFrame.pack(expand=True, anchor="center")

        # Widgets texto 'Login'
        tituloLabel = ctk.CTkLabel(master=loginFrame, text="Gerenciador PWD", font=("Roboto", 20))
        tituloLabel.place(x=0, y=0, relwidth=1, relheight=0.2)

        # Faz a validacao de login
        def validarLogin():
            email = emailLogin.get()
            senha = senhaLogin.get()

            senhaSalva = validacaoSenhaUsuario(email)

            if banco.validarLogin(email, senha):
                messagebox.showinfo(title=None, message="Login bem-sucedido.")
            else:
                messagebox.showwarning(title=None, message="Email ou senha incorretos.")

        # Campo email e senha
        emailLogin = ctk.CTkEntry(master=loginFrame, placeholder_text="Email", width=300, font=("Roboto", 14))
        emailLogin.place(relx=0.5, rely=0.4, anchor=CENTER)
        senhaLogin = ctk.CTkEntry(master=loginFrame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*")
        senhaLogin.place(relx=0.5, rely=0.5, anchor=CENTER)


        # Botoes entrar
        botaoEntrar = ctk.CTkButton(master=loginFrame, text="Entrar", width=300, fg_color="#2196F3", text_color="black", hover_color="#1565C0", command=validarLogin)
        botaoEntrar.place(relx=0.5, rely=0.6, anchor=CENTER)

        # Botao Cadastrar
        def telaCadastro():
            loginFrame.pack_forget()
            
            # Tela cadastro
            cadastroFrame = ctk.CTkFrame(master=janela, width=360, height=376)
            cadastroFrame.pack(expand=True, anchor="center")

            # Texto 'cadastro'
            cadastroLabel = ctk.CTkLabel(master=cadastroFrame, text="Cadastro", font=("Roboto", 20))
            cadastroLabel.place(x=0, y=0, relwidth=1, relheight=0.2)

            # Campo email
            emailCadastro = ctk.CTkEntry(master=cadastroFrame, placeholder_text="Email", width=300, font=("Roboto", 14))
            emailCadastro.place(relx=0.5, rely=0.4, anchor=CENTER)

            # Campo senha
            senhaCadastro = ctk.CTkEntry(master=cadastroFrame, placeholder_text="Senha", width=300, font=("Roboto", 14), show="*")
            senhaCadastro.place(relx=0.5, rely=0.5, anchor=CENTER)

            # Campo repetir senha
            senha2Cadastro = ctk.CTkEntry(master=cadastroFrame, placeholder_text="Repetir senha", width=300, font=("Roboto", 14), show="*")
            senha2Cadastro.place(relx=0.5, rely=0.6, anchor=CENTER)


            def voltarLogin():
                # Tira o frame cadastro
                cadastroFrame.pack_forget()
                # Volta com  o frame login
                loginFrame.pack(expand=True, anchor="center")
            

            # Botao voltar
            BotaoVoltLogin = ctk.CTkButton(master=cadastroFrame, text="Ja tenho uma conta", width=300, fg_color="#2196F3", text_color="black", hover_color="#1565C0",command=voltarLogin)
            BotaoVoltLogin.place(relx=0.5, rely=0.8, anchor=CENTER)

            # MensagemBox de teste
            def salvarUsuario():
                msgBox = messagebox.showinfo(title=None, message="Cadastro concluido com sucesso.")


            # Pega as informacoes digitadas pelo o usuario no campo email/senha em cadastro.
            def salvarCadastro():
                email = emailCadastro.get()
                senha = senhaCadastro.get()
                confeSenha = senha2Cadastro.get()

                # Verifica se a senha é igual a de confirmacao.
                if senha == confeSenha:
                    messagebox.showinfo(title=None, message="Cadastro concluido.")
                    banco.cadastrarUsuarios(email,senha)
                else:
                    messagebox.showerror(title=None, message="As senhas nao conferem.")

            # Botao 'final cadastro' salva no banco as informacoes de cadastro do usuario.
            botaoFinalCadastro = ctk.CTkButton(master=cadastroFrame, text="Finalizar Cadastro", width=300, fg_color="#2196F3", text_color="black", hover_color="#1565C0", command=salvarCadastro)
            botaoFinalCadastro.place(relx=0.5, rely=0.7, anchor=CENTER)
            


        botaoCadastrar = ctk.CTkButton(master=loginFrame, text="Cadastrar", width=300, fg_color="#2196F3", text_color="black", hover_color="#1565C0", command=telaCadastro)
        botaoCadastrar.place(relx=0.5, y=264, anchor=CENTER)

Aplicacao()
