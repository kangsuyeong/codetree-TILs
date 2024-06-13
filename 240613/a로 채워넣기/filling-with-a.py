string=input()

list_string=list(string)

list_string[1]='a'
list_string[len(list_string)-2]='a'
s=''.join(list_string)
print(s)