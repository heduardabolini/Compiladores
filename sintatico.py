from enumtokens import *
from main import resultado
import re

tokens = resultado()

####################################### INICIO - FUNCOES PRINCIPAIS ###########################

def function(): #<function*> -> <type> 'IDENT' '(' <argList> ')' <bloco> ;
    type()
    consome(enumtokens.TKN_VARIAVEIS, 'function')
    consome(enumtokens.TKN_ABRE_PARENTESES, 'function')
    arglist()
    consome(enumtokens.TKN_FECHA_PARENTESES, 'function')
    bloco()

def arglist(): #<argList> -> <arg> <restoArgList> | & ;
    if tokens[0][0] == enumtokens.TKN_INT or  tokens[0][0] == enumtokens.TKN_FLOAT:
        arg()
        restoarglist()

def arg(): #<arg> -> <type> 'IDENT' ;
    consome(tokens[0][0], 'arg')
    consome(enumtokens.TKN_VARIAVEIS, 'arg')

def restoarglist(): #<restoArgList> -> ',' <argList> | & ;
    if tokens[0][0] == enumtokens.TKN_VIRGULA:
        consome(tokens[0][0], 'restoarglist')
        arglist()

def type(): #<type> -> 'int' | 'float' ;
    if tokens[0][0] == enumtokens.TKN_INT:
        consome(enumtokens.TKN_INT, 'type')
    elif tokens[0][0] == enumtokens.TKN_FLOAT:
        consome(enumtokens.TKN_FLOAT, 'type')
    else:
        print("Esperado os tokens INT e FLOAT")
        exit()

def bloco(): #<bloco> -> '{' <stmtList> '}' ;
    consome(enumtokens.TKN_ABRE_CHAVES, 'bloco')
    stmtList()
    consome(enumtokens.TKN_FECHA_CHAVES, 'bloco')
   
def stmtList(): #stmtList> -> <stmt> <stmtList> | & ;
    array_tokens = [
        enumtokens.TKN_FOR,
        enumtokens.TKN_PRINT,
        enumtokens.TKN_SCAN,
        enumtokens.TKN_WHILE,
        enumtokens.TKN_VARIAVEIS,
        enumtokens.TKN_IF,
        enumtokens.TKN_ABRE_CHAVES,
        enumtokens.TKN_BREAK,
        enumtokens.TKN_CONTINUE,
        enumtokens.TKN_INT,
        enumtokens.TKN_FLOAT,
        enumtokens.TKN_RETURN,
        enumtokens.TKN_PONTO_VIRGULA,
        enumtokens.TKN_NEGACAO,
        enumtokens.TKN_ADICAO,
        enumtokens.TKN_SUBTRACAO,
        enumtokens.TKN_ABRE_PARENTESES,
        enumtokens.TKN_NUMEROS_FLOAT,
        enumtokens.TKN_NUMEROS_INT
    ]
    
    if tokens:
        if tokens[0][0] in array_tokens: #ERRO AQUI
            stmt()
            stmtList()
    # else:
    #     print("Não possui correspondente para", tokens[0][1])
    #     exit()

