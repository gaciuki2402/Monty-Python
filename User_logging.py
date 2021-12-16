import base64
import os
import pathlib


class Authenticator(object):
    def __init__(self,users={}):
        self.users = users

    def login(self):
        self.attempt_username = input("Username2:")
        self.attempt_password = input("Password2:")
        self.encodedAttemptPassword = base64.b64encode(self.attempt_password.encode())
        self.decodedAttemptPassword = self.encodedAttemptPassword.decode('utf-8')
        print(self.decodedAttemptPassword)
        isLoggedIn = False
        if self.attempt_username in self.users:
            self.encodedPassword = base64.b64encode(self.users[self.attempt_username].encode())
            self.decodedPassword = self.encodedPassword.decode('utf-8')
            print(self.decodedPassword)
            if self.decodedPassword == self.decodedAttemptPassword:
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
        isLoggedIn = False
        while not isLoggedIn:
            login = self.login()
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
