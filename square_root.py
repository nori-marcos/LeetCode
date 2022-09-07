def get_square_root(x: int) -> int:
    number = 0
    counter = 0

    while number <= x:

        number = counter * counter

        if number >= x:
            break

        counter += 1

    if counter * counter > x:
        return counter - 1

    else:
        return counter


print(get_square_root(9))
