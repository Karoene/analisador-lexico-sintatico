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
        self.listaIdent = []  #lista de identificadores declarados
        

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

        n = len(self.tokens)
        i = 1 
        # Adicionar a lista de identificadores todos os declarados   
        for i in range(n):             
            if (self.tokens[i].valor == 'variavel' and self.tokens[i+1].tipo == 'identificador'):                                 
                self.listaIdent.append(self.tokens[i+1].valor)            
        #print(self.listaIdent)        
        

        try:
            indiceAtual = self.indice
           
            if ( not (self.verificaTipoProximoToken(TIPO_TOKEN['palavra']['inicia']))):
                
                self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha + 1,
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
                #loop para todos os tokens
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

    # INSTRUCAO := Atribuicao | Expressao | Declaracao
    def analisarInstrucao(self):
        #print(str(self.tokenAtual.valor) + ' = val token atual')
        #print(str(self.tokenAtual.tipo) + ' = tip token atual')
        #a = str(self.tokenAtual.valor)
        

        if (self.verificaTipoProximoToken(TIPO_TOKEN['desconhecido'])):
            self.pegarProximoToken()
            self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna-1,
                            'Token desconhecido aqui ' + str(self.tokenAtual.valor)
                        )                        
                    )
        elif (self.verificaTipoProximoToken(TIPO_TOKEN['palavra']['variavel']) 
        or self.tokenAtual.valor == 'variavel'):            
            self.analisarDeclaracao()
            
        elif (self.verificaTipoProximoToken(TIPO_TOKEN['identificador']) or self.tokenAtual.valor == '='):
            if (self.verificaTipoProximoToken(TIPO_TOKEN['atribuicao']['Equal'], 2)):
                #print('ENTROU 1')
                self.analisarAtribuicao()
            elif (self.tokenAtual.valor == '='):
                #print('ENTROU 2')
                self.analisarAtribuicao()    
            else:
                #print(' ENTROU 3')
                self.analisarExpressao()
        else:
            self.pegarProximoToken()
       
        
        #print(str(self.tokenAtual.valor) + ' = val ')
        #print(str(self.tokenAtual.numeroLinha) + ' = linha val')

    
    def analisarDeclaracao(self):
        #aux1 = self.tokenAtual.numeroColuna
        aux2 = self.tokenAtual.numeroLinha
        aux3 = self.tokenAtual.numeroColuna 
        #print(str(self.tokenAtual.valor) + ' = valor atual')
        #print(str(self.tokenAtual.numeroLinha) + ' = linha atual')
       
        if (self.tokenAtual.valor == 'variavel'):
            #self.pegarProximoToken()
            #aux3 = self.tokenAtual.numeroLinha
            #print(aux3 , '= val aux3')
            #self.tokenAtual.tipo == 'identificador')
            if (not (self.verificaTipoProximoToken(TIPO_TOKEN['identificador']))):
                #print(self.verificaTipoProximoToken(TIPO_TOKEN['identificador']))
                #print(' AQUIIII //////////////////////////////////////////')
                self.erros.append(
                    mensagemDeErro(
                    self.tokenAtual.numeroLinha,
                    self.tokenAtual.numeroColuna,
                    #aux2,
                    #aux3,
                    'identificador esperado apos palavra chave1 ' 
                    )                        
                )
        else:
            
            #self.tokenAtual.tipo == 'identificador')
            #print(str(self.tokenAtual.valor)+' = outro')
            aux4 = self.tokenAtual.numeroLinha
            aux5 = self.tokenAtual.numeroColuna
            self.pegarProximoToken()
            #print(str(self.tokenAtual.valor)+' = outro1')
            
            if (not (self.verificaTipoProximoToken(TIPO_TOKEN['identificador']))):
                    self.erros.append(
                        mensagemDeErro(
                        self.tokenAtual.numeroLinha,
                        self.tokenAtual.numeroColuna,
                        #aux4,
                        #aux5,
                        'identificador esperado apos palavra chave2 ' 
                        )                        
                    )
                    if (not (self.verificaTipoProximoToken(TIPO_TOKEN['delimitadores']))):
                        self.erros.append(
                            mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna,
                            #aux4+1,
                            #aux5,                        
                            'esparado delimitador ' 
                            )                        
                    )
        self.pegarProximoToken()
        #print(str(self.tokenAtual.valor)+' = outr2')
        #print(str(self.tokenAtual.numeroLinha) + ' = linha outr2')
       



    # Atribuicao := Identificador "=" Expressao
    def analisarAtribuicao(self):
        if self.verificaTipoProximoToken(TIPO_TOKEN['identificador']):
            self.pegarProximoToken()
            #print(self.tokenAtual.valor + ' /////////////////')
            i = 1
            n = 0
            count = 0
            for i in self.listaIdent:
                if (self.tokenAtual.valor == self.listaIdent[n]):
                    #print(' CONTEM ////////////')
                    count = count + 1
                    break
                
                n = n +1
            if (count == 0):
                self.erros.append(
                        mensagemDeErro(
                            self.tokenAtual.numeroLinha,
                            self.tokenAtual.numeroColuna,
                            'identificador nao declarado = ' + str(self.tokenAtual.valor)
                        )                        
                    )

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

    # Expressao := [ "-" ] Termo { ("+" | "-") Termo }
    def analisarExpressao(self):
        
    
        if self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Menos']):
            self.pegarProximoToken()

        self.analisarTermo()

        while (self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Mais']) or
               self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Menos'])):
            self.pegarProximoToken()
            self.analisarTermo()
      

    # Termo := Fator { ( "*" | "/" | "%" ) Fator }
    def analisarTermo(self):
        self.analisarFator()

        while (
            self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Mult']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Div']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['aritmetico']['Modulo'])
        ):
            self.pegarProximoToken()
            self.analisarFator()

    # Fator := Numero | Identificador | string  | "(" Expressao ")"
    def analisarFator(self):
        if (
            self.verificaTipoProximoToken(TIPO_TOKEN['inteiro']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['decimal']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['string']) or
            self.verificaTipoProximoToken(TIPO_TOKEN['identificador'])
        ):
            if (self.verificaTipoProximoToken(TIPO_TOKEN['identificador'])):
                self.pegarProximoToken()
                #print(self.tokenAtual.valor + ' // AQQQ')
                i = 1
                n = 0
                count = 0
                for i in self.listaIdent:
                    if (self.tokenAtual.valor == self.listaIdent[n]):
                        #print(' CONTEM ////////////')
                        count = count + 1
                        break
                    
                    n = n +1
                if (count == 0):
                    self.erros.append(
                            mensagemDeErro(
                                self.tokenAtual.numeroLinha,
                                self.tokenAtual.numeroColuna,
                                'identificador nao declarado = ' + str(self.tokenAtual.valor)
                            )                        
                        )
                return True
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