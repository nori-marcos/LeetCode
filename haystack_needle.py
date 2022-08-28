def haystack_contains_needle(haystack, needle):

    def contains_needle(needle_input, check):

        if len(needle_input) > len(check):
            return False

        count = 0

        while count < len(needle_input):
            if needle_input[count] != check[count]:
                return False
            else:
                count += 1

        return True

    trigger = needle[0]

    for i in range(len(haystack)):

        if haystack[i] == trigger and contains_needle(needle, haystack[i:]):
            return i

    if len(haystack) == 0:
        return 0

    return -1


print(haystack_contains_needle("hello", "ll"))
