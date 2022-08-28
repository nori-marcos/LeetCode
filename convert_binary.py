dec_num = 35

list_binary = []

if dec_num == 0:
    print(0)

while dec_num > 0:
    remainder = dec_num % 2
    list_binary.append(remainder)
    dec_num = dec_num//2

string_binary = "".join(map(str, list_binary[::-1]))

print(string_binary)