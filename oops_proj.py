class chatbook:

    __user_id = 1
    # This can be accessible through only class

    def __init__(self):
        self.__name = "Default User"
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
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

    # Getter

    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to chatbook !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to Message a friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email id -> ")
        password = input("Enter your password here -> ")
        self.username = email
        self.password = password
        print("You have signed up successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup by pressing 1")
        else:
            uname = input("Please enter your email id -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Please enter correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here : ")
            print(f"Following content has been posted : {txt}")
        else:
            print("You need to signin 1st to post something")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin == True:
            txt = input("Enter your message here to friend : ")
            frnd = input("Whom to send this message : ")
            print(f"Following message has been sent : {txt} to {frnd}")
        else:
            print("You need to signin 1st to post something")
        print("\n")
        self.menu()


# user1 = chatbook()
# # user 1 is a object

# sam = chatbook()

# sam.menu()


# Adding a new attribute

# sam.name = "Sam Kumar"
# print(sam.name)
