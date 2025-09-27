class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook !! How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to write a post
                           4. Press 4 to Message a friend
                           5. Press any other key to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.postmessage()
        elif user_input == "4":
            pass
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
                print("Sign in done")
            else:
                print("Please enter correct credentials")
        print("\n")
        print("Sign in part 2 done")
        self.menu()

    # def postmessage(self):
    #     print("\n")
    #     inp = input("Hi type your good name here : ")
    #     print(f"{inp} nice to meet you")
    #     print("\n")
    #     self.menu

    # def msgtofrnd():


obj = chatbook()
