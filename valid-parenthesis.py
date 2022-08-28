def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False

stack = []
is_balanced = True

string = "(]"

chars = list(string)

for i, char in enumerate(chars):
    if char in "{[(":
        stack.append(char)
    else:
        if len(stack) == 0:
            is_balanced = False
            break
        else:
            top = stack.pop()
            if not is_match(top, char):
                is_balanced = False
                break

if len(stack) == 0 and is_balanced:
    print(True)
else:
    print(False)