# detect a capital character in string
# .................................................. Main Fucntion
def detect_capital(string):
    temp = []
    output = None
    punc = ["!"]
    for character in string:
        capital = character.upper()
        if character == character.upper():
            temp.append(character)

    temp = "".join(temp)
    temp = temp.replace(" ","")

    for char in temp:

        if char.upper() not in temp:
            output = "there are no capital letters in\t{}".format(string)

        elif char.upper() in temp:
            output = "string\t{}\ncapital(s)\t{},'{}'".format(string,len(temp),temp)

    print(output)
    return output
# .................................................. On Run
if __name__ == "__main__":
    while True:
        string = str(input("enter a string: "))
        detect_capital(string)

        exit = input("do you want to exit? (y)es or (n)o?: ")
        if exit == "y":
            print("goodbye")
            break
            exit
        else:
            continue
# .................................................. Bugs / Issues
"""
The loop on line 15 is not 100% correct.

When there are no capital letters,

program yields this error:

"output referenced before assignment"

* fixed partially by setting output = None (line 5)
"""

"""
Program recognizing punctuation as a capital

How to fix this ? ? ? 

"""
