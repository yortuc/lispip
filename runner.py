from tokenizer import tokenize
from parser import parse
from evaluator import evl

def identity(*lines):
    pass

ctx = {
    'id': lambda x: x,
    'add': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'print': lambda x: print(f'>> {x}'),
    'app': identity,
    '=': lambda x, y: x == y,
    '<': lambda x, y: x<y,
    '>': lambda x, y: x>y,
    '>=': lambda x, y: x>=y,
    '<=': lambda x, y: x<=y
}

def run(expr, context=ctx):
    return evl(parse(tokenize(expr)), context)

run(
'''
(defun factorial (params x)
    (if (< x 2)
        1
        (mul x (factorial (- x 1)))
    )
)
(print (factorial 5))
''')
