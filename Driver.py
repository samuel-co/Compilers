# pip install antlr4-python3-runtime
import sys
from antlr4 import *
from LittleLexer import LittleLexer
from LittleListener import LittleListener
from LittleParser import LittleParser
from SymbolTableBuilder import SymbolTableBuilder
from AST import AST
from AST_Walker import ast_walker

def main(testcase_filename):
    lexer = LittleLexer(FileStream(testcase_filename))
    stream = CommonTokenStream(lexer)
    parser = LittleParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()

    symbol_table_builder = SymbolTableBuilder()
    walker.walk(symbol_table_builder, tree)
    # symbol_table_builder.print_symbol_table()

    a = AST(symbol_table_builder.symbol_table)
    walker.walk(a, tree)

    aw = ast_walker(a.tree, a.symbol_table)
    aw.print_tree()

    '''
    # Step 3 Code
    symbol_table_builder = SymbolTableBuilder()
    walker = ParseTreeWalker()
    walker.walk(symbol_table_builder, tree)
    symbol_table_builder.print_symbol_table()
    '''

    '''
    # Step 2 Code
    # retrieve token list and pass it into the parser
    lexer = LittleLexer(FileStream(testcase_filename))
    stream = CommonTokenStream(lexer)
    parser = LittleParser(stream)
    # deactivate the parser error messages
    parser.removeErrorListeners()
    # run the tokens through the parse tree
    parser.program()
    # if there were syntax errors the program is accepted, otherwise not accepted
    if parser._syntaxErrors == 0:
        print("Accepted")
    else:
       print("Not accepted")
    '''

    '''
    #Step 1 Code
    lexer = LittleLexer(FileStream(testcase_filename))
    token = lexer.nextToken()

    # while we have valid tokens to read
    while token.type != Token.EOF:
        # pull out the text type of the token from the lexer list
        name = lexer.symbolicNames[token.type]
        # print the token's info
        print("Token Type: {}".format(name))
        print("Value: {}".format(token.text))
        # get the next token
        token = lexer.nextToken()
    '''

if __name__ == '__main__':
	# args[1] contains the address of current testcase
	testcase_filename = sys.argv[1]
	# Now, read this file and you will get the testcase input text
	main(testcase_filename)


