def count_distinct_substrings(s: str) -> int:
    n = len(s)
    substrings = set()

    for i in range(n):
        for j in range(i+1, n+1):
            print(s[i:j])
            substrings.add(s[i:j])

    return len(substrings)

# Example usage:
input_str = "abc"
print(count_distinct_substrings(input_str))