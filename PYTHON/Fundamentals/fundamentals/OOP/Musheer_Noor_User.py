class User:
    def __init__(self, first_name, last_name, email, age,):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_into(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Not enough points.")
        else:
            self.gold_card_points = self.gold_card_points - amount



new_user1 = User("John", "Doe", "JD@aol.com", 30)
new_user1.display_into()

new_user2 = User("Ada", "Smith", "ASmith@yahoo.com", 40)
new_user3 = User("Jeremy", "Turk", "JT123@Gmail.com", 20)

new_user1.spend_points(50)
new_user2.enroll()
new_user2.spend_points(80)

new_user1.display_into()
new_user2.display_into()
new_user3.display_into()

new_user1.enroll()
new_user3.spend_points(40)
