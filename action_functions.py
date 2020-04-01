import player_data
import scratch_interface


def get_point_values(users, user_index, activity):
    print("Implemented get point values for: ",users[user_index])
    scratch_interface.server_send(activity['user'],users[user_index].get_values())

def start_pairing(users, user_index, activity):
    pass

def end_pairing(users, user_index, activity):
    pass

def buy_card(users, user_index, activity):
    pass

def send_message(users, user_index, activity):
    pass

def get_message_with_index(users, user_index, activity):
    pass

def get_message_count(users, user_index, activity):
    pass
    
actions_on_recieve = {
    0: get_point_values,
    1: start_pairing,
    2: end_pairing,
    3: buy_card,
    4: send_message,
    5: get_message_with_index,
    6: get_message_count
}

#Finds the index of the user data object with the specified username. Returns none on failiure.
def try_get_user(username, users):
    match = [index for index in range(len(users)) if users[index].username == username]
    if len(match)==0:
        return None
    else:
        return match[0]

def get_user(activity, users):
    user_index=try_get_user(activity['user'], users)
    print(activity)
    #New user
    if(user_index==None):
        print("New user: "+activity['user'])
        user_index = len(users)
        users.append(player_data.PlayerStaticData(activity['user']))
    else:
        users[user_index].gems+=1 #Add one gem every time you play. (only temporery)
    return user_index

#Perform actions based on the new requests
def actions(activities, users):
    for activity in activities:
        if activity['name'] == "☁ user" and activity['verb']=="set_var":#If it is actually a request
            user_index = get_user(activity, users)
            request = activity['value'][0]
            #We find functions the function here based on the first digit of the value.
            func = actions_on_recieve.get(int(request))
            if func==None:
                raise Exception("Error when handling request, the specified action was not found. This should never happen. Request: ",activity)
            func (users, user_index, activity) #Call the function
