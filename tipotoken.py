# -*- coding: utf-8 -*-
TIPO_TOKEN = {  #dicionario com os token que minha linguagem aceita 
    "palavra": {
        "variavel": 'variavel',
        "inicia": 'inicia',
        "termina": 'termina',
   },
    
    "atribuicao": {   #grupo (atribuição)        
        "Equal": '=',  #atribuicao        
    }, 

    "aritmetico": {  #aritimetico
        "Div": '/',
        "Modulo": '%',
        "Menos": '-',
        "Mais": "+",
        "Mult": "*",
    },
        
    "delimitadores": {  #delimitadores        
        "EsquerdaColchete": '[',
        "EsquerdaParentese": "(",    
        "DireitaColchete": ']',
        "DireitaParenteses": ')',                 
    },    
    
    "identificador": 'identificador', #identificadores = nomes de variavel
    "inteiro": 'integer',  #valor explicito (chamado de literal)
    "decimal": 'decimal',  #valor decimal explicito
    "string": 'stringLiteral',  #string entre aspas

    
    "fimdaentrada": 'fimdaentrada',  #fim da entrada de leilura, fim do arquivo lido
    "desconhecido": 'desconhecido'  #para um lexema nao reconhecido, sem tipo definido
}
