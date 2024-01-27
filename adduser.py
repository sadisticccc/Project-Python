def add_user(USER_FILE_PATH):
    import codecs
    import getpass

    def adduser():

        username = input("Enter username: ").lower()
        real_name = input("Enter real name: ")
        password = getpass.getpass("Enter password: ")

        # Check if username already exists
        with open(USER_FILE_PATH, "r") as file:
            user_lines=[line.strip() for line in file]
        
        for line in user_lines:
            if line.startswith(username + ":"):
                print("Error: Username already exists.")
                return

        # Add new user
        encrypted_password = codecs.encode(password,"rot_13")
        user_lines.append(f"{username}:{real_name}:{encrypted_password}")

        with open(USER_FILE_PATH, "w") as file:
            file.write("\n".join(user_lines))

        print("User added successfully.")
    
    adduser()