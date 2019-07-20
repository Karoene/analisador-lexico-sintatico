# -*- coding: utf-8 -*-
TIPO_TOKEN = {  #dicionario com os token que minha linguagem aceita 
    "atribuicao": {   #grupo (atribuição)
        "DivEqual": '/=',  #tipos de tokens
        "Equal": '=',  #atribuicao
        "MinusEqual": '-=',
        "ModuloEqual": '%=',
        "PlusEqual": '+=',
        "TimesEqual": '*=',
    }, 

    "aritmetico": {  #aritimetico
        "Div": '/',
        "Modulo": '%',
        "Minus": '-',
        "Plus": "+",
        "Times": "*",
    },
        
    "delimitadores": {  #delimitadores
        "Comma": ',',
        "LeftBrace": '{',
        "LeftBracket": '[',
        "LeftParen": "(",
        "RightBrace": '}',
        "RightBracket": ']',
        "RightParen": ')',        
    },    
    
    "identificador": 'identifier', #identificadores = nomes de variavel
    "inteiro": 'integer',  #valor explicito (chamado de literal)
    "decimal": 'decimal',  #valor decimal explicito
    "string": 'stringLiteral',  #string entre aspas

    
    "EndOfInput": 'EndOfInput',  #fim da entrada de leilura, fim do arquivo lido
    "Unrecognized": 'Unrecognized'  #para um lexema nao reconhecido, sem tipo definido
}
