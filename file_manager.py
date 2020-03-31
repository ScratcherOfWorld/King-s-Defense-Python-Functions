import os
import ast
from os import path
import player_data

#Creates new directories and files if necessary
def create_files(init_rep):
    if not path.exists(init_rep):
        os.makedirs(init_rep)
    
    for filename in ["data_scratchers.txt", "last_value_cloud.txt"]:
        f= open(init_rep + filename,"a+")
        f.close()

def read_file(file_path, clouds_are_questions):
    file = open(file_path, "r")
    file_read=file.read()
    file.close()
    
    if file_read == "":
        #It is new so we assume it hasn't read anything
        extracted = []
    else:
        #Recover read data from file
        extracted = file_read.replace('?','☁')
        extracted = ast.literal_eval(extracted)
    return extracted

def setup_files(init_rep):
    create_files(init_rep)
    last_values_cloud = read_file(init_rep+"last_value_cloud.txt", True)
    dict_users = read_file(init_rep+"data_scratchers.txt", False)
    users = [player_data.PlayerStaticData("") for user in dict_users]
    for user_index in range (len(users)):
        users[user_index].from_dict(dict_users[user_index])
    print(users)
    return (last_values_cloud, users)

def save_files(init_rep, last_values_cloud, users):
    file_last_value = open(init_rep + "last_value_cloud.txt", "w")
    file_last_value.write(remove_cloud_symbols(str(last_values_cloud))) #We write the last data recieved to a file for security
    file_last_value.close()

    #Save user data
    file_users = open(init_rep + "data_scratchers.txt", "w")
    file_users.write(remove_cloud_symbols(str([data.get_dict() for data in users]))) #Write the player data to a file
    file_users.close()

#The cloud symbol can't be encoded on my computer.
def remove_cloud_symbols(string):
    return string.replace('☁', '?')
    
