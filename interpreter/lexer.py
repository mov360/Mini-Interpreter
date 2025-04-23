import re

'''
-------------------------------
Token Definitions (Token Types)
-------------------------------
Using constants for token types to avoid typos and ensure consistency across files.
VARIABLE & EQUIVALENT related logics will be available in Future
'''

NUM = 'NUM'                 # Decimal Numbers (e.g., 123)
VARIABLE = 'VARIABLE'       # Variable name (e.g., x, y, total)
PLUS = 'PLUS'               # Addition '+'
MINUS = 'MINUS'             # Subtraction '-'
MULTIPLY = 'MULTIPLY'       # Multiplication '*'
DIVIDE = 'DIVIDE'           # Division '/'
EQUIVALENT = 'EQUIVALENT'   # Assignment '='
LEFT_BRACE = 'LEFT_BRACE'   # Left bracket '('
RIGHT_BRACE = 'RIGHT_BRACE' # Right bracket ')'
NONE = 'NONE'               # Whitespace (to be ignored)
INVALID = 'INVALID'         # Any unrecognized characters

'''
-------------------
Tokenizer Function
-------------------
This function scans the input text and yields a sequence of (kind, value) pairs.
'''

def tokenize(text):
    token_types = [
        (NUM, r'\d+'),
        (VARIABLE, r'[a-zA-Z]+'),
        (PLUS, r'\+'),
        (MINUS, r'\-'),
        (MULTIPLY, r'\*'),
        (DIVIDE,r'/'),
        (EQUIVALENT, r'\='),
        (LEFT_BRACE, r'\('),
        (RIGHT_BRACE, r'\)'),
        (NONE, r'\s+'), # Whitespace (to be ignored)
        (INVALID, r'.'), # Invalid tokens
    ]

    # Compile a single regex pattern using named groups for each token type
    pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_types)

    # Iterate through the input text to find matches
    for match_object in re.finditer(pattern, text):
        kind = match_object.lastgroup  # Matched token type (e.g., Variable, NUM)
        value = match_object.group()   # Matched token value (e.g., 42, +, x)

        if kind == 'INVALID':
            # Raise error for invalid characters
            raise SyntaxError(f"Invalid character: {value}")
        elif kind != 'NONE':  # Skip 'NONE' token type (spaces)
            # Yield token type(kind) and value
            yield kind, value
