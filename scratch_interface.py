import urllib.request
import pyautogui
import data_formatter
import json
import time

time_between_messages = 1

#Type message if the other message has had time to be read.
def server_check_send(server_messages, last_sent_time):
    if len(server_messages)>0:                             #If there are any messages
        if time.time()-last_sent_time>time_between_messages:    #And the specified time has been waited
            pyautogui.typewrite(server_messages[0])
            pyautogui.press('enter')
            del server_messages[0]
            return time.time()
    return last_sent_time

#This ensures a value is not immediatly written then overwritten.
def server_buffer_send(server_messages, user, message_type, string):
    print("To",user,"Body",string)
    server_messages.append(data_formatter.encode(user)+"99"+message_type+string)
    
#Get last 40 changes in cloud data
def get_clouddata(project_id):
    page = urllib.request.urlopen('https://clouddata.scratch.mit.edu/logs?projectid=' + project_id + '&limit=40&offset=0')
    page = page.read()
    page = json.loads(page)
    return page

def get_new_followers(username):
    #We could either look at the profile page or the messages.
    #I think it should be better in the profile page (scratcherofworld)
    pass
