# coding=utf8
#Parser — синтаксический анализатор.
import re

class Parser:
    def __init__(self, string):
        self.string = string
        self.error = None
        self.lang()


    def lang(self):
        for i in range(len(self.string)):
            self.error = False
            self.expr()

    def expr(self):
        self.VAR()
        self.ASSIGN_OP()
        self.stmt()

    def VAR(self):
        re.match("^[a-zA-Z][a-zA-Z0-9]*$", self.string)

    def ASSIGN_OP(self):
        pass

    def stmt(self):
        pass


if __name__ == '__main__':
    file = open('program', 'r')
    string = file.readline()
    print(string)
    parser = Parser(string)

    file.close()



