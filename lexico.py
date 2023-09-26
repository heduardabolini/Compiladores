from enumtokens import *
import re

#função para ler o arquivo em uma lista
def lerArq():
    arq = open("prog6.c", "r")
    linhas = arq.readlines() 
    arq.close()
    return linhas

#função para separar os tokens
def separarToken(linhas):
    linhas_comentarios_barra = re.sub(r'//.*', '', ''.join(linhas)) #retirar comentários em barra
    regex = r'"[^"]+"|(-?\d+\.\d+)|(-?\d+)|\b\w+\b|(\|\||&&|<=|>=|==|\n|.)'#regex para separar os tokens
    #r'"[^"]+"|(-?\d+\.\d+)|(-?\d+)|\b\w+\b|.' 
    tokens = []

    for match in re.finditer(regex, linhas_comentarios_barra, re.DOTALL): #encontrando as correspondências da expressão regular
        for i in match.groups():
            if i is not None: #encontrando token
                tokens.append(i)
                break
        else:
            tokens.append(match.group(0))

    return tokens

#função para transformar comentários em bloco /**/ em comentários em barra //
def transformarComentario(linhas):
    codigo_transformado = []
    comentario = False

    for linha in linhas:
        if '/*' in linha and '*/' in linha: #comentario em bloco com uma linha 
            linha_transformada = linha.replace("/*", "//").replace("*/", "")
            codigo_transformado.append(linha_transformada)

        elif '/*' in linha: #comentario começando com /*
            comentario = True
            linha_transformada = linha.replace("/*", "//")
            codigo_transformado.append(linha_transformada)

        elif comentario and '*/' in linha: #encerrando bloco de comentario */
            comentario = False
            linha_transformada = linha.replace("*/", "")
            linha_transformada = '//' + linha_transformada
            codigo_transformado.append(linha_transformada)

        elif comentario: #dentro do comentario em bloco, transformando as linhas em //
            codigo_transformado.append("\n//" + linha.strip())  
            
        else: #fora do comentatio em bloco
            codigo_transformado.append(linha)

    return codigo_transformado

