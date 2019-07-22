from tipotoken import TIPO_TOKEN
from token import Token

class LeituraFinalizada(Exception):
    def __init__(self):
        pass

def mensagemDeErro(linha, coluna, mensagem):
    '''
        Produz uma mensagem de erro
    '''
    return str(linha) + ':' + str(coluna) + ': ' + mensagem

class AnalisadorSintatico:
    '''
        Verifica se a linguagem condiz com a gramatica que foi
        especificada para ela a partir dos tokens que forem fornecidos,
        informando os erros encontrados
    '''

    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenAtual = Token(TIPO_TOKEN['desconhecido'], None, 0, 0)
        self.erros = []
        self.indice = -1 # Indice do token atual
        

    def pegarProximoToken(self):
        '''
            Atribui o proximo token da lista para o token atual
        '''
        self.indice += 1
        if (self.indice < len(self.tokens)):
            self.tokenAtual = self.tokens[self.indice]
        else:
            raise LeituraFinalizada

    def verificaTipoProximoToken(self, tipo, posicoes=1):
        '''
            Compara o tipo do token atual com o tipo que foi recebido
            como parametro
        
        '''

        if ((self.indice + posicoes) < len(self.tokens)):  
            return self.tokens[self.indice + posicoes].tipo == tipo
        else:
            return False

    def analisarSintaticamente(self):
        '''
            Analisa os tokens e verifica se eles estao corretos com a
            gramatica da linguagem
        '''
        tokenAux = Token(TIPO_TOKEN['palavra'], 'termina', self.tokenAtual.numeroLinha, self.tokenAtual.numeroColuna)
        lista = []
        lista.append(self.tokens[-1])
        

        try:
            indiceAtual = self.indice
           
            if ( not (self.verificaTipoProximoToken(TIPO_TOKEN['palavra']['inicia']))):
                
                self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna,
                            'Inicia = Token esperado ' 
                        )                        
                )
            aux = self.tokens[-1]            
            aux1 = lista[-1]               
            
            if (  (aux1 == aux) and (self.verificaTipoProximoToken(TIPO_TOKEN['palavra']['termina'], 0))):
                    print('')
            else:
                self.erros.append(
                        mensagemDeErro(
                            aux.numeroLinha,
                            aux.numeroColuna,
                            'Termina = Token esperado ' 
                        )  
                    )
                
            while self.indice < (len(self.tokens) - 1):
                self.analisarInstrucao()
                if (self.indice == indiceAtual):
                    self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna,
                            'Token inesperado ' + str(self.tokenAtual.valor)
                        )                        
                    )
                    break
                indiceAtual = self.indice
        except LeituraFinalizada:
            pass

    # Statement := Attribution | Expression | Declaracao
    def analisarInstrucao(self):
        
        if (self.verificaTipoProximoToken(TIPO_TOKEN['palavra']['variavel']) or self.tokenAtual.valor == 'variavel'):            
            self.analisarDeclaracao()
            
        if self.verificaTipoProximoToken(TIPO_TOKEN['identificador']):
            if self.verificaTipoProximoToken(TIPO_TOKEN['atribuicao']['Equal'], 2):
                self.analisarAtribuicao()
            else:
                self.analisarExpressao()
        
        self.pegarProximoToken()
    
    def analisarDeclaracao(self):        
        if (self.tokenAtual.valor == 'variavel'):
            self.pegarProximoToken()
            
            if (not (self.tokenAtual.tipo == 'identificador')):
                self.erros.append(
                    mensagemDeErro(
                    self.tokenAtual.numeroLinha,
                    self.tokenAtual.numeroColuna,
                    'identificador esperado apos palavra chave ' 
                    )                        
                )
        else:
            self.pegarProximoToken() 
            
            self.pegarProximoToken()
            
            if (not (self.tokenAtual.tipo == 'identificador')):
                    self.erros.append(
                        mensagemDeErro(
                        self.tokenAtual.numeroLinha,
                        self.tokenAtual.numeroColuna,
                        'identificador esperado apos palavra chave ' 
                        )                        
                    )
        self.pegarProximoToken()

    # Attribution := Identifier "=" Expression
    def analisarAtribuicao(self):
        if self.verificaTipoProximoToken(TIPO_TOKEN['identificador']):
            self.pegarProximoToken()
            if self.verificaTipoProximoToken(TIPO_TOKEN['atribuicao']['Equal']):
                self.pegarProximoToken()
                self.analisarExpressao()
            else:
                self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna,
                            'Expressão ou atribuição esperada depois de ' + str(self.tokenAtual.valor)
                        )                        
                    )
                return False
        else:
            self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna,
                            'Identificador esperado ' + str(self.tokenAtual.valor)
                        )                        
                    )
            return False
        return True

    # Expression := [ "-" ] Term { ("+" | "-") Term }
    def analisarExpressao(self):
        
    
        if self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Menos']):
            self.pegarProximoToken()

        self.analisarTermo()

        while (self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Mais']) or
               self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Menos'])):
            self.pegarProximoToken()
            self.analisarTermo()
      

    # Term := Factor { ( "*" | "/" | "%" ) Factor }
    def analisarTermo(self):
        self.analisarFator()

        while (
            self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Mult']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Div']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Modulo'])
        ):
            self.pegarProximoToken()
            self.analisarFator()

    # Factor := Number | Identifier | string  | "(" Expression ")"
    def analisarFator(self):
        if (
            self.verificaTipoProximoToken(TIPO_TOKEN['inteiro']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['decimal']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['string']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['identificador'])
        ):
            self.pegarProximoToken()
            return True

        if self.verificaTipoProximoToken(TIPO_TOKEN['delimitadores']['EsquerdaParentese']):
            self.pegarProximoToken()
            self.analisarExpressao()
            if not self.verificaTipoProximoToken(TIPO_TOKEN['delimitadores']['DireitaParenteses']):
                self.erros.append(
                    mensagemDeErro(
                        self.tokenAtual.numeroLinha,
                        self.tokenAtual.numeroColuna,
                        ')' + ' esperado depois de ' + str(self.tokenAtual.valor)
                    )
                )
                return False
                
            self.pegarProximoToken()
            return True

        self.erros.append(
            mensagemDeErro(
                self.tokenAtual.numeroLinha,
                self.tokenAtual.numeroColuna,
                'esperados um numero ou uma expressao entre parenteses depois de ' + str(self.tokenAtual.valor)
            )
        )