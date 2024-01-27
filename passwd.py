def pass_wd(USER_FILE_PATH):
    import codecs
    import getpass

    def passwd():
        username = input("Enter username: ").lower()
        current_password = getpass.getpass("Enter current password: ")

    # Check if the user exists and the current password is correct
        with open(USER_FILE_PATH, "r") as file:
            user_lines = [line.strip() for line in file]

        user_found = False
        for i in range(len(user_lines)):
            line = user_lines[i]
            if line.startswith(username + ":"):
                user_found = True
                stored_password = line.split(":")[2]

                if codecs.encode(current_password,"rot_13") == stored_password:
                    new_password = getpass.getpass("Enter new password: ")
                    confirm_password = getpass.getpass("Confirm new password: ")

                # Change password if confirmed
                    if new_password == confirm_password:
                        new_password = codecs.encode(new_password,"rot_13")
                        user_lines[i] = f"{username}:{line.split(':')[1]}:{new_password}"

                        with open(USER_FILE_PATH, "w") as file:
                            file.write("\n".join(user_lines))
                        print("Changed password successfully.")
                    else:
                        print("Error: New passwords do not match.")
                else:
                    print("Error: Incorrect current password.")

        if not user_found:
            print("Error: User not found.")

    passwd()
