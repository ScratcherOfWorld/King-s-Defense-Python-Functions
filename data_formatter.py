characters = list('''abcdefghijklmnopqrstuvwxyz1234567890`~!@#$%^&*()_+-=][{}|\:";'<>?,./ ôöóœøõèéêëēàáâäæãāûüùúūîíìçñ€£''')

#Used for formating send paramaters.
def make_text_set_length(text, length):
    if len(text)>length:
        raise Exception('Text: '+text+' cannot be made '+str(length)+'long')
    modified_text = str(text)
    while len(modified_text) < length:
        modified_text = "0" + modified_text
    return modified_text

#Convert string to decimal
def encode(string):
    string = string.lower() #Fix error because capital letters for usernames are not in the list
    return ''.join([make_text_set_length(str(characters.index(character)),2) for character in string])

#Decimal to string
def decode(string):
    return ''.join([characters[int(string[index]+string[index+1])] for index in range(0,len(string),2)])

#Out of the 40 values scratch shows, find the new ones.
def get_new_values(new_value,last):
    list_new = []
    for new_item in new_value:
        if not new_item in last:
            list_new.append(new_item)
    list_new.reverse()#oldest updates first.
    return list_new
