# def get_square_root(x: int) -> int:
#     if x < 2:
#         return x
#
#     l = 2
#     r = x // 2
#     while l <= r:
#         mid = (l + r) // 2
#         sqr = mid * mid
#
#         if sqr > x:
#             r = mid - 1
#         elif sqr < x:
#             l = mid + 1
#         else:
#             return mid
#
#     return r
#
#
# print(get_square_root(9))

def get_square_root(x: int) -> int:
    if x < 0:
        return x

    start = 1
    end = x
    answer = 0

    while start <= end:

        mid = start + (end - start) // 2

        if mid * mid <= x:
            answer = mid    # the power two is already lower than x, so it is maybe the answer, but even though we try one more
            start = mid + 1  # we move one number to the right, because mid was already checked.

        else:
            end = mid - 1  # we move one number to the left, because mid was already checked.

    return answer

print(get_square_root(4))
