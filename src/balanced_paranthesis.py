def is_pairs(open, close):
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    if open =='(' and close == ')':
        return True

def is_balanced(arr):
    stack = []
    size = len(arr)
    for i in range (0, size):
        print(arr[i])
        if arr[i] == '[' or arr[i] == '(' or arr[i] == '{':
            stack.append(arr[i])
        elif arr[i] == ']' or arr[i] == ')' or arr[i] == '}':
            if is_pairs(stack[-1], arr[i] or len(stack)!=0 ):
                stack.pop()
            else:
                return False

    if len(stack)==0:
        return True
    else:
        return False

a= '[[()](){}}]'
flag = is_balanced(a)
print(flag)




