class User:

    users_data = []

    def __init__(self, username, account_type, passowrd):

        self.username = username
        self.acccount_type = account_type
        self.password = passowrd

    def register(self):

        data = {
            "username": self.username,
            "account_type": self.acccount_type,
            "password": self.password
        }

        User.users_data.append(data)
        print("Registered successfully")


class Student(User):
    pass

class Professor(User):
    pass

class Admin(User):
    pass


while True:
    print("----Welcome to university management system----")
    print("----Choose an action----")
    print("1. Register")
    print("2. Login")
    print("3. Exit")


    choice = int(input("Enter your choice: "))

    if choice == 3 or choice == "3":
        break


    if choice == 1 or choice == "1":

        username = input("Enter username: ")
        account_type = input("Enter account type, eg: Admin, Student, Professor: ")
        password = input("Enter password: ")

        # If username already exist 

        user = User(username, account_type, password)

        if user:
            user.register()

        print(User.users_data)




