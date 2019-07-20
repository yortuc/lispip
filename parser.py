from collections import deque

class Func:
    def __init__(self, name, params=[], token_type='func'):
        self.name = name
        self.params = params
        self.token_type = token_type

    def __str__(self):
        return f'{self.name}:{self.params}'

    def __eq__(self, other):
        if isinstance(other, Func):
            return self.name == other.name and all([a == b for a, b in zip(self.params, other.params)])
        return False
        
def parse(tokens):
    stack = deque()
    
    for k in tokens:
        if k.token_type == 'open' or k.token_type == 'word':
            stack.append(k)
        elif k.token_type == 'close':
            sub = []
            while True:
                cur = stack.pop()
                if cur.token_type == 'open':
                    break
                else:
                    sub = [cur] + sub
            result = Func(sub[0].val, sub[1:])
            stack.append(result)
            
    if len(stack) == 1:
        return stack.pop()
    else:
        return list(stack)