ctx = {
    'string': lambda *x: ' '.join(x),
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
    'avg': lambda lst: sum(lst)/len(lst),
    'first': lambda lst: lst[0],
    'tail': lambda lst: lst[1:],
    'map': lambda fn, lst: [fn(k) for k in lst],
    #
    'list': lambda *x: [k for k in x]
}
