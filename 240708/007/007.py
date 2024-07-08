class Secret:
    def __init__(self,code,location,time):
        self.code = code
        self.location = location
        self.time = time

arr = input().split()
arr[2] = int(arr[2])


secret1 = Secret(arr[0],arr[1],arr[2])

print(f'secret code : {secret1.code}')
print(f'meeting point : {secret1.location}')
print(f'time : {secret1.time}')