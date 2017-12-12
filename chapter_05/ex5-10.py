current_users = ['davis', 'mike', 'jack', 'addison', 'david']
new_users = ['barry', 'mike', 'davis', 'potter', 'john']
for new_user in new_users :
    if new_user.lower() in current_users :
        print("%s : this username is already exist, please try anthoer one." % new_user)
    else :
        print("%s : this username has not been used." % new_user)