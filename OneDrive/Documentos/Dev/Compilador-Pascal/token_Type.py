from enum import Enum, auto

class TokenType(Enum):

    PROGRAM = auto()
    VAR = auto()
    PROCEDURE = auto()
    BEGIN = auto()
    END = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    WHILE = auto()
    DO = auto()

    INTEGER = auto()
    REAL = auto()

    ID = auto()
    NUMBER = auto()

    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()

    ASSIGN = auto()

    EQUAL = auto()
    GREATER = auto()
    LESS = auto()
    GREATER_EQUAL = auto()
    LESS_EQUAL = auto()
    NOT_EQUAL = auto()

    LPAREN = auto()
    RPAREN = auto()

    SEMICOLON = auto()
    COLON = auto()
    COMMA = auto()
    DOT = auto()

    EOF = auto()