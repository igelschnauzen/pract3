s = input("Введите строку: ")

def decompress(string):
    string += " "
    result = []

    for i in range(0, len(string)):
        if string[i] == " ": break
        if string[i].isdigit():
            result.append(string[i-1] * int(string[i]))
        else:
            if not(string[i+1].isdigit()):
                result.append(string[i])
    return ''.join(result)

print(decompress(s))
