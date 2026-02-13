""" 59. Split a list into chunks."""

l1 = [2, 4, 5, 8, 6, 7, 9, 11, 15]
chunk_size = int(input("Enter the chunk size"))


def split_list(test_list, size):
    return [test_list[i:i + chunk_size] for i in range(0, len(test_list), chunk_size)]

result =  split_list(l1, chunk_size)
print(result)

