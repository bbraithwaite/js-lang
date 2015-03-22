# TODO: temp place for shared assertion methods

def validate_token_and_value(self, lexer, input, expectedType, expectedValue):
    lexer.input(input)
    token = lexer.token()
    self.assertEqual(token.type, expectedType)
    self.assertEqual(token.value, expectedValue)

def validate_token(self, lexer, input, expectedType):
    validate_token_and_value(self, lexer, input, expectedType, input)

def assertTokenList(self, lexer, tokens):
    for t in tokens:
        if len(t) == 3:
            validate_token_and_value(self, lexer, t[0], t[1], t[2])
        else:
            validate_token(self, lexer, t[0], t[1])