from antlr4 import *
from antlr4.tree.Trees import Trees
from Python2Lexer import Python2Lexer
from Python2Listener import Python2Listener
from Python2Parser import Python2Parser
import sys

def main():
    lexer = Python2Lexer(FileStream(sys.argv[1]))
    stream = CommonTokenStream(lexer)
    parser = Python2Parser(stream)
    tree = parser.file_input()
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main()