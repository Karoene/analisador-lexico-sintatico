from analisador import AnalisadorLexico
from analisadorS import AnalisadorSintatico

'''TESTES NAO ACEITOS'''
arq = open('./test.txt', 'r')
#arq = open('./test2.txt', 'r')
#arq = open('./test3.txt', 'r')
#arq = open('./test4.txt', 'r')

'''TESTES ACEITOS'''
#arq = open('./test1AC.txt', 'r')
#arq = open('./test2AC.txt', 'r')
#arq = open('./test3AC.txt', 'r')
#arq = open('./test4AC.txt', 'r')
#################################
texto = arq.readlines()
tokens = []

for indice,linha in enumerate(texto):    
    linha = linha.replace('\n', '')
    #print(linha + '= val linha')
    if (linha):
      aux = len(linha) -1
      ind = linha[aux] 
      #print(ind + ':valor de ind')
      
      if (ind == (' ' or '  ' or '   ' or '    ')):
        linha = linha[:aux]
      
      lexer = AnalisadorLexico(linha, indice+1 )  #nova instancia, passando conteudo da linha lida, e numero da linha 
      atualTokens = lexer.tokenize()  #pega a lista com todos os tokens da linha lida
  
      for token in atualTokens:            
        tokens.append(token) #insere na lista geral de tokens os tokens dessa linha

for token in tokens:
  print(token)

parser = AnalisadorSintatico(tokens)
parser.analisarSintaticamente()
print(parser.erros)
