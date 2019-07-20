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
        
def tokenize(exp):
    exp = exp.replace('\n', ' ')
    
    while exp.find('  ')>0:
        exp = exp.replace('  ', ' ')
    
    tokens = []
    w = ''
    
    def add_word():
        nonlocal w
        if w != '':
            tokens.append(Token('word', w))
            w = ''
    
    for k in exp:                
        if k == '(':
            tokens.append(Token('open'))
        elif k == ')':
            add_word()
            tokens.append(Token('close'))
        elif k == ' ':
            add_word()
        else:
            w = w + k
    
    return tokens