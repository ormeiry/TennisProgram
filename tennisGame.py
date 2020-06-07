from random import randrange


players = [['Novak Djokovic', '22/05/1987', 0, 0],
           ['Rafael Nadal', '03/06/1986', 0, 0],
           ['Roger Federer', '08/08/1981', 0, 0],
           ['Dominic Thiem', '03/09/1996', 0, 0],
           ['Kei Nishikori', '29/12/1989', 0, 0],
           ['Alexander Zverev', '20/04/1997', 0, 0],
           ['Stefanos Tsitsipas', '12/08/1998', 0, 0],
           ['Daniil Medvedev', '11/02/1996', 0, 0],
           ['Karen Khachanov', '21/05/1996', 0, 0],
           ['Fabio Fognini', '24/05/1987', 0, 0], ]


def addPoints(numOfPoints, numOfGames):
    wonGame = False
    if numOfPoints == 0 or numOfPoints == 15:
        numOfPoints += 15
    elif numOfPoints == 30:
        numOfPoints += 10
    else:
        numOfGames += 1
        wonGame = True
    return numOfPoints, numOfGames, wonGame


def playSet(pOneSets, pTwoSets, playerOne, playerTwo, games):
    pOneGames = 0
    pOnePoints = 0

    pTwoGames = 0
    pTwoPoints = 0

    playersInMatch = [playerOne, playerTwo]
    while (True):
        if (pOneGames - pTwoGames > 1 and pOneGames == 6 or pOneGames - pTwoGames >= 1 and pOneGames == 7):
            pOneSets += 1
            print(
                f"{playerOne[0]} has won the set, score is: {pOneSets}:{pTwoSets}")
            return pOneSets, pTwoSets, games
        elif (pTwoGames - pOneGames > 1 and pTwoGames == 6 or pTwoGames - pOneGames >= 1 and pTwoGames == 7):
            pTwoSets += 1
            print(
                f"{playerTwo[0]} has won the set, score is: {pOneSets}:{pTwoSets}")
            return pOneSets, pTwoSets, games
        else:
            if(pOnePoints == 0 and pTwoPoints == 0):
                print(f"Game {games}: ", end='')
            num = randrange(2)
            if playersInMatch[num] == playerOne:
                pOnePoints, pOneGames, wonGame = addPoints(
                    pOnePoints, pOneGames)
                if(wonGame):
                    print(f"game winner {playerOne[0]}")
                    pOnePoints = 0
                    pTwoPoints = 0
                    games += 1
                else:
                    print(f"{pOnePoints}-{pTwoPoints}, ",  end='')

            elif playersInMatch[num] == playerTwo:
                pTwoPoints, pTwoGames, wonGame = addPoints(
                    pTwoPoints, pTwoGames)
                if(wonGame):
                    print(f"game winner {playerTwo[0]}")
                    pOnePoints = 0
                    pTwoPoints = 0
                    games += 1
                else:
                    print(f"{pOnePoints}-{pTwoPoints}, ",  end='')


def doMatch(playerOne, playerTwo):
    playerOne[2] += 1
    playerTwo[2] += 1

    pOneSets = 0
    pTwoSets = 0
    sets = 1
    games = 1

    print(f"----{playerOne[0]} VS {playerTwo[0]}----")
    while(True):
        print(f"<set {sets}>")
        pOneSets, pTwoSets, games = playSet(
            pOneSets, pTwoSets, playerOne, playerTwo, games)
        sets += 1
        if pOneSets == 2:
            print(f"{playerOne[0]} has won the match!")
            playerOne[3] += 10
            return 1
        if pTwoSets == 2:
            print(f"{playerTwo[0]} has won the match!")
            playerTwo[3] += 10
            return 2


def randChoice(plist):
    index = randrange(len(plist))
    player = plist[index]
    return index, player


def doStage(pInTour):
    winnersList = []
    length = len(pInTour) + 1
    if (length == 3):
        winner = doMatch(pInTour[0], pInTour[1])
        winnersList.append(pInTour[winner-1])
        return winnersList
    while(len(pInTour) > 1):
        index, playerOne = randChoice(pInTour)
        pInTour.pop(index)

        index, playerTwo = randChoice(pInTour)
        pInTour.pop(index)

        winner = doMatch(playerOne, playerTwo)

        if (winner == 1):
            winnersList.append(playerOne)
        else:
            winnersList.append(playerTwo)
    return winnersList


def doTournament(plist, name):
    print(f"Welcome to the {name} Tournament!")
    print("Tournament players are: ")

    numOfplayers = randrange(2, 8, 2)
    if (numOfplayers == 6):
        numOfplayers = randrange(4, 9, 4)
    tourList = []
    while(True):
        randPlayer = randrange(len(plist))
        if (plist[randPlayer] not in tourList):
            tourList.append(plist[randPlayer])
        if (len(tourList) == numOfplayers):
            break

    for i in range(len(tourList)):
        if (i == len(tourList) - 1):
            print(f"{tourList[i][0]}")
        else:
            print(f"{tourList[i][0]}, ", end='')

    while(len(tourList) != 1):
        tourList = doStage(tourList)

    print(f"{tourList[0][0]} has won the tournament!!")
    tourList[0][3] += 10
    return tourList[0]


def printPlayer(player):
    pName = players[player][0]
    pBDate = players[player][1]
    pMatchesPlayed = players[player][2]
    pPointsWon = players[player][3]
    print('{:<30s}{:^20s}{:^20}{:^7}'.format(
        pName, pBDate, pMatchesPlayed, pPointsWon))
    return


def printPlayers(plist, num):
    dash = '-' * 80
    print(dash)
    print('{:<30s}{:^20s}{:^20s}{:>7s}'.format(
        'Full Name', 'Birth Date', 'Matches Played', 'Points'))
    print(dash)

    if (num > len(plist)):
        num = len(plist)
    elif(num < 0):
        for i in range(len(plist)+num, len(plist)):
            printPlayer(i)
        return
    for i in range(num):
        printPlayer(i)
    return


def sortPlayers(plist):
    plist.sort(key=lambda x: x[3])
    plist.reverse()
    return plist


def addPlayer():
    name = input("Enter name: ")
    bdate = input("Enter birthday[dd/mm/yyyy]: ")
    matchesPlayed = int(input("Enter number of matches played: "))
    pointsWon = int(input("Enter number of points: "))
    player = [name, bdate, matchesPlayed, pointsWon]
    players.append(player)
    return player


def removePlayer(plist):
    sortPlayers(plist)
    plist.pop()
    return plist


def menu(plist):
    dash = "-" * 80
    while(True):
        print("Tennis menu, choose a num then press the enter key:")
        print(dash)
        print("1. Print players table(for reverse order enter negative integer)")
        print("2. Print one Player by entering his table position")
        print("3. Add one Player to the table")
        print("4. Remove last place player")
        print("5. Sort the players table by points")
        print("6. Create a new tournament")
        print("7. Exit program")
        choice = int(input("Your Choice: "))
        print(dash)
        if choice == 1:
            howMany = int(input("How many players you want to see? "))
            print(dash)
            printPlayers(plist, howMany)
            print(dash)
        elif choice == 2:
            position = int(input("Enter the players position in table: "))
            print(dash)
            printPlayer(position - 1)
            print(dash)
        elif choice == 3:
            addPlayer()
        elif choice == 4:
            removePlayer(plist)
        elif choice == 5:
            sortPlayers(plist)
        elif choice == 6:
            tName = input("Enter Tournament name: ")
            doTournament(players, tName)
            print("-" * 50)
        else:
            break
        print("-" * 50)
    return


def main():
    menu(players)
    return "Done."


main()
