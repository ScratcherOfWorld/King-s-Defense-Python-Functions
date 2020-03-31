import player_data
#Finds the index of the user data object with the specified username. Returns none on failiure.
def get_user(username, users):
    match = [index for index in range(len(users)) if users[index].username == username]
    if len(match)==0:
        return None
    else:
        return match[0]

#Perform actions based on the new requests
def actions(activities, users):
    for activity in activities:
        if activity['name'] == "☁ user" and activity['verb']=="set_var":#If it is actually a request
            user_index=get_user(activity['user'], users)
            print(activity)
            #New user
            if(user_index==None):
                print("New user: "+activity['user'])
                user_index = len(users)
                users.append(player_data.PlayerStaticData(activity['user']))
            else:
                users[user_index].gems+=1 #Add one gem every time you log in. (only temporery)

            pass #We call functions for all the requests here based on the first digit of the value.
