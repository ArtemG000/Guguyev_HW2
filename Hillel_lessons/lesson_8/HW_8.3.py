#Вам необхідно написати функцію find_unique_value, яка приймає список із чисел, знаходить серед них унікальне число та повертати його.
#Унікальне число - це число, яке зустрічається в списку один раз. Випадок, коли в одному списку буде кілька унікальних чисел, перевіряти не потрібно.
#Artem Guguyev

def find_unique_value(some_list):
    some_dict = {}
    for key in some_list:
        if key not in some_dict.keys():
            some_dict[key] = 1
        else:
            some_dict[key] += 1
    tpl_nums = list(some_dict.items())
    for i in range(len(tpl_nums)):
        if tpl_nums[i][1] == 1:
            uniq = tpl_nums[i][0]
    return uniq

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
