ctx = {
    'add': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'print': lambda x: print(f'>> {x}'),
    '=': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '<': lambda x, y: x<y,
    '>': lambda x, y: x>y,
    '>=': lambda x, y: x>=y,
    '<=': lambda x, y: x<=y,
    'or': lambda x, y: x or y
}