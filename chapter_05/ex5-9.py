usernames = []
if usernames :
    for username in usernames :
        if username == 'admin' :
            print("Hello admin, would you like to see a status report?")
        else :
            print("Hello %s, thank you for logging in again." % username)
else :
    print("We need to find some users!")