def dict_to_list(l1, l2):
    res = dict(zip(l1, l2))
    return res


value = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
key = [1,2,3,4,5,6,7,8,9]
result = dict_to_list(key, value)
print(result)

num = int(input("enter the number to checked in dict"))

if num in result.keys():
    print(result[num])