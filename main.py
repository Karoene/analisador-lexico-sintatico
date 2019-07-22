from analisador import AnalisadorLexico
from analisadorS import AnalisadorSintatico


arq = open('./test.txt', 'r')
#arq = open('./test2.txt', 'r')
#arq = open('./test3.txt', 'r')
texto = arq.readlines()
tokens = []

for indice,linha in enumerate(texto):    
    linha = linha.replace('\n', '')
    if (linha):
      aux = len(linha) -1
      ind = linha[aux]      
      if (ind == ' '):
        linha = linha[:aux]
      
    lexer = AnalisadorLexico(linha, indice+1 )  #nova instancia, passando conteudo da linha lida, e numero da linha 
       
    atualTokens = lexer.tokenize()  #pega a lista com todos os tokens da linha lida
  
    if linha:  #se a linha atual nao for vazia        
        for token in atualTokens:            
          tokens.append(token) #insere na lista geral de tokens os tokens dessa linha

for token in tokens:
  print(token)

parser = AnalisadorSintatico(tokens)
parser.analisarSintaticamente()
print(parser.erros)