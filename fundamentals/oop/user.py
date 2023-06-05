class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
        self.info = [
            self.first_name, 
            self.last_name, 
            self.email,
            self.age
        ]

        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        for info in self.info:
            print(info)
    
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self.is_rewards_member

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("You have insufficient gold card points")
        else:
            self.gold_card_points -= amount

user1 = User("John", "Smith", "john.smith@email.com", 28)
user1.display_info()

user2 = User("Luke", "James", "luke.james@email.com", 41)
user3 = User("Pat", "Robinson", "pat.robinson@email.com", 19)

user2.spend_points(50)

user3.enroll()
user3.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

user2.enroll()
user2.enroll()

user3.spend_points(200)
