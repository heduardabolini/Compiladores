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
    i = 0  #posição atual na lista
    valida = False

    while i < len(lista):
        tupla = lista[i]

        if tupla[0] == 'call':
            if tupla[1] == 'scan':
                print(tupla[2])
                entrada = input()  
                execucao[tupla[3]] = entrada
               
                for elemento in execucao:
                    if elemento == tupla[3]:
                        execucao[elemento] = entrada                                     
            elif tupla[1] == 'print':
                print(tupla[2])
                
        if tupla[0] in ['+', '-', '*', '/', '&&', '||', '=', '!', '==', '!=', '<', '<=', '>', '>=']:
            for elemento in execucao:
                if elemento == tupla[2]: #Duvida -> se a variavel nao existir?
                    val = list(execucao.values())[0] + tupla[0] + tupla[3]
                    valida = True  
            if valida == False:
                print("Variável não encontrada")
                exit()
            execucao[tupla[1]] = val 

        if tupla[0] == 'if':
            for elemento in execucao:
                if elemento == tupla[1]:
                    condicao = eval(execucao[tupla[1]])
                    if condicao:
                        label_pos = posicao[tupla[2]] 
                        #print(label_pos)
                        i = label_pos
                    else:
                        label_pos = posicao[tupla[3]]
                        #print(label_pos)
                        i = label_pos  
        
        if tupla[0] == 'jump':
            label_pos = posicao[tupla[1]]
            #print(label_pos)
            i = label_pos 

        i += 1 

    return execucao

exemplo = programa()
posicao = guardarPosicao(exemplo)
print(posicao)

execucao = listaExecucao(exemplo, posicao)
print(execucao)
