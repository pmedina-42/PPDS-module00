ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "tata!")
ft_set = {"Hello", "tata!"}
ft_dict = {"Hello": "tata!"}

# List, ez
ft_list[1] = "World!"

# Tuple, using list
x = list(ft_tuple)
x[1] = "Spain!"
ft_tuple = tuple(x)

# Set, ez
ft_set.remove("tata!")
ft_set.add("Madrid!")

# Dict, ez
ft_dict['Hello'] = "42Madrid!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
