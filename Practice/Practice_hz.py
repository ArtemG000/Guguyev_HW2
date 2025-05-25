import copy

def symbols_delete(value: (str, dict, list, None)) -> str:
    """
    func return string without '-' and with element after '\\'. Or iterable object
    """
    if type(value) is not str:
        return value
    if value.startswith('-'):
        value = value[1:].lstrip()
        if not value:
            return None
    value_lst = []
    i = 0
    while i < len(value):
        if value[i] == '\\' and i + 1 < len(value):
            value_lst.append(value[i + 1])
            i += 2
        else:
            value_lst.append(value[i])
            i += 1
    return ''.join(value_lst).strip()

def value_converter(iterable_obj, element_value: str, element_index: (int, str)) -> (bool, int, float, str):
    """
    checks and coverts the element from iterable_object
    element_index either index for list or key for dict
    """

    bool_dct = {'true': True, 'false': False}
    if element_value is None or len(element_value) == 0:
        iterable_obj[element_index] = None
    elif type(element_value) is not str:
        iterable_obj[element_index] = element_value
    elif "null" in element_value.lower() and not (element_value.startswith('"') and element_value.endswith('"')):
        iterable_obj[element_index] = None
    elif element_value.isdigit():
        iterable_obj[element_index] = int(element_value)
    elif element_value.lower() in bool_dct:
        iterable_obj[element_index] = bool_dct[element_value.lower()]
    elif element_value.startswith('"') and element_value.endswith('"'):
        iterable_obj[element_index] = element_value[1: -1]
    else:
        iterable_obj[element_index] = element_value

def deep_add(list_to_save_tmp_deep, list_with_deep_iterable_obj) :
    """
    checks the inserted element and creates a list in the correct format
    """
    x = copy.deepcopy(list_to_save_tmp_deep)
    x = yaml('\n'.join(x))
    list_to_save_tmp_deep.clear()
    list_with_deep_iterable_obj.append(x)

def yaml(a: (str, list, dict)) -> (dict, list):
    end_dict = {}
    end_list = []
    lst = [i for i in a.splitlines() if i]
    if any([i.startswith('  ') for i in lst]):
        temporary_list_with_deep = []
        list_with_deep_iterable_obj = []
        for ind, el in enumerate(lst[:-1]):
            if el.startswith('  ') and lst[ind + 1].startswith('  ') and lst[ind + 1] is lst[-1]:
                temporary_list_with_deep.append(el[2:])
                temporary_list_with_deep.append(lst[ind + 1][2:])
                deep_add(temporary_list_with_deep, list_with_deep_iterable_obj)
            elif el.startswith('  ') and lst[ind + 1].startswith('  '):
                temporary_list_with_deep.append(el[2:])
            elif el.startswith('  ') and not lst[ind + 1].startswith('  '):
                temporary_list_with_deep.append(el[2:])
                deep_add(temporary_list_with_deep, list_with_deep_iterable_obj)
            else:
                list_with_deep_iterable_obj.append(el)
            if lst[ind + 1] is lst[-1] and not lst[ind + 1].startswith('  '):
                if temporary_list_with_deep:
                    temporary_list_with_deep.append(el[2:])
                    deep_add(temporary_list_with_deep, list_with_deep_iterable_obj)
                list_with_deep_iterable_obj.append(lst[ind + 1])
        lst = list_with_deep_iterable_obj
    # list
    if all([":" not in line for line in lst]):
        for line in lst:
            if type(line) is not str:
                end_list.append(line)
                continue
            if '"' in line:
                text_in_line = symbols_delete(line)
                if text_in_line.startswith('"') and text_in_line.endswith('"'):
                    end_list.append(text_in_line)
                    continue
            # checks the comments
            if '#' in line:
                text_in_line = symbols_delete(line.split('#')[0])
                if text_in_line:
                    end_list.append(f'{text_in_line}')
            else:
                text_in_line = symbols_delete(line)
                if text_in_line:
                    end_list.append(f'{text_in_line}')
                else:
                    end_list.append(None)

        for i, el in enumerate(end_list):
            value_converter(end_list, el, i)
        if any([type(_) in (list, dict) for _ in end_list]):
            result_list = []
            for i, el in enumerate(end_list):
                if el is None and isinstance(end_list[i + 1], (list, dict)) and i != len(end_list):
                    continue
                result_list.append(el)
            end_list = copy.deepcopy(result_list)
        return end_list

    # dict
    for ind, key_value in enumerate(lst):
        if not key_value or isinstance(key_value, (list, dict, int)):
            continue
        if key_value.endswith(':') and not key_value is lst[-1] and isinstance(lst[ind + 1], (list, dict)):
            key = key_value[:-1]
            value = lst[ind + 1]
        else:
            key, value = map(str.strip, key_value.split(':', 1))
        value = symbols_delete(value)
        value_converter(end_dict, value, key)
    print(f'end_dict:{end_dict}')
    return end_dict

assert yaml("- Alex\n-\n  - odessa\n  - dnipro\n- Li") == [
    "Alex",
    ["odessa", "dnipro"],
    "Li",
]
assert yaml("- 67\n-\n  name: Irv\n  game: Mario\n-\n- 56") == [
    67,
    {"game": "Mario", "name": "Irv"},
    None,
    56,
]
assert yaml("name: Alex\nstudy:\n  type: school\n  number: 78\nage: 14") == {
    "age": 14,
    "study": {"type": "school", "number": 78},
    "name": "Alex",
}
assert yaml('name: Alex\nstudy:\n  - 89\n  - 89\n  - "Hell"\nage: 14') == {
    "age": 14,
    "study": [89, 89, "Hell"],
    "name": "Alex",
}
assert yaml(
    "name: Alex\nstudy:\n  -\n    type: school\n    num: 89\n  -\n    type: school\n    num: 12\nage: 14"
) == {
    "age": 14,
    "study": [{"num": 89, "type": "school"}, {"num": 12, "type": "school"}],
    "name": "Alex",
}
assert yaml(
    "name: Alex\nstudy:\n  -\n    type: school\n    nums:\n      - 12\n      - 67\n  -\n    type: school\n    num: 12\nage: 14"
) == {
    "age": 14,
    "study": [{"type": "school", "nums": [12, 67]}, {"num": 12, "type": "school"}],
    "name": "Alex",
}

assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {'coding': None, 'name': 'Bob Dylan', 'children': 6}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
assert yaml('- true\n- false\n- "false"\n- "null"\n- null') == [True, False, "false", "null", None]

assert yaml('- write some\n- "Alex Chii"\n- 89') == ["write some", "Alex Chii", 89]
assert yaml("- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5") == [1, 2, 3, 4, 5]
assert yaml("-\n-\n-\n- 7") == [None, None, None, 7]
assert yaml(
    '# comment\n- write some # after\n# one mor\n- "Alex Chii #sir "\n- 89 #bl'
) == ["write some", "Alex Chii #sir ", 89]
assert yaml('key: 1\nactive: true\nname: "Tester"\nflag: false\nnone: null') == {
    'key': 1, 'active': True, 'name': 'Tester', 'flag': False, 'none': None
}