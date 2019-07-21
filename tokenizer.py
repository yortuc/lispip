class Token:
    def __init__(self, token_type, val=None):
        self.token_type = token_type
        self.val = val
    
    def __str__(self):
        return f'{self.token_type}:{self.val}'
    
    def __eq__(self, other):
        if isinstance(other, Token):
            return self.token_type == other.token_type and self.val == other.val
        return False

def preprocess_string_expression(exp):
    """Clean the expression"""
    exp = exp.replace('\n', ' ')
    
    while exp.find('  ')>0:
        exp = exp.replace('  ', ' ')

    return exp

def tokenize(exp):
    exp = preprocess_string_expression(exp)

    tokens = []
    w = ''
    list_open = False
    string_open = False
    
    def add_word():
        nonlocal w
        if w != '':
            tokens.append(Token('word', w))
            w = ''
    
    index = 0
    while index < len(exp):  
        k = exp[index]
        if k == '(':
            tokens.append(Token('open'))
        
        elif k == ')':
            add_word()
            tokens.append(Token('list_close' if list_open else 'close'))
            list_open = False
        
        elif k == ' ' and string_open == False:
            add_word()

        elif k == "'": # list starter
            if exp[index+1] == '(':
                list_open = True
                tokens.append(Token('list_open'))
                index += 1

        elif k == '"':
            if string_open: # close string
                tokens.append(Token('word', w))
                w = ''
                string_open = False
            else:
                string_open = True
        
        else:
            w = w + k

        index += 1
    
    return tokens