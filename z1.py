s = input("Введите строку: ")

def compress(string):
    string += " " #для обработки последнего символа без доп. условий
    res = []
    counter = 0

    for sym in range(0, len(string)):
        if sym == 0:
            counter += 1
            continue
        else:
            if string[sym] == string[sym-1]:
                counter += 1
            else:
                res.append(string[sym-1])
                if(counter != 1): res.append(str(counter))
                counter = 1

    return ''.join(res)

print(compress(s))
