class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, "Rista")
user_2 = User(2, "Fakhri")

print("\nName : " + user_1.user_name)
print("Following :", user_1.following)
print("Followers :", user_1.followers)
print("=")
print("Name : " + user_2.user_name)
print("Following :", user_1.following)
print("Followers :", user_2.followers)

user_1.follow(user_2)

print("\nName : " + user_1.user_name)
print("Following :", user_1.following)
print("Followers :", user_1.followers)
print("=")
print("Name : " + user_2.user_name)
print("Following :", user_2.following)
print("Followers :", user_2.followers)
