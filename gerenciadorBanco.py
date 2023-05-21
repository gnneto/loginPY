import sqlite3
import bcrypt

# Cria o banco de dados e suas tabelas/colunas iniciais.
def criarBanco():  # save_user

    conexao = sqlite3.connect('gerenciadorBanco.db')
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            senha TEXT
        )
        """)
    conexao.commit()

    cursor.close()
    conexao.close()



# Cadastro de dados do usuario Email/senha
def cadastrarUsuarios(email, senha):
    criarBanco()
    conexao = sqlite3.connect('gerenciadorBanco.db')
    cursor = conexao.cursor()
    
    senhaHash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('INSERT INTO usuarios (email, senha) VALUES (?, ?)', (email, senhaHash))
    conexao.commit()


    cursor.close()
    conexao.close()


def validarLogin(email, senha):
    criarBanco()
    conexao = sqlite3.connect('gerenciadorBanco.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT senha FROM usuarios WHERE email = ?', (email,))
    registro = cursor.fetchone()

    if registro:
        senhaSalva = registro[0]
        if bcrypt.checkpw(senha.encode('utf-8'), senhaSalva):
            return True
        else:
            return False
    else:
        return False

    cursor.close()
    conexao.close()

def validacaoSenhaUsuario(email):
    criarBanco()
    conexao = sqlite3.connect('gerenciadorBanco.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
    registro = cursor.fetchone()

    cursor.close()
    conexao.close()

    if registro:
        return registro[0]
    else:
        return None
    
    cursor.close()
    conexao.close()
