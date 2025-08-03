def count_words(text):
    text_list = text.split()
    num_words = len(text_list)
    return num_words

def count_characters(text):
    char_dict = {}
    for char in text:
        chal = char.lower()
        if chal in char_dict:
            char_dict[chal] += 1
        else:
            char_dict[chal]= 1
    
    return char_dict

def sort_dict(dict):
    dict_list = []

    for char, count in dict.items():
        if char.isalpha():
            new_dict = {'char': char, 'num': count}
            dict_list.append(new_dict)
    
    print(dict_list)
    return dict_list