def stmt(): #<stmt> -> <forStmt> | <ioStmt> | <whileStmt> | <expr> ';' | <ifStmt> | <bloco> | 'break'';'| 'continue'';'| <declaration> | 'return' <fator> ';'| ';' ;
    if tokens[0][0] == enumtokens.TKN_FOR:
       forStmt()
    elif tokens[0][0] == enumtokens.TKN_PRINT or tokens[0][0] == enumtokens.TKN_SCAN:
        ioStmt()
    elif tokens[0][0] == enumtokens.TKN_WHILE:
        whileStmt()
    elif tokens[0][0] in [enumtokens.TKN_VARIAVEIS, enumtokens.TKN_NEGACAO, enumtokens.TKN_ADICAO, enumtokens.TKN_SUBTRACAO, enumtokens.TKN_ABRE_PARENTESES, enumtokens.TKN_NUMEROS_FLOAT, enumtokens.TKN_NUMEROS_INT ]: #EXPRESSAO
        expr()
        consome(enumtokens.TKN_PONTO_VIRGULA, 'stmt1') 
    elif tokens[0][0] == enumtokens.TKN_IF:
        ifStmt()
    elif tokens[0][0] == enumtokens.TKN_ABRE_CHAVES:
        bloco()
    elif tokens[0][0] == enumtokens.TKN_BREAK:
        consome(enumtokens.TKN_BREAK, 'stmt2')
        consome(enumtokens.TKN_PONTO_VIRGULA, 'stmt3')      
    elif tokens[0][0] == enumtokens.TKN_CONTINUE:
        consome(enumtokens.TKN_CONTINUE, 'stmt4')
        consome(enumtokens.TKN_PONTO_VIRGULA, 'stmt5')
    elif tokens[0][0] == enumtokens.TKN_INT or tokens[0][0] == enumtokens.TKN_FLOAT:
        declaration()
    elif tokens[0][0] == enumtokens.TKN_RETURN:
        consome(enumtokens.TKN_RETURN, 'stmt6')
        fator()
        consome(enumtokens.TKN_PONTO_VIRGULA, 'stmt7')
    elif tokens[0][0] == enumtokens.TKN_PONTO_VIRGULA:
        consome(enumtokens.TKN_PONTO_VIRGULA, 'stmt8')

####################################### FIM - FUNCOES PRINCIPAIS ###########################


####################################### INICIO - DESCRICAO DOS STMT ###########################

def declaration(): #<declaration> -> <type> <identList> ';' ;
    type()
    identList()
    consome(enumtokens.TKN_PONTO_VIRGULA, 'declaration')

def identList(): #<identList> -> 'IDENT' <restoIdentList> ;
    consome(enumtokens.TKN_VARIAVEIS, 'identlist')
    restoIdentList()

def restoIdentList(): #<restoIdentList> -> ',' 'IDENT' <restoIdentList> | & ;
    if tokens[0][0] == enumtokens.TKN_VIRGULA:
        consome(enumtokens.TKN_VIRGULA, 'restoidentlist')
        consome(enumtokens.TKN_VARIAVEIS, 'restoidentlist')
        restoIdentList()
        
def forStmt(): #'for' '(' <optExpr> ';' <optExpr> ';' <optExpr> ')' <stmt> ;
    consome(enumtokens.TKN_FOR, '1')
    consome(enumtokens.TKN_ABRE_PARENTESES,'2')
    optExpr()
    consome(enumtokens.TKN_PONTO_VIRGULA, '3')
    optExpr()
    consome(enumtokens.TKN_PONTO_VIRGULA, '4')
    optExpr()
    consome(enumtokens.TKN_FECHA_PARENTESES, '5')
    stmt()

def optExpr(): #<optExpr> -> <expr> | & ;
    if tokens[0][0] in [enumtokens.TKN_VARIAVEIS, enumtokens.TKN_NEGACAO, enumtokens.TKN_ADICAO, enumtokens.TKN_SUBTRACAO, enumtokens.TKN_ABRE_PARENTESES, enumtokens.TKN_NUMEROS_FLOAT, enumtokens.TKN_NUMEROS_INT ]: #EXPRESSAO
        expr()
         
