from token_Type import TokenType
from tokens import  Token

class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1

        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):

        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def identifier(self):

        result = ""

        while (
            self.current_char is not None and
            (self.current_char.isalnum() or self.current_char == '_')
        ):
            result += self.current_char
            self.advance()

        keywords = {
            "program": TokenType.PROGRAM,
            "var": TokenType.VAR,
            "begin": TokenType.BEGIN,
            "end": TokenType.END,
            "integer": TokenType.INTEGER,
            "real": TokenType.REAL,
            "if": TokenType.IF,
            "then": TokenType.THEN,
            "else": TokenType.ELSE,
            "while": TokenType.WHILE,
            "do": TokenType.DO,
            "procedure": TokenType.PROCEDURE
        }

        token_type = keywords.get(result.lower(), TokenType.ID)

        return Token(token_type, result)
    
    def number(self):

        result = ""

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += '.'
            self.advance()

            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            return Token(TokenType.NUMBER, float(result))
        
        return Token(TokenType.NUMBER, int(result))
    
    
    def get_next_token(self):

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                return self.identifier()
            
            if self.current_char.isdigit():
                return self.number()
            
            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS, '+')
            
            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULT, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/')
            
            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            
            if self.current_char == ';':
                self.advance()
                return Token(TokenType.SEMICOLON, ';')
            
            if self.current_char == '=':

                self.advance()

                return Token(TokenType.EQUAL, '=')
            
            if self.current_char == ',':
                self.advance()
                return Token(TokenType.COMMA, ',')
            
            if self.current_char == '.':
                self.advance()
                return Token(TokenType.DOT, '.')
            
            if self.current_char == '>':

                self.advance()

                if self.current_char == '=':

                    self.advance()

                    return Token(TokenType.GREATER_EQUAL, '>=')

                return Token(TokenType.GREATER, '>')
            
            if self.current_char == '<':

                self.advance()

                if self.current_char == '=':

                    self.advance()

                    return Token(TokenType.LESS_EQUAL, '<=')

                if self.current_char == '>':

                    self.advance()

                    return Token(TokenType.NOT_EQUAL, '<>')

                return Token(TokenType.LESS, '<')
            
            if self.current_char == ':':

                self.advance()

                if self.current_char == '=':
                    self.advance()
                    return Token(TokenType.ASSIGN, ':=')
                
                return Token(TokenType.COLON, ':')
            raise Exception(f"Caractere inválido: {self.current_char}")
        return Token(TokenType.EOF, None)