# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:38:41 2020

@author: ScratcherOfWorld and Jimmyrooster
"""
import urllib.request
import json
import pyautogui
import time
import ast
import os
from os import path
import yaml

time.sleep(0)
#https://scratch.mit.edu/projects/381246958/ (my test project for this - just input numbers)
project_id = "381246958" #write your project id (numbers in the URL)
end = 1010110101010100234 #when the server will turn off (in seconds)
init_rep = "C:/ProgramData/KingsDefenseServer/" #put your file repertory where the server will stock its data

#Used for formating send paramaters.
def make_text_set_length(text, length):
    if len(text)>length:
        raise Exception('Text: '+text+' cannot be made '+str(length)+'long')
    modified_text = str(text)
    while len(text) < length:
        modified_text = "0" + modified_text
    return modified_text

#Get last 40 changes in cloud data
def get_clouddata():
    page = urllib.request.urlopen('https://clouddata.scratch.mit.edu/logs?projectid=' + project_id + '&limit=40&offset=0')
    page = page.read()
    page = json.loads(page)
    return page

#Type message
def insert_in_enterbox_scratch(string):
    pyautogui.typewrite(string)

#Out of the 40 values scratch shows, find the new ones.
def get_new_values(new_value,last):
    list_new = []
    for new_item in new_value:
        if not new_item in last:
            list_new.append(new_item)
    list_new.reverse()#oldest updates first.
    return list_new

#Perform actions based on the new requests
def actions(activities):
    for activity in activities:
        if activity['name'] == "☁ user" and activity['verb']=="set_var":#If it is actually a request
            pass #We call functions for all the requests here based on the first digit of the value.

def init_scratchers_data(scratchers1001,rep1001):
    #What is this?
    data_casiers1001 = open(rep1001 + "data_scratchers.txt", "r")
    dictionary_data_casiers1001 = data_casiers1001.read()
    dictionary_data_casiers1001 = yaml.load(dictionary_data_casiers1001, Loader=yaml.FullLoader)
    towrite1001 = []

    for i in range(len(scratchers1001)):
        if scratchers1001[i] in dictionary_data_casiers1001.values() == False:
            towrite1001.insert(0,scratchers1001[i])

    data_casiers1001.close()
    data_casiers1001 = open(rep1001 + "data_scratchers.txt", "w").close()
    data_ID1001 = open(rep1001 + "computer_ID.txt", "r")
    ID1001=0
    try:
        if len(data_ID1001.read())>2:
            ID1001 = int(data_ID1001.read())
    except ValueError:
        raise Exception("data: |"+data_ID1001.read()+"| could not be made into int.")
    data_ID1001.close()
    for i in range(len(towrite1001)):
        ID1001 = ID1001 + 1
        dictionary_data_casiers1001[towrite1001[i]] = ID1001    #What should ID1001 do?
    data_ID1001 = open(rep1001 + "computer_ID.txt", "w").close()
    data_ID1001 = open(rep1001 + "computer_ID.txt", "w")
    data_ID1001.write(str(ID1001))
    data_ID1001.close()
    data_casiers1001 = open(rep1001 + "data_scratchers.txt", "w")
    data_casiers1001.write(str(dictionary_data_casiers1001))
    data_casiers1001.close()
    print("Data dictionary: ",dictionary_data_casiers1001)

def get_new_followers(username):
    #We could either look at the profile page or the messages.
    pass

#Unused What is this?
def save_scratcher_data():
    data_casiers = open(init_rep + "data_scratchers.txt", "r")
    if data_casiers.read() == "":
        data_casiers.close()
        data_casiers = open(init_rep + "data_scratchers.txt", "w")
        data_casiers.write('{}')
        data_casiers.close()

#Creates new directories and files if necessary
def create_files():
    if not path.exists(init_rep):
        os.makedirs(init_rep)
    
    for filename in ["data_scratchers.txt", "last_value_cloud.txt", "computer_ID.txt"]:
        f= open(init_rep + filename,"a+")
        f.close()

def setup_files():
    create_files()

    file_last_value = open(init_rep + "last_value_cloud.txt", "r")
    last_values_read=file_last_value.read()
    file_last_value.close()
    
    if last_values_read == "":
        #It is new so we assume it hasn't read anything
        last_values_cloud = [{}]
    else:
        #Recover read data from file
        last_values_cloud = last_values_read.replace('?','☁')
        last_values_cloud = ast.literal_eval(last_values_cloud)
    return last_values_cloud

def remove_cloud_symbols(string):
    return string.replace('☁', '?')

def tick_server(last_values_cloud):
    file_last_value = open(init_rep + "last_value_cloud.txt", "w")
    file_last_value.write(remove_cloud_symbols(str(last_values_cloud))) #We write the last data recieved to a file for security
    file_last_value.close()
    
    value = get_clouddata() #get 40 last values of the cloud
    new_values = get_new_values(value,last_values_cloud) #keep new values in the 40 values
    
    if len(new_values)>0:
        print(new_values) #Log any activity if there is any
        actions(new_values) #Perform actions based on any activity

    last_values_cloud = value
    #init_scratchers = search_init(new_values) #get new players
    #init_scratchers_data(init_scratchers, init_rep) #new players: we create here their files, you can modify the function
    #get_new_followers('GamesKingdom')
    #insert_in_enterbox_scratch(value) #put the value to return to scratch
    return last_values_cloud

last_values_cloud=setup_files()

while int(time.time()) < end:
    last_values_cloud=tick_server(last_values_cloud)
