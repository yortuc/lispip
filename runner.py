from tokenizer import tokenize
from parser import parse
from evaluator import evl

def identity(*lines):
    pass

ctx = {
    'add': lambda x, y: x + y,
    'mul': lambda x, y: x * y,
    'print': lambda x: print(f'>> {x}'),
    'app': identity
}

def run(expr, context=ctx):
    return evl(parse(tokenize(expr)), context)

run('''(app
         (defun square (params x) 
             (mul x x))
         
         (defun volume (params x height) 
             (mul (square x) height))
             
         (print (volume 2 6)))''')