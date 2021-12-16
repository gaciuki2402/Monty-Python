import base64
import os
import pathlib


class Authenticator(object):
    def __init__(self,users={}):
        self.users = users

    def add_user(self):
        self.username = input("Username:")
        self.password = input("password:")
        if self.username in self.users:
            raise ValueError("username already exists!")
        if len(self.password) < 6:
            raise ValueError("Password must be more than 6 values!")
        return True

    def login(self):
        self.attempt_username = input("Username2:")
        self.attempt_password = input("Password2:")
        isLoggedIn = False
        if self.attempt_username in self.users:
            if self.users[self.attempt_username] == self.attempt_password:
                print("Login Successful")
                self.Shop()
                isLoggedIn = True
            else:
                print("Invalid Password")
                isLoggedIn = False
        else:
            print("Invalid Username")
            isLoggedIn = False

    def Shop(self):
        print("Welcome to Gaciuki general shop.")
        print("""
        Bread: Ksh.50\n
        Milk: Ksh. 30 per litre\n
        """)

    def Logic(self):
        account = eval(input("Enter 1 to create account and 2 to login:"))
        isLoggedIn = False
        while not isLoggedIn:
            if account == 1:
                add_user = self.add_user()
                if add_user == True:
                    login = self.login()
                    break
            elif account == 2:
                login = self.login()
                break
            else:
                print("Invalid Choice")
                break


if __name__ == "__main__":
    auth = Authenticator({
        "grace": "password1234",
        "irene":"keepcalm1234",
        "admin":"admin1234"

        })
    auth.Logic()

#
# class Authorization(Authenticator):
#
#     def __init__(self):
#
#     def encryptPassword(self):
#         self.encodedPassword=base64.b64encode(self.password.encode())
#         self.decodedPassword=self.encodedPassword.decode('utf-8')
#
#     def login(self):
#         isLoggedIn=False
#         print("Welcome back,\n Please login to continue.")
#         while not isLoggedIn:
#             self.attempt_username=input("Username:")
#             self.attempt_password=input("Password:")
#             self.encodedAttemptPassword=base64.b64encode(self.attempt_password.encode())
#             self.decodedAttemptPassword=self.encodedAttemptPassword.decode('utf-8')
#             loginPassword=base64.b64decode(self.decodedPassword)
#             attempt_password2=base64.b64decode(self.decodedAttemptPassword)
#             try:
#                 if self.username==self.attempt_username and loginPassword==attempt_password2:
#                     print(f"Welcome to freemob...\nYour username is {self.username}")
#                     isLoggedIn=True
#                 else:
#                     print("Wrong Password username")
#             except:
#                 raise ValueError
#             finally:
#                 pass
# if __name__=="__main__":
#     user1=Authorization("Grace","password")
#     user1.encryptPassword()
#     user1.login()
