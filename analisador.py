from token import *
from tipotoken import *
import re

expressoes = (
    r'^[_a-zA-Z][_a-zA-Z0-9]*', # Identificadores
    r'^(=|\/=|-=|%=|\+=|\*=)',  # Atribuicao
    r'^(\/|%|-|\+|\*)',         # Aritmeticos
    r'^(,|{|}|\[|\]|\(|\)|;)'   # Delimitadores
    r'^[+-]?\d+(\.\d+)?',       # Numeros
    r'^[\"|\'][\w ]+[\"|\']'    # Strings
)

class AnalisadorLexico:
    def __init__(self, conteudoLinha, numeroLinha):
        self.conteudoLinha = conteudoLinha
        self.numeroLinha = numeroLinha
        self.numeroColuna = 0

    def tokenize(self):
        '''
            Transforma o conteudo da linha lida em uma lista de tokens
        '''

        self.numeroColuna = 0
        tokens = []
        token = self.proximoToken()

        while token.tipo != TIPO_TOKEN['EndOfInput']:
            tokens.append(token)
            token = self.proximoToken()

        return tokens

    def proximoToken(self):
        '''
            Retorna o proximo token encontrado a partir da coluna atual
        '''
        if (self.numeroColuna >= len(self.conteudoLinha)):
            return Token(TIPO_TOKEN['EndOfInput'], None, self.numeroLinha, self.numeroColuna)

        # Pega conteudoLinha da coluna atual ate o final
        substr = self.conteudoLinha[self.numeroColuna:] 
        
        # Usa uma expressao regular para capturar os espacos a partir do comeco da substring
        #capturaEspacos = re.match([r'^\S\n\t]+', substr)
        capturaEspacos = re.match(r'[^\S\n\t]+', substr) 


        # Pula a quantidade de colunas referente a quantidade de espacos encontrada
        if (capturaEspacos):
            espacos = capturaEspacos.group(0)
            self.numeroColuna += len(espacos)
            substr = substr[self.numeroColuna:]

        for indice, expressao in enumerate(expressoes):
            capturaLexema = re.match(expressao, substr)
            if (capturaLexema):
                lexema = capturaLexema.group(0)
                token = self.criarToken(lexema, indice)
                self.numeroColuna += len(lexema)
                return token

        self.numeroColuna += 1
        return Token(
            TIPO_TOKEN['Unrecognized'],
            self.conteudoLinha[self.numeroColuna - 1],
            self.numeroLinha,
            self.numeroColuna
        )

    def criarToken(self, lexema, indice):
        '''
            Usa o indice da expressao regular para encontrar o tipo de token apropriado para o lexema
        '''
        if indice == 0: # Indice 0 e o indice da expressao para tokens identificadores
            return Token(TIPO_TOKEN['identificador'], lexema, self.numeroLinha, self.numeroColuna)

        if indice == 1: # Indice da expressao para tokens de atribuicao
            for nomeDoTipo, valorDoTipo in TIPO_TOKEN['atribuicao'].items():
                # Itera os tokens de atribuicao
                if lexema == valorDoTipo: # Se o token de atriubuicao atual for igual ao lexema
                    return Token(TIPO_TOKEN['atribuicao'][nomeDoTipo], lexema, self.numeroLinha, self.numeroColuna)

        if indice == 2: # Indice da expressao para tokens de operacoes aritmeticas
            for nomeDoTipo, valorDoTipo in TIPO_TOKEN['aritmetico'].items(): 
                # Itera os tokens de operacoes aritmeticas
                if lexema == valorDoTipo: 
                    # Se o token de operacao aritmetica for igual ao lexema
                    return Token(TIPO_TOKEN['aritmetico'][nomeDoTipo], lexema, self.numeroLinha, self.numeroColuna)

        if indice == 3: # Indice da  expressao para tokens delimitadores
            for nomeDoTipo, valorDoTipo in TIPO_TOKEN['delimitadores'].items(): # Itera os tokens delimitadores
                if lexema == valorDoTipo: # Se o token delimitador for igual ao lexema
                    return Token(TIPO_TOKEN['delimitadores'][nomeDoTipo], lexema, self.numeroLinha, self.numeroColuna)

        if indice == 4: # Indice da expressao para tokens numerios
            if re.match(r'^\d+$', lexema): # Verifica se eh um inteiro
                return Token(TIPO_TOKEN['inteiro'], lexema, self.numeroLinha, self.numeroColuna)
            else: # Caso nao seja inteiro, eh ponto flutuante
                return Token(TIPO_TOKEN['decimal'], lexema, self.numeroLinha, self.numeroColuna)

        if indice == 5: # Expressao para tokens de strings
            return Token(TIPO_TOKEN['string'], lexema, self.numeroLinha, self.numeroColuna)