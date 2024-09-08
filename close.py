from random import *

members = input("how much members are you?")
if not members.isdigit():
    print("input error")
elif int(members) < 4 or int(members) > 15:
    print("number of canadists is not in range")

else:
    vote1 = input("how much people gonna vote?")
    if vote1.isdigit() and (int(vote1) >= 100):
        names = []
        votes = []

        for i in range(int(members)):
            name = input("enter the names of the members \n")
            names.append(name)

        for i in range(int(vote1)):
            vote_random = (choice(names))
            votes.append(vote_random)
        y = max(set(votes), key=votes.count)
        print(y, "you are the canadict in the first place!")
        print("this is how much votes you got:", votes.count(y), '\n')

        for i in votes:
            for j in range(int(members)):
                x = max(set(votes), key=votes.count)
                print(x, "you are the canadict in the ", j + 1, " place")
                print("this is how much votes you got:", votes.count(x))
                while x in votes:
                    votes.remove(x)

    else:
        print("eror with your input")