#função do analisador léxico
def lexico(token):
    tokens = []
    linha = 1  
    coluna = 1
    
    #retirando palavras reservadas da linguagem mini c e números
    palavras_reservadas = ["int", "float", "for", "while", "break", "continue", "if", "else", "print", "scan", "return"]
    padrao = r'\b(?!(?:' + '|'.join(re.escape(palavra) for palavra in palavras_reservadas) + r'|"\w+))\b(?![-+]?\d+\b)\w+\b'    

    #analisando cada linha token
    for i in token:
     
        if i == '+':
            tokens.append((enumtokens.TKN_ADICAO, i, linha, coluna))
            coluna +=len(i)

        elif i == '-':
            tokens.append((enumtokens.TKN_SUBTRACAO, i, linha, coluna))
            coluna +=len(i)

        elif i == '*':
            tokens.append((enumtokens.TKN_MULTIPLICACAO, i, linha, coluna))
            coluna +=len(i)

        elif i == '/':
            tokens.append((enumtokens.TKN_DIVISAO, i, linha, coluna))
            coluna +=len(i)

        elif i == '%':
            tokens.append((enumtokens.TKN_MODULO, i, linha, coluna))
            coluna +=len(i)

        elif i == '||':
            tokens.append((enumtokens.TKN_LOGICO_OU, i, linha, coluna))
            coluna +=len(i)
        
        elif i == '&&':
            tokens.append((enumtokens.TKN_LOGICO_AND, i, linha, coluna))
            coluna +=len(i)
            
        elif i == '!':
            tokens.append((enumtokens.TKN_NEGACAO, i, linha, coluna))
            coluna +=len(i)
            
        elif i == '==':
            tokens.append((enumtokens.TKN_IGUALDADE, i, linha, coluna))
            coluna +=len(i)

        elif i == '!=':
            tokens.append((enumtokens.TKN_DIFERENCA, i, linha, coluna))
            coluna +=len(i)
        
        elif i == '>':
            tokens.append((enumtokens.TKN_MAIOR, i, linha, coluna))
            coluna +=len(i)

        elif i == '<':
            tokens.append((enumtokens.TKN_MENOR, i, linha, coluna))
            coluna +=len(i)

        elif i == '>=':
            tokens.append((enumtokens.TKN_MAIOR_IGUAL, i, linha, coluna))
            coluna +=len(i)

        elif i == '<=':
            tokens.append((enumtokens.TKN_MENOR_IGUAL, i, linha, coluna))
            coluna +=len(i)

        elif i == '=':
            tokens.append((enumtokens.TKN_ATRIBUICAO, i, linha, coluna))
            coluna +=len(i)

        elif i == 'int':
            tokens.append((enumtokens.TKN_INT, i, linha, coluna))
            coluna +=len(i)

        elif i == 'float':
            tokens.append((enumtokens.TKN_FLOAT, i, linha, coluna))
            coluna +=len(i)

        elif i == 'for':
            tokens.append((enumtokens.TKN_FOR, i, linha, coluna))
            coluna +=len(i)

        elif i == 'while':
            tokens.append((enumtokens.TKN_WHILE, i, linha, coluna))
            coluna +=len(i)

        elif i == 'break':
            tokens.append((enumtokens.TKN_BREAK, i, linha, coluna))
            coluna +=len(i)

        elif i == 'continue':
            tokens.append((enumtokens.TKN_CONTINUE, i, linha, coluna))
            coluna +=len(i)

        elif i == 'if':
            tokens.append((enumtokens.TKN_IF, i, linha, coluna))
            coluna +=len(i)

        elif i == 'else':
            tokens.append((enumtokens.TKN_ELSE, i, linha, coluna))
            coluna +=len(i)

        elif i == 'print':
            tokens.append((enumtokens.TKN_PRINT, i, linha, coluna))
            coluna +=len(i)

        elif i == 'scan':
            tokens.append((enumtokens.TKN_SCAN, i, linha, coluna))
            coluna +=len(i)

        elif i == 'return':
            tokens.append((enumtokens.TKN_RETURN, i, linha, coluna))
            coluna +=len(i)
        
        elif i == ';':
            tokens.append((enumtokens.TKN_PONTO_VIRGULA, i, linha, coluna))
            coluna +=len(i)

        elif i == ',':
            tokens.append((enumtokens.TKN_VIRGULA, i, linha, coluna))
            coluna +=len(i)

        elif i == '{':
            tokens.append((enumtokens.TKN_ABRE_CHAVES, i, linha, coluna))
            coluna +=len(i)

        elif i == '}':
            tokens.append((enumtokens.TKN_FECHA_CHAVES, i, linha, coluna))
            coluna +=len(i)

        elif i == '(':
            tokens.append((enumtokens.TKN_ABRE_PARENTESES, i, linha, coluna))
            coluna +=len(i)
        
        elif i == ')':
            tokens.append((enumtokens.TKN_FECHA_PARENTESES, i, linha, coluna))
            coluna +=len(i)

        #verificando se é string com a ocorrência ""
        elif re.match(r'"([^"]*)"',i):
            tokens.append((enumtokens.TKN_STRING, i, linha, coluna))
            coluna +=len(i)
        
        #verificando se é número 
        # if re.match(r'-?\d+(?:\.\d+)?',i):
        #     tokens.append((enumtokens.TKN_NUMEROS, i, linha, coluna))
        #     coluna +=len(i)

        #verificando se é inteiro
        elif re.match(r'-?\d+$',i):
            tokens.append((enumtokens.TKN_NUMEROS_INT, i, linha, coluna))
            coluna +=len(i)

        #verificando se é float
        elif re.match(r'-?\d+\.\d+',i):
            tokens.append((enumtokens.TKN_NUMEROS_FLOAT, i, linha, coluna))
            coluna +=len(i)
        
        #verificando se é variável, excluindo as strings com aspas duplas
        variaveis_encontradas = re.findall(padrao, i)
        for variavel in variaveis_encontradas:
            if i == variavel and i != '"':
                tokens.append((enumtokens.TKN_VARIAVEIS, i, linha, coluna))
                coluna +=len(i)

        #espaço em branco '', soma 1 na coluna            
        if re.match(r'\s+', i): 
            coluna +=len(i)

        #tabulacao \t, soma 4 na coluna 
        if re.match(r'\t', i):
            if coluna == 2:
                coluna = 4
            else:
                coluna +=4

        #quebra de linha, soma na linha e reseta a coluna
        if i == '\n':
            linha += 1
            coluna = 1

    return tokens

# # ler arquivo e transforma os comentários em bloco, em comentários em barra
# linhas = lerArq()
# comentario = transformarComentario(linhas)
# for linha in comentario:
#     print(linha)

# #separa os tokens para analise
# tokens = separarToken(comentario)
# print(tokens)
# print("\n")

# #analisador lexico, com retorno de (tipo, token, linha, coluna)
# lexicos = lexico(tokens)
# for token in lexicos:
#     print(token)

def resultado():
    linhas = lerArq()
    comentario = transformarComentario(linhas)
    tokens = separarToken(comentario)
    lexicos = lexico(tokens)

    return lexicos
