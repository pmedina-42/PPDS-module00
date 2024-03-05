def ft_filter(func, iterable):
    filtered_list = []
    for item in iterable:
        if func(item):
            filtered_list.append(item)
    return filtered_list
