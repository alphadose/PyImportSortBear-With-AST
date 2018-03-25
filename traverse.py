from antlr4 import *
from Python2Lexer import Python2Lexer
from Python2Visitor import Python2Visitor
from Python2Parser import Python2Parser
import sys

class CustomVisitor(Python2Visitor):

	def visitDotted_name(self, ctx:Python2Parser.Import_stmtContext):
		print("Parent package: " + ctx.getText())
		return self.visitChildren(ctx)

	def visitDotted_as_name(self, ctx:Python2Parser.Dotted_as_nameContext):
		info = ctx.getText()
		if "as" in info:
			packages = info.split("as")
			print("Package {} aliased as {}".format(packages[0],packages[1]))
		return self.visitChildren(ctx)

	def visitImport_from(self, ctx:Python2Parser.Import_as_nameContext):
		info = ctx.getText()
		print("Package {} derived from package {}".format(info[-1], info[4]))
		return self.visitChildren(ctx)

def main():
    lexer = Python2Lexer(FileStream(sys.argv[1]))
    stream = CommonTokenStream(lexer)
    parser = Python2Parser(stream)
    tree = parser.file_input()
    visitor = CustomVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()