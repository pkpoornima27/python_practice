

arr = [98, 56, 71, 12, 46, 54, 23, 8]

def min_diff(a):
    a.sort()
    diff_arr = []
    size = len(a)
    for i in range(0, size-1):
        diff = a[i+1] - a[i]
        print(diff)
        diff_arr.append(diff)
    diff_arr.sort()
    return diff_arr[0]

def max_diff(a):
    a.sort()
    diff_arr = []
    size = len(a)
    for i in range(0, size-1):
        diff =  a[i+1]- a[i]
        diff_arr.append(diff)
    diff_arr.sort(reverse=True)
    return diff_arr[0]



r_min =  min_diff(arr)
r_max = max_diff(arr)
print("min diff:", r_min)
print("Maximum diff", r_max)