def ioStmt(): #<ioStmt> -> 'scan' '(' 'STR' ',' 'IDENT' ')' ';' 'print' '(' <outList> ')' ';' ;
    if tokens[0][0] == enumtokens.TKN_SCAN:
        consome(enumtokens.TKN_SCAN, 'iostmt')
        consome(enumtokens.TKN_ABRE_PARENTESES, 'iostmt')
        consome(enumtokens.TKN_STRING, 'iostmt')
        consome(enumtokens.TKN_VIRGULA, 'iostmt')
        consome(enumtokens.TKN_VARIAVEIS, 'iostmt')
        consome(enumtokens.TKN_FECHA_PARENTESES, 'iostmt')
        consome(enumtokens.TKN_PONTO_VIRGULA, 'iostmt')
    else:
        consome(enumtokens.TKN_PRINT, 'iostmt')
        consome(enumtokens.TKN_ABRE_PARENTESES, 'iostmt')
        outList()
        consome(enumtokens.TKN_FECHA_PARENTESES, 'iostmt')
        consome(enumtokens.TKN_PONTO_VIRGULA, 'iostmt')

def outList(): #<outList> -> <out> <restoOutList> ; 
    out()
    restoOutList()

def out(): #<out> -> 'STR' | 'IDENT' | 'NUMint' | 'NUMfloat' ;
    if tokens[0][0] == enumtokens.TKN_STRING:
        consome(enumtokens.TKN_STRING, 'out')
    elif tokens[0][0] == enumtokens.TKN_VARIAVEIS:
        consome(enumtokens.TKN_VARIAVEIS, 'out') 
    elif tokens[0][0] == enumtokens.TKN_NUMEROS_INT:
        consome(enumtokens.TKN_NUMEROS_INT, 'out') 
    elif tokens[0][0] == enumtokens.TKN_NUMEROS_FLOAT:
        consome(enumtokens.TKN_NUMEROS_FLOAT, 'out') 

def restoOutList(): #<restoOutList> -> ',' <out> <restoOutList> | & ;
    if tokens[0][0] == enumtokens.TKN_VIRGULA:
        consome(enumtokens.TKN_VIRGULA, 'out')
        out()
        restoOutList() 

def whileStmt(): #<whileStmt> -> 'while' '(' <expr> ')' <stmt> ;
    consome(enumtokens.TKN_WHILE, 'whilestmt')
    consome(enumtokens.TKN_ABRE_PARENTESES, 'whilestmt')
    expr()
    consome(enumtokens.TKN_FECHA_PARENTESES, 'whilestmt')
    stmt()

def ifStmt(): #<ifStmt> -> 'if' '(' <expr> ')' <stmt> <elsePart> ;
    consome(enumtokens.TKN_IF, 'ifstmt')
    consome(enumtokens.TKN_ABRE_PARENTESES, 'ifstmt')
    expr()
    consome(enumtokens.TKN_FECHA_PARENTESES, 'ifstmt')
    stmt()
    elsePart()

def elsePart(): #<elsePart> -> 'else' <stmt> | & ;
    if tokens[0][0] == enumtokens.TKN_ELSE:
        consome(enumtokens.TKN_ELSE, 'elsepart')
        stmt() 

####################################### FIM - DESCRICAO DOS STMT ####################################

####################################### INICIO - EXPRESSOES #########################################

def expr(): #<expr> -> <atrib> ;
    atrib()

def atrib(): #<atrib> -> <or> <restoAtrib> ;
    functionOr()
    restoAtrib()

def restoAtrib(): #<restoAtrib> -> '=' <atrib> | & ;
    if tokens[0][0] == enumtokens.TKN_ATRIBUICAO:
        consome(enumtokens.TKN_ATRIBUICAO, 'restoatrib')
        atrib()

def functionOr(): #<or> -> <and> <restoOr> ;
    functionAnd()
    restoOr()

def restoOr(): #<restoOr> -> '||' <and> <restoOr> | & ;
    if tokens[0][0] == enumtokens.TKN_LOGICO_OU:
        consome(enumtokens.TKN_LOGICO_OU, 'restoor')
        functionAnd()
        restoOr()

def functionAnd(): #<and> -> <not> <restoAnd> ;
    functionNot()
    restoAnd()

