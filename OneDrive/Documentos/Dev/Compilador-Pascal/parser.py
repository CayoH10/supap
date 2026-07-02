from token_Type import TokenType
from simbol_table import SymbolTable

class Parser:

    def __init__(self, lexer):
        
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.symbol_table = SymbolTable()
        self.procedures = {}

    def eat(self, token_type):

        if self.current_token.type == token_type:

            print(f"Consumindo: {self.current_token}")

            self.current_token = self.lexer.get_next_token()

        else:
            raise Exception(
                f"Erro sintático. Esperado {token_type} "
                f"mas veio {self.current_token.type}"
            )
        
    def header(self):

        self.eat(TokenType.PROGRAM)
        self.eat(TokenType.ID)
        self.eat(TokenType.SEMICOLON)

    def declarations(self):

        if self.current_token.type == TokenType.VAR:
            self.variable_declarations()
        while self.current_token.type == TokenType.PROCEDURE:
            self.procedure_declarations()

    def procedure_declarations(self):
        while self.current_token.type == TokenType.PROCEDURE:

            self.procedure_declaration()

    def procedure_declaration(self):
        self.eat(TokenType.PROCEDURE)

        proc_name = self.current_token.value

        if proc_name in self.procedures:
            raise Exception(
                f"Procedure já declarada: {proc_name}"
            )

        self.procedures[proc_name] = True

        self.eat(TokenType.ID)

        self.eat(TokenType.SEMICOLON)

        print(f"Procedure declarada: {proc_name}")

        self.declarations()

        self.block()

        self.eat(TokenType.SEMICOLON)

    def variable_declarations(self):
        self.eat(TokenType.VAR)

        while self.current_token.type == TokenType.ID:

            self.variable_declaration()

    def variable_declaration(self):

        identifiers = self.identifier_list()

        self.eat(TokenType.COLON)

        var_type = self.type_spec()

        self.eat(TokenType.SEMICOLON)

        for identifier in identifiers:

            self.symbol_table.define(identifier, var_type)

            print(f"Variável declarada: {identifier} -> {var_type}")

    def identifier_list(self):

        identifiers = []

        identifiers.append(self.current_token.value)

        self.eat(TokenType.ID)

        while self.current_token.type == TokenType.COMMA:

            self.eat(TokenType.COMMA)

            identifiers.append(self.current_token.value)

            self.eat(TokenType.ID)

        return identifiers

    def type_spec(self):

        if self.current_token.type == TokenType.INTEGER:

            self.eat(TokenType.INTEGER)

            return "integer"

        elif self.current_token.type == TokenType.REAL:

            self.eat(TokenType.REAL)

            return "real"

        else:
            raise Exception("Tipo inválido")

    def block(self):

        self.eat(TokenType.BEGIN)

        self.statements()

        self.eat(TokenType.END)

    def statements(self):

        self.statement()

        while self.current_token.type == TokenType.SEMICOLON:

            self.eat(TokenType.SEMICOLON)

            self.statement()

    def statement(self):

        if self.current_token.type == TokenType.ID:

            var_name = self.current_token.value

            self.eat(TokenType.ID)

            # chamada de procedure
            if self.current_token.type == TokenType.LPAREN:
                if var_name not in self.procedures:

                    raise Exception(
                        f"Procedure não declarada: {var_name}"
                    )

                self.eat(TokenType.LPAREN)
                self.eat(TokenType.RPAREN)

            # atribuição
            else:

                if self.symbol_table.lookup(var_name) is None:

                    raise Exception(
                        f"Variável não declarada: {var_name}"
                    )

                self.eat(TokenType.ASSIGN)

                self.expression()

        elif self.current_token.type == TokenType.IF:

            self.eat(TokenType.IF)

            self.expression()

            self.eat(TokenType.THEN)

            self.statement()

            if self.current_token.type == TokenType.ELSE:

                self.eat(TokenType.ELSE)

                self.statement()

        elif self.current_token.type == TokenType.WHILE:

            self.eat(TokenType.WHILE)

            self.expression()

            self.eat(TokenType.DO)

            self.statement()

        elif self.current_token.type == TokenType.BEGIN:

            self.block()

        else:
            pass

    def simple_expression(self):

        self.term()

        while self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS
        ):

            if self.current_token.type == TokenType.PLUS:

                self.eat(TokenType.PLUS)

            else:

                self.eat(TokenType.MINUS)

            self.term()

    def expression(self):

        self.simple_expression()

        if self.current_token.type in (

            TokenType.GREATER,
            TokenType.LESS,
            TokenType.EQUAL,
            TokenType.GREATER_EQUAL,
            TokenType.LESS_EQUAL,
            TokenType.NOT_EQUAL

        ):

            self.eat(self.current_token.type)

            self.simple_expression()

    def term(self):

        self.factor()

        while self.current_token.type in (
            TokenType.MULT,
            TokenType.DIV
        ):
            if self.current_token.type == TokenType.MULT:
                self.eat(TokenType.MULT)

            elif self.current_token.type == TokenType.DIV:
                self.eat(TokenType.DIV)

            self.factor()

    def factor(self):

        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)

        elif token.type == TokenType.ID:
            self.eat(TokenType.ID)

        elif token.type == TokenType.LPAREN:

            self.eat(TokenType.LPAREN)

            self.expression()

            self.eat(TokenType.RPAREN)

        else:
            raise Exception("Erro em factor")
        
    def program(self):

        self.header()

        self.declarations()

        self.block()

        self.eat(TokenType.DOT)

        print("Programa sintaticamente correto!")