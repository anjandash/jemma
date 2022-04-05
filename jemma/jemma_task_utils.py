"""
jemma_task_utils

author: @anjandash
license: MIT
"""

import javalang


"""
# ----------------------
#  NOTE: Available dicts
# ----------------------
# keywords          = {}
# literal_keywords  = {}
# operators         = {}
# symbols           = {}
# ----------------------
"""

keywords = {
    'ABSTRACT':     'abstract',
    'ASSERT':       'assert',
    'BOOLEAN':      'boolean',
    'BREAK':        'break',
    'BYTE':         'byte',
    'CASE':         'case',
    'CATCH':        'catch',
    'CHAR':         'char',
    'CLASS':        'class', 
    'CONST':        'const',
    'CONTINUE':     'continue',

    'DEFAULT':      'default',
    'DO':           'do',
    'DOUBLE':       'double',
    'ELSE':         'else',
    'ENUM':         'enum',
    'EXTENDS':      'extends',
    'FINAL':        'final',
    'FINALLY':      'finally',
    'FLOAT':        'float',
    'FOR':          'for',
    'GOTO':         'goto',

    'IF':           'if',
    'IMPLEMENTS':   'implements',
    'IMPORT':       'import',
    'INSTANCEOF':   'instanceof',
    'INT':          'int',
    'INTERFACE':    'interface',

    'LONG':         'long',
    'NATIVE':       'native',
    'NEW':          'new',
    'PACKAGE':      'package', 
    'PRIVATE':      'private',
    'PROTECTED':    'protected',
    'PUBLIC':       'public',
    'RETURN':       'return',

    'SHORT':        'short',
    'STATIC':       'static',
    'STRICTFP':     'strictfp',
    'SUPER':        'super',
    'SWITCH':       'switch',
    'SYNCHRONIZED': 'synchronized',

    'THIS':         'this',
    'THROW':        'throw',
    'THROWS':       'throws',
    'TRANSIENT':    'transient',
    'TRY':          'try',
    'VOID':         'void',
    'VOLATILE':     'volatile',
    'WHILE':        'while',

    # 'UNDERSCORE':   '_',          # EXCLUDED! not sure if the grammar supports it
    # 'NONSEALED':    'non-sealed', # EXCLUDED! not sure if the grammar supports it
    #  ------------   ------------  # EXCLUDED! String is not a Java keyword, String is a class
}

literal_keywords = {
    'TRUE':     'true',
    'FALSE':    'false',
    'NULL':     'null',
}

operators = {
    'PLUS':     '+',
    'SUB':      '-',
    'STAR':     '*',
    'SLASH':    '/',
    'PERCENT':  '%',
    'AMP':      '&',
    'BAR':      '|',
    'CARET':    '^',
    'BANG':     '!',
    'EQ':       '=',
    
    'PLUSEQ':   '+=',
    'SUBEQ':    '-=',
    'STAREQ':   '*=',
    'SLASHEQ':  '/=',
    'PERCENTEQ':'%=',
    'AMPEQ':    '&=',
    'BAREQ':    '|=',
    'CARETEQ':  '^=',
    'BANGEQ':   '!=',
    'EQEQ':     '==',

    'LT':       '<',
    'GT':       '>',
    'LTEQ':     '<=',
    'GTEQ':     '>=',
    'LTLT':     '<<',
    'GTGT':     '>>',
    'GTGTGT':   '>>>',
    'LTLTEQ':   '<<=',
    'GTGTEQ':   '>>=',
    'GTGTGTEQ': '>>>=',

    'PLUSPLUS': '++',
    'SUBSUB':   '--',
    'AMPAMP':   '&&',
    'BARBAR':   '||',        

    'QUES':     '?',
    'COLON':    ':',   
    'TILDE':    '~',
    'ARROW':    '->',   

    'INSTANCEOF':'instanceof',
    'COLONCOLON':'::', 

}

symbols = {
    'DOT':      '.',
    'COMMA':    ',',
    'SEMI':     ';',    
    'LPAREN':   '(',
    'RPAREN':   ')',
    'LBRACE':   '{',
    'RBRACE':   '}',
    'LBRACKET': '[',
    'RBRACKET': ']',

    'MONKEYS_AT':'@',
    'ELLIPSIS':  '...', 
}


keywords_reverse = {v:k for k, v in keywords.items()}
literal_keywords_reverse = {v:k for k, v in literal_keywords.items()}
operators_reverse = {v:k for k, v in operators.items()}
symbols_reverse = {v:k for k, v in symbols.items()}


def get_replaced_token(code_token):
    if code_token.upper() in keywords_reverse.keys():
        return keywords_reverse[code_token.upper()]
    elif code_token.upper() in literal_keywords_reverse.keys():
        return literal_keywords_reverse[code_token.upper()]
    elif code_token.upper() in operators_reverse.keys():
        return operators_reverse[code_token.upper()]
    elif code_token.upper() in symbols_reverse.keys():
        return symbols_reverse[code_token.upper()]
    return code_token


def get_actual_token(code_token):
    if code_token.upper() in keywords.keys():
        return keywords[code_token.upper()]
    elif code_token.upper() in literal_keywords.keys():
        return literal_keywords[code_token.upper()]
    elif code_token.upper() in operators.keys():
        return operators[code_token.upper()]
    elif code_token.upper() in symbols.keys():
        return symbols[code_token.upper()]
    return code_token


# ********** #
#            #
# ********** #


def gen_TKNA_from_method_text(method_text):
    tokens = list(javalang.tokenizer.tokenize(method_text))
    tokens = [str(t) for t in tokens]
    tokens = [t[t.index('"')+1:t.rindex('"')] for t in tokens]
    return " ".join(tokens)


def gen_TKNB_from_method_text(method_text):
    tokens = list(javalang.tokenizer.tokenize(method_text))
    tokens = [str(t) for t in tokens]
    tokens = [t[t.index('"')+1:t.rindex('"')] for t in tokens]
    tokens = [get_replaced_token(t) for t in tokens]
    return ",".join(tokens)

def gen_C2VC_from_method_text(method_text):
    pass

def gen_C2SQ_from_method_text(method_text):
    pass

def gen_FTGR_from_method_text(method_text):
    pass

def gen_REPR_from_method_text(method_text):
    pass

def gen_representation(representation, method_id, custom_method_text):

    masked_text = custom_method_text

    if   representation == "TKNA":
        return gen_TKNA_from_method_text(masked_text)
    elif representation == "TKNB":
        return gen_TKNB_from_method_text(masked_text)
    elif representation == "C2VC":
        return gen_C2VC_from_method_text(masked_text)
    elif representation == "C2SQ":
        return gen_C2SQ_from_method_text(masked_text)
    elif representation == "FTGR":
        return gen_FTGR_from_method_text(masked_text)



# ********** #
#            #
# ********** #

def run_models(metric, representation, train_methods, test_methods, models=["MLP", "CNN", "BiLSTM"]):
    pass