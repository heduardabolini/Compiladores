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
    logico = {
        '!': '  not ',
        '&&':'  and   ',
        '||':'  or  '
    }

    while i < len(lista):
        tupla = lista[i]
        # print(tupla)

        if tupla[0] == 'call':
            if tupla[1] == 'scan':
                print(tupla[2])
                entrada = input()  
                execucao[tupla[3]] = entrada
                                              
            elif tupla[1] == 'print':
                if tupla[2] in execucao:
                    print(execucao[tupla[2]], end="")
                else:
                    print(tupla[2], end="")
                
                if tupla[3] != None:
                    if tupla[3] in execucao:
                        print(execucao[tupla[3]])
                    else:
                        print(tupla[3])
                
        if tupla[0] in ['+', '-', '*', '/', '&&', '||', '=', '!', '==', '!=', '<', '<=', '>', '>=']:
            # print(execucao)
            op1 = None
            op2 = None

            if tupla[2] in execucao:
                op1 = execucao[tupla[2]]
            else:
                op1 = tupla[2]
            op1 = str(op1)

            if tupla[3] != None:
                if tupla[3] in execucao:
                    op2 = execucao[tupla[3]]
                else:
                    op2 = tupla[3]
            op2 = str(op2)
           
            if isinstance(op1, bool):
                op1 = str(op1)
                if tupla[3] != None:
                    if isinstance(op2, bool):
                        if tupla[0] in logico:
                            op2 = str(op2)
                            val = eval(op1 + logico[tupla[0]] + op2)
                    else:
                        print("Variável não encontrada")
                        exit()
                else:
                    if tupla[0] in ['!']:
                        val = eval(logico[tupla[0]] + op1)
                    else:
                        print("Operação Inválida")
                        exit() 
                    
                execucao[tupla[1]] = val

            elif isinstance(op1, str) and op1.isnumeric():
                if tupla[3] != None:
                    if isinstance(op2, str) and op2.isnumeric():
                        val = eval(op1 + tupla[0] + op2)
                    else:
                        print("Variável não encontrada")
                        exit()
                else:
                    if tupla[0] in ['+', '-']:
                        val = eval(tupla[0] + op1)
                    else:
                        print("Operação Inválida")
                        exit() 
                    
                execucao[tupla[1]] = val
            else:
                print("Variável não encontradaaa")
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
