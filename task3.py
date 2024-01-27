import sys
import adduser, deluser, passwd, login

# File path to store user information
# USER_FILE_PATH = "passwd.txt"
USER_FILE_PATH = sys.argv[1]


while True:
    menu = input("\n1) Add User:\n2) Delete User:\n3) Change Password:\n4) Login: \n")
    if menu == '1':
        adduser.add_user(USER_FILE_PATH)
    elif menu == '2':
        deluser.del_user(USER_FILE_PATH)
    elif menu == '3':
        passwd.pass_wd(USER_FILE_PATH)
    elif menu == '4':
        login.log_in(USER_FILE_PATH)
    else:
        print("\nInvalid input!!")

    further = input("Do you want to continue?(YES/NO)")
    if further.upper()!= "YES" and further.upper() != "Y":
        break


