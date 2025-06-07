class chatbook:

    __user_id = 100

    def __init__(self):
        self.id = f"ABC{chatbook.__user_id}"
        chatbook.__user_id += 1
        self.__name = "Default User"
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value
        return chatbook.__user_id    

    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to Chatbook!! How would you like to proceed?
                        1. Press 1 to signup
                        2. Press 2 to signin
                        3. Press 3 to write a post
                        4. Press 4 to message a friend
                        5. Press any other key to exit 
                           
                           Enter your input: """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Enter your password: ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully!!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first")
        else:
            uname = input("Enter your email/username: ")
            pwd = input("Enter your password: ")

            if self.username == uname and self.password == pwd:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Provide correct credentials..!!")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here: ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something...!")
            print('\n')
            self.menu()
    
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here: ")
            frnd = input("Whom to send msg? ")
            print(f"your msg has been sent to {frnd}")
        else:
            print("You need to signin first to post something...!")
            print('\n')
            self.menu()