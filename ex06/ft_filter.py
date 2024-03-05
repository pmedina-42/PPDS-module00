def ft_filter(func, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    filtered_list = []
    for item in iterable:
        if func(item):
            filtered_list.append(item)
    return filtered_list
