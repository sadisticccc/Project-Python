def del_user(USER_FILE_PATH):
    import codecs
    import getpass

    def deluser():
        username = input("Enter username to delete: ").lower()

        # Remove user if found
        with open(USER_FILE_PATH, "r") as file:
            user_lines = [line.strip() for line in file]
        
        new_user_lines = [line for line in user_lines if not line.startswith(username + ":")]

        if len(new_user_lines) == len(user_lines):
            print("No user found with the given username.")
        else:
            with open(USER_FILE_PATH, "w") as file:
                file.write("\n".join(new_user_lines))
            print("User deleted successfully.")

    deluser()        