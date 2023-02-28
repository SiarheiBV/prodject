first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5, "a": 9}


def merge(dict1, dict2):
    return {key: [dict1.get(key), dict2.get(key)]
            for key in sorted(dict1.keys() | dict2.keys())}


print(merge(first_dict, second_dict))