def restoAnd(): #<restoAnd> -> '&&' <not> <restoAnd> | & ;
    if tokens[0][0] == enumtokens.TKN_LOGICO_AND:
        consome(enumtokens.TKN_LOGICO_AND, 'restoand')
        functionNot()
        restoAnd()

def functionNot(): #<not> -> '!' <not> | <rel> ; 
    if tokens[0][0] == enumtokens.TKN_NEGACAO:
        consome(enumtokens.TKN_NEGACAO, 'functionnot')
        functionNot()
    else:
        rel()

def rel(): #<rel> -> <add> <restoRel> ; 
    add()
    restoRel()

def restoRel(): #<restoRel> -> '==' <add> | '!=' <add> '<' <add> | '<=' <add> '>' <add> | '>=' <add> | & ;
    if tokens[0][0] == enumtokens.TKN_IGUALDADE:
        consome(enumtokens.TKN_IGUALDADE, 'restorel')
        add()
    elif tokens[0][0] == enumtokens.TKN_DIFERENCA:
        consome(enumtokens.TKN_DIFERENCA, 'restorel')
        add()
    elif tokens[0][0] == enumtokens.TKN_MENOR:
        consome(enumtokens.TKN_MENOR, 'restorel')
        add()
    elif tokens[0][0] == enumtokens.TKN_MENOR_IGUAL:
        consome(enumtokens.TKN_MENOR_IGUAL, 'restorel')
        add()
    elif tokens[0][0] == enumtokens.TKN_MAIOR:
        consome(enumtokens.TKN_MAIOR, 'restorel')
        add()
    elif tokens[0][0] == enumtokens.TKN_MAIOR_IGUAL:
        consome(enumtokens.TKN_MAIOR_IGUAL, 'restorel')
        add()
    
def add(): #<add> -> <mult> <restoAdd> ;
    mult()
    restoAdd()

def restoAdd(): #<restoAdd> -> '+' <mult> <restoAdd> | '-' <mult> <restoAdd> | & ;
    if tokens[0][0] == enumtokens.TKN_ADICAO:
        consome(enumtokens.TKN_ADICAO, 'restoadd')
        mult()
        restoAdd()
    elif tokens[0][0] == enumtokens.TKN_SUBTRACAO:
        consome(enumtokens.TKN_SUBTRACAO, 'restoadd')
        mult()
        restoAdd()

def mult(): #<mult> -> <uno> <restoMult> ;
    uno()
    restoMult()

def restoMult(): #<restoMult> -> '*' <uno> <restoMult> |  '/' <uno> <restoMult> |  '%' <uno> <restoMult> | & ;
    if tokens[0][0] == enumtokens.TKN_MULTIPLICACAO:
        consome(enumtokens.TKN_MULTIPLICACAO, 'restomult')
        uno()
        restoMult()
    elif tokens[0][0] == enumtokens.TKN_DIVISAO:
        consome(enumtokens.TKN_DIVISAO, 'restomult')
        uno()
        restoMult()
    elif tokens[0][0] == enumtokens.TKN_MODULO:
        consome(enumtokens.TKN_MODULO, 'restomult')
        uno()
        restoMult()

def uno(): #'+' <uno> | '-' <uno> | <fator> ;
    if tokens[0][0] == enumtokens.TKN_ADICAO:
        consome(enumtokens.TKN_ADICAO, 'uno')
        uno()
    elif tokens[0][0] == enumtokens.TKN_SUBTRACAO:
        consome(enumtokens.TKN_SUBTRACAO, 'uno')
        uno()
    else:
        fator()

