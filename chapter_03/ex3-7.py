invitation_list = ["Bob", "Michael", "Eric", "Alex"]
print("Invitaion system up...")
print(invitation_list[0] + " has been invited.")
print(invitation_list[1] + " has been invited.")
print(invitation_list[2] + " has been invited.")
print(invitation_list[3] + " has been invited.")
print("Whoops, " + invitation_list[1] + " cannot arrive in time.")
print("We have invited Rechard instead.")
invitation_list.remove(invitation_list[1])
invitation_list.insert(1, "Rechard")
print(invitation_list[0] + " has been invited.")
print(invitation_list[1] + " has been invited.")
print(invitation_list[2] + " has been invited.")
print(invitation_list[3] + " has been invited.")
print("Done!")

# ==================================================================

print("Here will come a bigger table...")
print("We just can invite three more people...")
print("Inviting...")
invitation_list.insert(0, "Johnson")
invitation_list.insert(int(len(invitation_list) / 2), "Mikey")
invitation_list.append("Jordan")
print(invitation_list[0] + " has been invited.")
print(invitation_list[1] + " has been invited.")
print(invitation_list[2] + " has been invited.")
print(invitation_list[3] + " has been invited.")
print(invitation_list[4] + " has been invited.")
print(invitation_list[5] + " has been invited.")
print(invitation_list[6] + " has been invited.")
print("Done!")

# ==================================================================

print("Ooops, the table cannot be here soon...")
print("Canceling the invitations...")
while (len(invitation_list) > 2) :
    print("Sorry to infrom you Mr." + invitation_list.pop() + ", the invitation is canceled.")
print(invitation_list[0] + " has been invited.")
print(invitation_list[1] + " has been invited.")
del invitation_list[0]
del invitation_list[0] # 当元素被删除之后，列表的秩会被重置
print(invitation_list)