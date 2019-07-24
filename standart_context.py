import random

def extend_context(c1):
    for k in c1:
        ctx[k] = c1[k]

def set_global_var(key, value):
    ctx[key] = value

def identity(*params):
    pass
        
ctx = {
    'block': identity,
    'set': lambda k, v: set_global_var(key, value),

    # string funcs
    'string': lambda *x: ' '.join(x),
    'string-concat': lambda *x: ''.join(x),

    # math
    'add': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'print': lambda x: print(f'{x}'),
    '=': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '<': lambda x, y: x<y,
    '>': lambda x, y: x>y,
    '>=': lambda x, y: x>=y,
    '<=': lambda x, y: x<=y,
    'or': lambda x, y: x or y,
    'int': lambda str: int(str),
    'create-random': lambda x, y: random.randint(x, y),

    # List funcs
    'list': lambda *x: [k for k in x],
    'avg': lambda lst: sum(lst)/len(lst),
    'first': lambda lst: lst[0],
    'tail': lambda lst: lst[1:],
    'map': lambda fn, lst: [fn(k) for k in lst],
    'list-add': lambda lst, item: lst + [item],
    
    # import python-binding
    'import': lambda file_name: extend_context(getattr(__import__(file_name), 'ctx')),
    
     # meta
    'running-context': lambda: [c for c in ctx],
}
