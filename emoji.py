# meassage = input("Enter Youre message : ")
# meassage = meassage.lower()
# modified_meassage = ""
# if "sad" in meassage:
#    modified_meassage= meassage.replace("sad","😿")
# elif "happy" in meassage:
#    modified_meassage= meassage.replace("happy","😊")
# elif "angry" in meassage:
#    modified_meassage= meassage.replace("angry","😡")
# elif "love" in meassage:
#    modified_meassage= meassage.replace("love","😍")

# print(modified_meassage) 

emoji_sets = {
        "sad": "😿",
        "happy": "😊",
        "angry": "😡",
        "love": "😍"
    }

choice = True
while choice:
    message = input("Enter your message: ")
    message = message.lower()
    modified_message = message

    for word, emoji in emoji_sets.items():
        if word in modified_message:
            modified_message=modified_message.replace(word, emoji)

    print(modified_message)
    option = input("Do you want to countinue (Y/N) : ")
    option = option.upper()
    if option=="N":
        choice = False

