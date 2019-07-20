def evl_list(nodes, context):
    result = None
    for n in nodes:
        result = evl(n, context)
    return result

def evl_single(root, context):
    # Single 
    if root.token_type == 'word':
        try:
            num = float(root.val)
            return num
        except:
            if root.val in context:
                return context[root.val]
            else:
                return root.val
    
    elif root.token_type == 'list':
        # evaluate all items in list and return
        evaluated_list = []
        for t in root.val:
            evaluated_list.append(evl_single(t, context))
        return evaluated_list

    elif root.token_type == 'func':
        if root.name == 'defun':
            # define function
            # (defun square (params x) (mul x x))
            fn_name = root.params[0].val
            fn_params = [p.val for p in root.params[1].params]
            fn_body = root.params[2]
        
            def run_func(*params):
                local_context = context.copy()
                # bind parameter values on function call
                for i in range(len(fn_params)):
                    k = fn_params[i]
                    local_context[k] = params[i]
                return evl(fn_body, local_context)
            context[fn_name] = run_func

        elif root.name == 'if':
            # (if (= a b) (a_equals_b) (a_not_equals_b))
            control_exp = root.params[0]
            control_true = root.params[1]
            control_false = root.params[2]

            if evl(control_exp, context):
                return evl(control_true, context)
            else:
                return evl(control_false, context)

        else:
            # standart func evaluation, first eval params
            # check func is available
            if root.name not in context:
                raise Exception(f'Function `{root.name}` not found in context. \n Context: \n {context}')

            params = []
            for p in root.params:
                params.append(evl(p, context))
            return context[root.name](*params)

def evl(root, context):
    # list
    if type(root) == list:
        return evl_list(root, context)        
    else:
        return evl_single(root, context)