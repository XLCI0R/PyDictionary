from difflib import get_close_matches

def getDef(inputt, words):
    word = inputt.lower()

    if word in words:
        for i in words[word]:
            print(i)
    
    elif len(get_close_matches(word, words.keys())) > 0:
        alt = input("Did you mean {} instead?(Y/N)".format(get_close_matches(word, words.keys())[0]))

        if alt == "Y" or alt == "y":
            for i in words[get_close_matches(word, words.keys())[0]]:
                print(i)

        elif alt == "N" or alt == "n":
            print("Your word doesn't exist bruh")

        else:
            print("What? Can't you read?\nEnter Y if yes, N if no.\nDumbass")

