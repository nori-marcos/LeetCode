def haystack_contains_needle(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)


print(haystack_contains_needle("hello", "ll"))
