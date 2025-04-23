from interpreter.lexer import*

'''
----------------------
Evaluator Class
----------------------
This class evaluates an abstract syntax tree (AST) representing arithmetic expressions.
It also maintains variable assignments in a local environment (`self.vars`).

'''
class Evaluator:

    def __init__(self):
        # Dictionary to store variable(token types) and arguement(token values)
        self.vars = {}

    def eval(self, node):
        if node[0] == NUM:
            # Return number directly
            return node[1]
        elif node[0] == VARIABLE:
            # Assign any variable to 0 for now (Under development)
            return self.vars.get(node[1],0)
        elif node[0] == PLUS:
            # Return sum | x + y = z
            return self.eval(node[1]) + self.eval(node[2])
        elif node[0] == MINUS:
            # Return difference | x - y = z
            return self.eval(node[1]) - self.eval(node[2])
        elif node[0] == MULTIPLY:
            # Return product | x * y = z
            return self.eval(node[1]) * self.eval(node[2])
        elif node[0] == DIVIDE:
            # Return division | x / y = z
            return self.eval(node[1]) / self.eval(node[2])
        else:
            # Throws error if any unknown token is found
            raise ValueError(f"Unknown node type: {node[0]}")
        
    def assign(self, var, value):
        '''
        Stores the scanned values in the associated variables,
        thus it can be used in the expressions
        '''
        self.vars[var] = value
        