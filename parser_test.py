from tokenizer import tokenize, Token
from parser import parse, Func

def test_parse_simple_tokens():
    tokens = tokenize('(add 1 2)')
    result = parse(tokens)

    assert result.name == 'add' and result.params == [Token('word', '1'), Token('word', '2')]

def test_parse_cascaded_parans():
    tokens = tokenize('(add (mul 3 4) 5)')
    result = parse(tokens)

    expected_params = [Func('mul', [Token('word', '3'), Token('word', '4')]), Token('word', '5')]

    assert result.name == 'add' and all([a == b for a, b in zip(result.params, expected_params)])
    
def test_parse_list_of_expressions():
    tokens = tokenize('(print) (exit)')
    result = parse(tokens)

    expected_ast = [Func('print'), Func('exit')]

    assert all([a == b for a, b in zip(result, expected_ast)])

def test_parse_list():
    tokens = tokenize("'(1 2 3)")
    result = parse(tokens)
    expected_list_items = [
        Token('word', '1'), Token('word', '2'), Token('word', '3')
    ]
    assert result.token_type == 'list' and all([a == b for a, b in zip(result.val, expected_list_items)])