class SymbolTable:

    def __init__(self):

        self.symbols = {}

    def define(self, name, type):
        if name in self.symbols:
            raise Exception(
                f"Variável já declarada: {name}"
            )
        self.symbols[name] = type

    def lookup(self, name):

        return self.symbols.get(name)
    
    def __repr__(self):

        return str(self.symbols)