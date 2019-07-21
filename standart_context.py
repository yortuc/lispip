def extend_context(c1):
    for k in c1:
        ctx[k] = c1[k]

def set_global_var(key, value):
        ctx[key] = value

ctx = {
    'set': lambda k, v: set_global_var,

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

    # List funcs
    'list': lambda *x: [k for k in x],
    'avg': lambda lst: sum(lst)/len(lst),
    'first': lambda lst: lst[0],
    'tail': lambda lst: lst[1:],
    'map': lambda fn, lst: [fn(k) for k in lst],
    
    # import python-binding
    'import': lambda file_name: extend_context(getattr(__import__(file_name), 'ctx'))
}
