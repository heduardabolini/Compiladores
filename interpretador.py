from teste1 import *

#lista de label (guardo a posicao da linha)
def guardarPosicao(exemplo):
    index = {}
    operadores = {}

    for i, item in enumerate(exemplo):
        index[item] = i

    for key, value in index.items():
        if 'label' in key:
            label = key[1]
            operadores[label] = value

    return operadores

#controle de variaveis (lista ou tuplas olhar pela operacao)
def listaExecucao(lista, posicao):
    execucao = {}
    i = 0

    while i < len(lista):
        tupla = lista[i]

        if tupla[0] == 'call':
            if tupla[1] == 'scan':
                print(tupla[2])
                entrada = input()  
                execucao[tupla[3]] = entrada
                                              
            elif tupla[1] == 'print':
                if tupla[2] in execucao:
                    print(execucao[tupla[2]])
                else:
                    print(tupla[2])
                
        if tupla[0] in ['+', '-', '*', '/', '&&', '||', '=', '!', '==', '!=', '<', '<=', '>', '>=']:
            if tupla[2] in execucao:
                op1 = execucao[tupla[2]]
            else:
                op1 = tupla[2]

            if tupla[3] != None:
                if tupla[3] in execucao:
                    op2 = execucao[tupla[3]]
                else:
                    op2 = tupla[3]

            if op1.isnumeric() and op2.isnumeric():
                if tupla[3] != None:
                    val = eval(op1 + tupla[0] + op2)
                else:
                    val = eval(tupla[0] + op1)
                    
                execucao[tupla[1]] = val
            else:
                print("Variável não encontrada")
                exit()
        
        if tupla[0] == 'if':
            if tupla[1] in execucao:
                condicao = execucao[tupla[1]]
                if condicao:
                    label_pos = posicao[tupla[2]] 
                    i = label_pos
                else:
                    label_pos = posicao[tupla[3]]
                    i = label_pos  

        if tupla[0] == 'jump':
            label_pos = posicao[tupla[1]]
            i = label_pos 

        i += 1 

    return execucao

exemplo = programa()
posicao = guardarPosicao(exemplo)
print(posicao)

execucao = listaExecucao(exemplo, posicao)
print(execucao)
