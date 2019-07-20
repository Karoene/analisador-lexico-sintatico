from analisador import AnalisadorLexico
#import { Parser } from './parser'
'''
AINDA PRECISO FAZER A LEITURA DO ARQUIVO
'''
source = 'z=((x+y)-((x+y)/(x-y)))+((x+y)/(x-y))"kakakak"'
source1 = 'k = esfes'
source2 = ''
lines = source.split('\n') # separa as linhas da entrada do codigo fonte, caso aja mais de uma linha no source
print(lines)
tokens = []   #lista de todos os tokens do codigo fonte

for indice,linha in enumerate(lines):
    lexer = AnalisadorLexico(linha, indice+1 )  #nova instancia, passando conteudo da linha lida, e numero da linha 
    #print(lexer)
    curTokens = lexer.tokenize()  #pega a lista com todos os tokens da linha lida
    #print(curTokens)
    
    if linha:  #se a linha atual nao for vazia
        #for (let j = 0; j < curTokens.length; ++j) //percorre todos os tokens da linha atual
        for token in curTokens:
            tokens.append(token); #insere na lista geral de tokens os tokens dessa linha

for token in tokens:
  print(token)