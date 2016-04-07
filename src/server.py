import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>\-)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>\=)'
WS = r'(?P<WS>\s)'
DEVIDE = r'(?P<DEVIDE>\/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'

tokenizer = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS, DEVIDE, LPAREN, RPAREN]))


def generate(pat, text):
    tokens = pat.scanner(text)
    for token in iter(tokens.match, None):
        k = token.lastgroup, token.group()
        if k[0] != 'WS':
            yield k

if __name__ == '__main__':
    for i in generate(tokenizer, "( 1* 2+3)"):
        print i

