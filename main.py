# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:38:41 2020

@authors: ScratcherOfWorld and Jimmyrooster
"""
import file_manager
import scratch_interface
import action_functions
import data_formatter
import data_formatter
import time

time.sleep(0)
#https://scratch.mit.edu/projects/381246958/ (my test project for this - just input numbers)
project_id = "381246958" #Write your project id (numbers in the URL)
end = 1010110101010100234 #When the server will turn off (in seconds)
last_sent_time = 0
init_rep = "C:/ProgramData/KingsDefenseServer/" #Put your file repertory where the server will stock its data

def tick_server(last_values_cloud, users):
    value = scratch_interface.get_clouddata(project_id) # Get 40 last values of the cloud
    new_values = data_formatter.get_new_values(value,last_values_cloud) # Get new activity.
    
    #If there is actually any new activity
    if len(new_values)>0: 
        action_functions.actions(new_values, users) #Perform actions based on any activity
        last_values_cloud = value
        file_manager.save_files(init_rep, last_values_cloud, users)
    
    #get_new_followers('GamesKingdom')
    return (last_values_cloud, users)


(last_values_cloud, users) = file_manager.setup_files(init_rep)
while int(time.time()) < end:
    (last_values_cloud, users)=tick_server(last_values_cloud, users)
    last_sent_time = scratch_interface.server_check_send(last_sent_time)
