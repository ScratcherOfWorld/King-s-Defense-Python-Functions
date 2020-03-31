#Used for formating send paramaters.
def make_text_set_length(text, length):
    if len(text)>length:
        raise Exception('Text: '+text+' cannot be made '+str(length)+'long')
    modified_text = str(text)
    while len(text) < length:
        modified_text = "0" + modified_text
    return modified_text

#Out of the 40 values scratch shows, find the new ones.
def get_new_values(new_value,last):
    list_new = []
    for new_item in new_value:
        if not new_item in last:
            list_new.append(new_item)
    list_new.reverse()#oldest updates first.
    return list_new
