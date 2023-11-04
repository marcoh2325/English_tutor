"""Store words and their translation to another language"""

def print_dict(_dict_to_print):
    for k,v in _dict_to_print.items():
        print(f"{k}: {v}")

def store_dict(_dict_to_store, _option):
    """Store the introduced words as a json or csv"""
    pass

def main():
    finish = True
    translations = dict()

    while(finish):
        word = input("Enter word")
        word_translation = input("Enter translation")
        translations[word] = word_translation
        finish = input("Was that your last word? y/n\n")
        if("y" == finish.lower()):
            finish = True
        elif("n" != finish.lower()):
            print("Please introduce y for yes and n for no")
    
    print_dict(translations)

if (__name__ == "__main__"):
    main()




