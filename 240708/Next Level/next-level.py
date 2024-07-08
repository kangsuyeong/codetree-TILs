class User:
    def __init__(self,user_id="",user_LV=0):
        self.user_id=user_id
        self.user_LV=user_LV
    def user_print(self):
        print(f'user {self.user_id} lv {self.user_LV}')

user1 = User()
user2 = User()

user1.user_id="codetree"
user1.user_LV=10
user_id, user_LV = input().split()
user2.user_id=user_id
user2.user_LV=user_LV

user1.user_print()

user2.user_print()