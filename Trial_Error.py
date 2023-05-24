w_name = ""
class CheckName:
    def __init__(self, name):
        self.name = name
    def check_name(self):
        def recheck(self):
            self.name = CheckName(input())
            self.name.check_name()

        if not self.name:
            print("Sorry I receive nothing. Would you please type in again?")
            recheck(self)
        elif len(self.name) > 10:
            print("The name shall be less than 10 letters. Please input again.")
            recheck(self)
        elif not self.name.isalpha():
            print("The name shall contain letters only. Please input again.")
            recheck(self)
        else:
            global w_name
            w_name += self.name + " "

#Beginning
first_name = CheckName(input("Welcome!\nWhat is your first name? "))
first_name.check_name()
last_name = CheckName(input("How about your last name? "))
last_name.check_name()
print(f"Thanks {w_name.title()}!")
#Ask for age
