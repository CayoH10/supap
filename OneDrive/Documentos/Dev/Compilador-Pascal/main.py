from lexer import Lexer
from parser import Parser

with open("exemplo.pas", "r") as file:
    text = file.read()

lexer = Lexer(text)

parser = Parser(lexer)

parser.program()