# function to get the names of the first person
'''function gets  name, returns a string'''
def getName():
    name= input()
    return name.lower()

# function to calculate love score
'''function takes two arguments, calculates the love score and returns an integer'''
def calcLove(name1,name2):
    # calculate the total instances that characters in the word TRUE appear in both names
    T=name1.count("t") + name2.count("t")
    R=name1.count("r") + name2.count("r")
    U=name1.count("u") + name2.count("u")
    E=name1.count("e") + name2.count("e")
    true_value =T+R+U+E

    # calculate the total instances that characters in the word LOVE appear in both names
    L=name1.count("l") + name2.count("l")
    O=name1.count("o") + name2.count("o")
    V=name1.count("v") + name2.count("v")
    Ee=name1.count("e") + name2.count("e")
    love_value=L+O+V+Ee

    # concatinate true_value and love_value to get the percentage
    percentage =str(true_value)+str(love_value)
    return int(percentage)

if __name__:
    print("please enter your name:")
    firstperson = getName()
    print("please enter your lover's name:")
    secondperson = getName()
    truelove= calcLove(firstperson, secondperson)
    print("Your Love score is: {} % ".format(truelove))