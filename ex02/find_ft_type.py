def all_thing_is_obj(object: any) -> int:
    type_actions = {
        list: lambda x: print("List :", type(x)),
        tuple: lambda x: print("Tuple :", type(x)),
        set: lambda x: print("Set :", type(x)),
        dict: lambda x: print("Dict :", type(x)),
        str: lambda x: print(x + " is in the kitchen :", type(x))
    }

    action = type_actions.get(type(object), lambda x: print("Type not found"))
    action(object)

    return 42
