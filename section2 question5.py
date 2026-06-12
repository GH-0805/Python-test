class AccountLockedError(Exception):
    pass
class Login:
    __password = "python@123"
    __attempts = 3
    def login(self, password):
        if self.__attempts <= 0:
            raise AccountLockedError(
                "Account locked due to multiple failed login attempts"
            )
        if password == self.__password:
            print("Login successful")
            return True
        else:
            self.__attempts -= 1
            print(f"Incorrect password. {self.__attempts} attempts remaining")
            return False
l = Login()
while True:
    p = input("Enter your password: ")
    try:
        if l.login(p):
            break
    except AccountLockedError as e:
        print(e)
        break