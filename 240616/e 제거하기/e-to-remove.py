string = input()

target = string.find('e')

string = string[:target] + string[target+1:]
print(string)