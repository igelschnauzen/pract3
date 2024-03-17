inp = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']

repeats = {

}

for string in inp:
    if string in repeats: repeats[string] += 1
    else: repeats[string] = 1

for key in repeats:
    print(repeats[key], end=" ")
print("")
