from server import *

class Parser(object):
    def __init__(self):
        self.cur = None
        self.nexttok = None

    def parse(self, text):
        self.tokens = generate(tokenizer, text) # got the token stream
        self._advance()
        return self.expr()

    def _advance(self):
        self.cur, self.nexttok = self.nexttok, next(self.tokens,None)

    def _accept(self, toktype):
        if self.nexttok and self.nexttok[0] == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected' + toktype)

    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.cur[0]
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -=right
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.cur[0]
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DEVIDE':
                termval /= right
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.cur[1])
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')

if __name__ == '__main__':
    while True:
        exp = raw_input('input your expression >>>')
        parser = Parser()
        print parser.parse(exp)

