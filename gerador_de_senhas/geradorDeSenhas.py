# -*- coding: utf-8 -*-
"""
Created on Sun Aug 03 15:19:42 2014

cria uma senha com quantos caracteres o usuário escolher.
Baseado na tabela ASCII 

@author: denison
"""

import random

#==============================================================================
# gera a tabela ascII
#==============================================================================
def get_tabela():
    asc = []
    for i in range(33, 126):
        asc += chr(i)
    
    return asc
    

#==============================================================================
# obtem a entra do usuario 
#==============================================================================
def prompt():
    tamanho = int(input("Forneca o tamanho da senha desejada: "))
    return tamanho


#==============================================================================
# funçao main
#==============================================================================
def main():
    tabela = get_tabela()
    tam = prompt()
    
    senha = ''
    for x in range(tam):
        senha += tabela[int(random.random() * 94)]
        
    print(u"Sua senha é: " + senha)

    continuar = input("\nDigite 1 para continuar. Outro valor para sair: ")
    if continuar == 1:
        main()

if __name__ == '__main__':
    main()
