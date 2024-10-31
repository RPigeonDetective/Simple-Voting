x = ""
red = 0
blue = 0
TotalVoters = 0

def disregardVote():
    global TotalVoters
    TotalVoters += 1
    print("Your vote has been placed directly in the trash.")

while True:
    x = input("Please write in the candidate you wish to vote for: ")
    if x == "Red":
        red += 1
        TotalVoters += 1
        print("Red now has " + str(red) + " out of " + str(TotalVoters))
    elif x == "Blue":
        blue += 1
        TotalVoters += 1
        print("Blue now has " + str(blue) + " out of " + str(TotalVoters))
    else:
        disregardVote()
