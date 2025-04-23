from interpreter.lexer import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0   # Keeps track of the current position in the token list

    def parse(self):
        # Start parsing the expression from the beginning
        return self.parse_expression()

    def current_token(self):
        # Return current token or None if out of bounds
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def eat(self, expected_type):
        """
        Consume the current token if it matches the expected type/kind.
        Advances the position or raises a syntax error.
        This function skips 'NONE' tokens (whitespace).
        """
        token = self.current_token()

        # Skip over NONE (whitespace) tokens
        while token and token[0] == NONE:
            self.position += 1
            token = self.current_token()

        # Now check if the current token matches the expected type
        if token and token[0] == expected_type:
            self.position += 1
        else:
            raise SyntaxError(f"Expected token: {expected_type}, got: {token}")

    def parse_expression(self):
        """
        Parses addition and subtraction.
        """
        left = self.parse_term()  # Parse the initial term

        # Continue parsing as long as the current token is a PLUS or MINUS operator
        while self.current_token() and self.current_token()[0] in (PLUS, MINUS):
            operator = self.current_token()  # Get the operator token
            self.eat(operator[0])  # Consume the operator
            right = self.parse_term()  # Parse the term after the operator
            left = (operator[0], left, right)  # Build the AST node for the operation

        return left

    def parse_term(self):
        """
        Parses multiplication and division.
        """
        left = self.parse_factor()  # Parse the initial factor

        # Continue parsing as long as the current token is a MULTIPLY or DIVIDE operator
        while self.current_token() and self.current_token()[0] in (MULTIPLY, DIVIDE):
            operator = self.current_token()  # Get the operator token
            self.eat(operator[0])  # Consume the operator
            right = self.parse_factor()  # Parse the factor after the operator
            left = (operator[0], left, right)  # Build the AST node for the operation

        return left

    def parse_factor(self):
        """
        Parses numbers, variables, and expressions in parentheses.
        """
        token = self.current_token()

        if token[0] == NUM:
            self.eat(NUM)  # Consume the number token
            return (NUM, int(token[1]))  # Return an AST node for the number

        elif token[0] == VARIABLE:
            self.eat(VARIABLE)  # Consume the variable token
            return (VARIABLE, token[1])  # Return an AST node for the variable

        elif token[0] == LEFT_BRACE:
            self.eat(LEFT_BRACE)  # Consume the left parenthesis
            node = self.parse_expression()  # Recursively parse the expression inside
            self.eat(RIGHT_BRACE)  # Consume the right parenthesis
            return node

        else:
            raise SyntaxError("Expected a number, variable, or parenthesis")
