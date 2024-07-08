class User:
    def __init__(self,user_id,user_LV):
        self.user_id=user_id
        self.user_LV=user_LV
    def user_print(self):
        print(f'user {self.user_id} lv {self.user_LV}')

user_id, user_LV = input().split()
user1 = User("codetree",10)
user1.user_print()
user2 = User(user_id,int(user_LV))
user2.user_print()