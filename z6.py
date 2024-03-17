s = input("Введите строку: ")

def abbr(string):
    letters = []
    for i in range(0, len(string)):
        if i == 0: letters.append(string[i].upper())
        else:
            if string[i] == ' ': letters.append(string[i+1].upper())
    return "".join(letters)

print(abbr(s))
