from lexico import *
from sintatico import *
import sys

def lerArq(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arq:
            linhas = arq.readlines()
        return linhas
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        sys.exit(1)

def resultado():
    nome_arquivo = sys.argv[1]
    linhas = lerArq(nome_arquivo)
    comentario = transformarComentario(linhas)
    tokens = separarToken(comentario)
    lexicos = lexico(tokens)
    return lexicos

