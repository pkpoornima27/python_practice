def first_non_repeating_character(s):
    for i in s:
        if s.count(i) == 1:
            return i
    return None

def all_non_repeating_char(s):
    non_repeating_char = ""
    for i in s:
        print(i)
        if s.count(i) == 1:
            non_repeating_char = non_repeating_char + i
    return non_repeating_char


str = "Poornima"
#c = first_non_repeating_character(str)
non_repeating = all_non_repeating_char(str)
print(non_repeating)