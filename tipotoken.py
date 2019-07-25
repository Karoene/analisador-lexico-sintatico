# -*- coding: utf-8 -*-
TIPO_TOKEN = {  #dicionario com os token que a linguagem aceita 
    "palavra": {
        "variavel": 'variavel',
        "inicia": 'inicia',
        "termina": 'termina',
        "Int": 'int',
        "Const": 'const',
        "Double": 'double',
        "Char": 'char',
        "String": 'string',
        "If": 'if',
        "Else": 'else',
        "True": 'true',
        "False": 'false',
        "Null": 'null',
        "Return": 'return',
        "While": 'while',
        "For": 'for',
        "Break": 'break',
        "Continue": 'continue',
        "Void": 'void'
   },
    
    "atribuicao": {   #grupo (atribuição)        
        "Equal": '=',  #atribuicao        
        "DivEqual": '/=',
        "MinusEqual": '-=',
        "ModuloEqual": '%=',
        "PlusEqual": '+=',
        "TimesEqual": '*='
    }, 

    "aritmetico": {  #aritimetico
        "Div": '/',
        "Modulo": '%',
        "Menos": '-',
        "Mais": "+",
        "Mult": "*",
    },

    "comparacao": {
        "DoubleEqual": '==',
        "Greater": '>',
        "GreaterOrEqual": '>=',
        "Less": '<',
        "LessOrEqual": '<=',
        "NotEqual": '!='
    },

    'booleano': {
        'And': '&&',
        'Not': '!',
        'Or': '||'
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
