from tokenizer import tokenize
from parser import parse
from evaluator import evl

ctx = { 
    'add': lambda x, y: x + y,
    'mul': lambda x, y: x * y 
}

def test_evaluate_single_expression():
    ast = parse(tokenize('(add 1 2)'))
    result = evl(ast, ctx)
    assert result == 3

def test_evaluate_list_of_expressions_return_last_one():
    ast = parse(tokenize('(add 1 2) (mul 9 8)'))
    result = evl(ast, ctx)
    assert result == 72