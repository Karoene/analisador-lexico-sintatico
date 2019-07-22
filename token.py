class Token:   #representa o objeto token, informacoes de um token
    def __init__(self, tipo, valor, linha, coluna):
        self.tipo = tipo  #tipo do lexema
        self.valor = valor  #lexema (sequencia de caracteres identificavel)
        self.numeroLinha = linha  #linha onde o lexema se localiza dentro do codigo fonte, Usado para mostrar onde esta o erro
        self.numeroColuna = coluna #posicao que ele ta, na linha. Usado para mostrar onde esta o erro
    
    def __str__(self):
        return '<' + self.tipo + ', ' + self.valor + ', ' + str(self.numeroLinha) + ', ' + str(self.numeroColuna) + '>'
