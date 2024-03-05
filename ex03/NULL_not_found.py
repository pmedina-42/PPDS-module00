def NULL_not_found(object: any) -> int:
    ta = {
        type(None): lambda x: (print("Nothing :", type(x)), 0),
        float: lambda x: (print("Cheese :", type(x)), 0),
        int: lambda x: (print("Zero :", type(x)), 0),
        str: lambda x: (print("Empty:", type(x)), 0)
        if not x else (print("Type not Found"), 1),
        bool: lambda x: (print("Fake :", type(x)), 0)
    }

    action = ta.get(type(object), lambda x: (print("Type not found"), 1))
    result = action(object)[1]

    if result is None:
        return 0
    else:
        return result
