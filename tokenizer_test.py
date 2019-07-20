from tokenizer import tokenize, Token

def test_tokenize_empty_string():
    assert tokenize('') == []

def test_tokenize_simple_parans():
    result = tokenize('(id)')
    expected = [Token('open'), Token('word', 'id'), Token('close')]

    assert all([a == b for a, b in zip(result, expected)])

def test_tokenize_cascaded_parans():
    result = tokenize('(mul (add 1 2) 3)')
    expected = [Token('open'), Token('word', 'mul'),
                Token('open'), Token('word', 'add'), Token('word', '1'), Token('word', '2'), Token('close'),
                Token('word', '3'), Token('close')]

    assert all([a == b for a, b in zip(result, expected)])

def test_tokenize_list_of_expressions():
    result = tokenize('(print 1) (exit)')
    expected = [Token('open'), Token('word', 'print'), Token('word', '1'), Token('close'),
                Token('open'), Token('word', 'exit'), Token('close')]
    
    assert all([a == b for a, b in zip(result, expected)])

def test_tokenize_with_spaces():
    result = tokenize('''(mul 
                            2 
                            3
                         )''')
    expected = [Token('open'), Token('word', 'mul'), Token('word', '2'), Token('word', '3'), Token('close')]
    
    assert all([a == b for a, b in zip(result, expected)])

def test_tokenize_list():
    result = tokenize("'(1 2 3)")

    expected = [
        Token('list_open'),
        Token('word', '1'), Token('word', '2'), Token('word', '3'),
        Token('list_close')
    ]

    assert all([a == b for a, b in zip(result, expected)])

def test_tokenize_list_in_func():
    result = tokenize("(avg '(1 2 3))")

    expected = [
        Token('open'), Token('word', 'avg'),
        Token('list_open'),
        Token('word', '1'), Token('word', '2'), Token('word', '3'),
        Token('list_close'),
        Token('close')
    ]

    assert all([a == b for a, b in zip(result, expected)])