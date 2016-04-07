import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>\=)'
WS = r'(?P<WS>\s)'
tokenizer = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def generate(pat, text):
    tokens = pat.scanner(text)
    for token in iter(tokens.match, None):
        k = token.lastgroup, token.group()
        yield k
for tok in generate(tokenizer, 'foo = 43+334*34+343=23'):
    print tok
