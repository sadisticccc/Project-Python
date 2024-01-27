def log_in(USER_FILE_PATH):
    import codecs
    import getpass

    def login():
        username = input("Enter username: ").lower()
        password = getpass.getpass("Enter password: ")

        # Check if the user exists and the password is correct
        with open(USER_FILE_PATH, "r") as file:
            user_lines = [line.strip() for line in file]

        for line in user_lines:
            if line.startswith(username + ":"):
                stored_password = line.split(":")[2]
                if codecs.encode(password,"rot_13") == stored_password:
                    print("Login successful.")
                else:
                    print("Error: Incorrect password.")
                return

        print("Error: User not found.")
    
    login()