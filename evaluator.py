def evl(root, context={}):
    if root.token_type == 'word':
        try:
            num = float(root.val)
            return num
        except:
            if root.val in context:
                return context[root.val]
            else:
                return root.val
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
        else:
            # standart func evaluation, first eval params
            params = []
            for p in root.params:
                params.append(evl(p, context))
            return context[root.name](*params)