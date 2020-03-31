# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 20:38:41 2020

@author: ScratcherOfWorld
"""

import urllib.request
import json
import pyautogui
import time
import yaml

time.sleep(0)
project_id = "12785898" #write your project id (numbers in the URL)
end = 1010110101010100234 #when the server will turn off
init_rep = "/C:/Users/" #put your file repertory where the server will stock his data


def limiter_nb_de_str(txt, nb):
    texte = str(txt)
    while len(texte) != nb:
        texte = "0" + texte
    return texte

def get_clouddata():
    page = urllib.request.urlopen('https://clouddata.scratch.mit.edu/logs?projectid=' + project_id + '&limit=40&offset=0')
    page = page.read()
    page = json.loads(page)
    #page = page[item_number]
    return page

def insert_in_enterbox_scratch(string):
    pyautogui.typewrite(string)




















def new_values(value,last):
    list_nouv = []
    nb = 0
    while value[nb] != last:
        list_nouv.insert(0,value[nb])
        nb = nb + 1
    return list_nouv #it retunrns all new values which are in the list after last value seen



def search_init(valeur):
    init_scratchersf = []
    for i in range(len(valeur)):
        if valeur[i]['name'] == "☁ user" and str(valeur[i]['value']) == "1": #warning that's a str
            init_scratchersf.insert(0,valeur[i]['user'])
    return init_scratchersf



def init_scratchers_data(scratchers1001,rep1001):
    data_casiers1001 = open(rep1001 + "data_scratchers.txt", "r")
    dictionary_data_casiers1001 = data_casiers1001.read()
    dictionary_data_casiers1001 = yaml.load(dictionary_data_casiers1001)
    towrite1001 = []

    for i in range(len(scratchers1001)):
        if scratchers1001[i] in dictionary_data_casiers1001.values() == False:
            towrite1001.insert(0,scratchers1001[i])

    data_casiers1001.close()
    data_casiers1001 = open(rep1001 + "data_scratchers.txt", "w").close()
    data_ID1001 = open(rep1001 + "compteur_ID.txt", "r")
    ID1001 = int(data_ID1001.read())
    data_ID1001.close()
    for i in range(len(towrite1001)):
        ID1001 = ID1001 + 1
        dictionary_data_casiers1001[towrite1001[i]] = ID1001    #il faudra définir ID1001
    data_ID1001 = open(rep1001 + "compteur_ID.txt", "w").close()
    data_ID1001 = open(rep1001 + "compteur_ID.txt", "w")
    data_ID1001.write(str(ID1001))
    data_ID1001.close()
    data_casiers1001 = open(rep1001 + "data_scratchers.txt", "w")
    data_casiers1001.write(str(dictionary_data_casiers1001))
    data_casiers1001.close()
    print(dictionary_data_casiers1001)

def get_new_followers(username):
    pass #we have to program it









# /!\ don't forget to create files before
data_casiers = open(init_rep + "data_scratchers.txt", "r")
if data_casiers.read() == "":
    data_casiers.close()
    data_casiers = open(init_rep + "data_scratchers.txt", "w")
    data_casiers.write('{}')
    data_casiers.close()








file_last_value = open(init_rep + "last_value_cloud.txt", "r")
if file_last_value.read() == "":
    last_value_cloud = get_clouddata()[0]
else:
    last_value_cloud = file_last_value.read()

while int(time.time()) < end:
    file_last_value = open(init_rep + "last_value_cloud.txt", "w").close()
    file_last_value = open(init_rep + "last_value_cloud.txt", "w")
    file_last_value.write(str(last_value_cloud)) #we write it in a file for security
    file_last_value.close()
    value = get_clouddata() #get 40 last values of th cloud
    value_nouv = new_values(value,last_value_cloud) #keep new values in the 40 values

    last_value_cloud = value[0]
    init_scratchers = search_init(value_nouv) #get new players
    init_scratchers_data(init_scratchers, init_rep) #new players: we create here their files, you can modify the function
    get_new_followers('GamesKingdom')
    #insert_in_enterbox_scratch(value) #put the value to return to scratch