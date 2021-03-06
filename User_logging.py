import base64

class Authenticator(object):
    def __init__(self,users={}):
        self.users = users

    def login(self):
        print("Welcome back,")
        self.attempt_username = input("Username2:")
        self.attempt_password = input("Password2:")
        self.encodedAttemptPassword = base64.b64encode(self.attempt_password.encode())
        self.decodedAttemptPassword = self.encodedAttemptPassword.decode('utf-8')
        self.isLoggedIn = False
        if self.attempt_username in self.users:
            self.encodedPassword = base64.b64encode(self.users[self.attempt_username].encode())
            self.decodedPassword = self.encodedPassword.decode('utf-8')
            if self.decodedPassword == self.decodedAttemptPassword:
                print("Login Successful")
                self.Shop()
                self.isLoggedIn = True
            else:
                print("Invalid Credentials.")
                self.isLoggedIn = False
        else:
            print("Invalid Credentials.")
            self.isLoggedIn = False

    def Shop(self):
        print("Welcome to Gaciuki general shop.")
        print("""
        Bread: Ksh.50\n
        Milk: Ksh. 30 per litre\n
        """)

    def Logic(self):
        isLoggedIn = False
        attempts=3
        while not isLoggedIn:
            login = self.login()
            if self.isLoggedIn==False:
                if attempts==1:
                    break
                attempts-=1
                print(f"Please try again {attempts} attempt remaining")
            else:
                break
if __name__ == "__main__":
    auth = Authenticator({
        "grace": "password1234",
        "irene":"keepcalm1234",
        "admin":"admin1234",

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
