import urllib.request
import pyautogui
import data_formatter
import json
#Type message
def server_send(user, string):
    print("To",user,"Body",string)
    pyautogui.typewrite(data_formatter.encode(user)+"99"+string)
    pyautogui.press('enter')

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