def fator(): #fator> -> 'NUMint' | 'NUMfloat' | 'IDENT'  | '(' <atrib> ')' ;
    if tokens[0][0] == enumtokens.TKN_NUMEROS_INT:
        consome(enumtokens.TKN_NUMEROS_INT, 'fator')
    elif tokens[0][0] == enumtokens.TKN_NUMEROS_FLOAT:
        consome(enumtokens.TKN_NUMEROS_FLOAT, 'fator')
    elif tokens[0][0] == enumtokens.TKN_VARIAVEIS:
        consome(enumtokens.TKN_VARIAVEIS, 'fator')
    elif tokens[0][0] == enumtokens.TKN_ABRE_PARENTESES:
        consome(enumtokens.TKN_ABRE_PARENTESES, 'fator')
        atrib()
        consome(enumtokens.TKN_FECHA_PARENTESES, 'fator')
    else:
        encontrado = descobretoken(tokens[0][0])
        print(f"Esperado varivel, numero ou expressao e foi encontrado o token {encontrado}")
        exit()
        
####################################### FIM - EXPRESSOES ############################################


def consome(tkn_esperado, func=''):
    esperado = descobretoken(tkn_esperado)
    if not tokens:
        print(f"Esperado o token {esperado} e não foi encontrado mais tokens")
        exit() 
    elif tokens[0][0] == tkn_esperado:
        tokens.pop(0)
    else:
        encontrado = descobretoken(tokens[0][0])
        print(f"Esperado o token {esperado} e foi encontrado o token {encontrado} - Linha {tokens[0][2]} - Coluna {tokens[0][3]} - Funcao {func} - Lexema {tokens[0][1]}")
        exit()
    
def descobretoken(token):
    if token == 1:
        tipo = 'TKN_ADICAO'
    elif token == 2:
        tipo = 'TKN_SUBTRACAO'
    elif token == 3:
        tipo = 'TKN_MULTIPLICACAO'
    elif token == 4:
       tipo = 'TKN_DIVISAO'
    elif token == 5:
       tipo = 'TKN_MODULO'
    elif token == 6:
       tipo = 'TKN_LOGICO_OU'
    elif token == 7:
       tipo = 'TKN_LOGICO_AND'
    elif token == 8:
       tipo = 'TKN_NEGACAO'
    elif token == 9:
       tipo = 'TKN_IGUALDADE'
    elif token == 10:
       tipo = 'TKN_DIFERENCA'
    elif token == 11:
       tipo = 'TKN_MAIOR'
    elif token == 12:
       tipo = 'TKN_MENOR'
    elif token == 13:
        tipo = 'TKN_MAIOR_IGUAL'
    elif token == 14:
        tipo = 'TKN_MENOR_IGUAL'
    elif token == 15:
        tipo = 'TKN_ATRIBUICAO'
    elif token == 16:
        tipo = 'TKN_INT'
    elif token == 17:
        tipo = 'TKN_FLOAT'
    elif token == 18:
        tipo = 'TKN_FOR'
    elif token == 19:
        tipo = 'TKN_WHILE'
    elif token == 20:
        tipo = 'TKN_BREAK'
    elif token == 21:
        tipo = 'TKN_CONTINUE'
    elif token == 22:
        tipo = 'TKN_IF'
    elif token == 23:
        tipo = 'TKN_ELSE'
    elif token == 24:
        tipo = 'TKN_PRINT'
    elif token == 25:
        tipo = 'TKN_SCAN'
    elif token == 26:
        tipo = 'TKN_RETURN'
    elif token == 27:
        tipo = 'TKN_PONTO_VIRGULA'
    elif token == 28:
        tipo = 'TKN_VIRGULA'
    elif token == 29:
        tipo = 'TKN_ABRE_CHAVES'
    elif token == 30:
        tipo = 'TKN_FECHA_CHAVES'
    elif token == 31:
        tipo = 'TKN_ABRE_PARENTESES'
    elif token == 32:
        tipo = 'TKN_FECHA_PARENTESES'
    elif token == 33:
        tipo = 'TKN_STRING'
    elif token == 34:
        tipo = 'TKN_NUMEROS_INT'
    elif token == 35:
        tipo = 'TKN_NUMEROS_FLOAT'
    elif token == 36:
        tipo = 'TKN_VARIAVEIS'

    return tipo

function()