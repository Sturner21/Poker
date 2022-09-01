#Bring in the only outside library used
import numpy as np

val_dict = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
val = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen', 'King', 'Ace']
suit = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
scoresDict = {1:'Pair', 2:'Two pairs', 3:'Three of a kind', 4:'Straight', 5:'Flush', 6:'Full House', 7:'Four of a kind', 8:'Straight Flush', 9:'Royal Flush'}

def player(n):
    '''Creates hands for n number of players.'''
    #n = number of players

    dealt_cards = []
    players_hands = []
    flop_and_river = []

    #Create number of lists needed for amount of players playing
    for i in range(n):
        players_hands.append(list())

    #Give each player 2 cards to start (like in real poker)
    for num in range(len(players_hands)):

        while len(players_hands[num]) != 2:

            #Choose suit and and value randomly
            x = np.random.randint(len(val))
            y = np.random.randint(len(suit))

            #If the "card" has not been "dealt"...
            if f"{val[x]} of {suit[y]}" not in dealt_cards:

                #Then add it to the player's hands
                players_hands[num].append(f"{val[x]} of {suit[y]}")

                #And add it to the list of "dealt cards"
                dealt_cards.append(f"{val[x]} of {suit[y]}")

    #Simulate through flop, turn, and river
    while len(flop_and_river) != 5:

        #Continue to generate suits and values randomly
        x = np.random.randint(len(val))
        y = np.random.randint(len(suit))

        #If the "card" has not been "dealt"
        if f"{val[x]} of {suit[y]}" not in dealt_cards:

            #Add it to the intermediary list flop_and_river
            flop_and_river.append(f"{val[x]} of {suit[y]}")

            #Add it to the list of "dealt cards"
            dealt_cards.append(f"{val[x]} of {suit[y]}")

    #Iterate through the number of players being simulated
    for i in range(len(players_hands)):

        #Iterate through each card in the intermediary list
        for card in range(len(flop_and_river)):

            #Append each card from the flop_and_river list to each player's hand
            players_hands[i].append(flop_and_river[card])

    #Return the list of of hands, each containing the 7 usable cards for the respective player
    return players_hands

def draw():
    '''Bug testing function. Generates 7 random cards to test any function below'''

    #For this function I will not be providing documentation because it is not meant to be used in scenarios other than bug testing
    hand = []

    while len(hand) != 7:
        x = np.random.randint(len(val))
        y = np.random.randint(len(suit))
        if f"{val[x]} of {suit[y]}" not in hand:
            hand.append(f"{val[x]} of {suit[y]}")

    return hand

def handValuesList(h):
    '''Another bug testing function'''

    #Again, I will not be providing documentation on this because it is for bug testing purposes
    hand_vals = []

    for card in range(len(h)):

        x = h[card].split(" ")[0]
        hand_vals.append(val_dict[x])

    return hand_vals

def highCard(h):
    '''Given a hand "h" (a list of strings), this function will output the highest value card. Values are illustrated in "val_dict" above.'''

    #Create a list to store the integer values of each "card" to reference later
    hand_vals = []

    #Loop through each "card" in the "hand"
    for card in range(len(h)):

        #Grab string value of the card (ie. "Five" or "King")
        x = h[card].split(" ")[0]

        #Check value of card compared to val_dict to get numeric score and add it to the list of hand_vals
        hand_vals.append(val_dict[x])

    #Output the value of the highest "card"
    return max(hand_vals)

def checkTwos(h):
    '''Given a hand "h" (a list of strings), this function will 1) determine if there are 0, 1, or 2 pairs present and 2) output their values'''

    #Create list to store the values of each "card"
    hand_vals = []

    #Create a list to store the values that are pairs
    pairs = []

    #Loop through each card, giving it a value, and adding it to the list of hand_vals
    for card in range(len(h)):

        x = h[card].split(" ")[0]
        hand_vals.append(val_dict[x])

    #Iterate over each value of each "card"
    for value in range(len(hand_vals)):

        #If there is a pair present then add it to the list "pairs"
        if hand_vals.count(hand_vals[value]) == 2:

            #Only add it on condition that value isn't already in pairs
            if hand_vals[value] not in pairs:

                pairs.append(hand_vals[value])

    #If there's 3 pairs we want the 2 best
    if len(pairs) == 3:

        #We get the index of the worst pair
        index = pairs.index(min(pairs))
        
        #Then we remove the worst pair
        pairs.pop(index)

        #Then return the 2 best pairs
        return True, pairs, hand_vals
    
    #If there are 1 or 2 pairs then we want them
    elif 1 <= len(pairs) <= 2:

        return True, pairs, hand_vals

    #If none are present, then we return false
    else:
        return False, hand_vals

def checkThrees(h):
    '''Given a hand "h" (a list of strings), check if there are 3 cards of the same value'''

    #Create list of values to reference
    hand_vals = []

    #Create a list to store value of 3 of a kind
    threes = []

    #Loop through each card, assign it a value, and add it to the hand_vals list
    for card in range(len(h)):

        x = h[card].split(" ")[0]
        hand_vals.append(val_dict[x])

    #Check the hand's values
    for value in range(len(hand_vals)):

        #If there are 3 values present, save them for later
        if hand_vals.count(hand_vals[value]) == 3:

            #Prevent same value being added to the list "threes" multiple times
            if hand_vals[value] not in threes:

                threes.append(hand_vals[value])

    #If there's only one value that appears 3 times, return it
    if len(threes) == 1:
        return True, threes, hand_vals

    #If there are a pair of three's present, return the highest one
    elif len(threes) == 2:
        return True, threes, max(threes), hand_vals

    #If there are none present, return False
    else:
        return False, hand_vals

def checkFours(h):
    '''Given a hand "h" (a list of strings), determine if 4 cards have the same value'''

    #Create a list to add the values of each "card" to
    hand_vals = []

    #Create a list to store the value of a 4 of a kind
    fours = []

    #Loop through each card, assign it a value, and then add that value to the hand_vals list
    for card in range(len(h)):

        x = h[card].split(" ")[0]
        hand_vals.append(val_dict[x])

    #Loop through each value in the list of hand_vals
    for value in range(len(hand_vals)):

        #If 4 "cards" have the same value...
        if hand_vals.count(hand_vals[value]) == 4:

            #Add the value of the 4 of a kind to the list fours
            fours.append(hand_vals.count(hand_vals[value]))

            #Output that there is a four of a kind and what that value is
            return True, fours[0], hand_vals[value]

    #Otherwise, return false
    return False, h

def fullHouse(h):
    '''Given a hand "h" (a list of strings), determine if there is a three of a kind present and a pair of values, that different, present'''

    #First check if there is a 3 of a kind
    if checkThrees(h)[0] == True:

        #Then check if there is a pair of cards
        if checkTwos(h)[0] == True:

            #If both return True, then we know there must be a full house and we output what the value of each respective pair and 3 of a kind is
            return True, max(checkThrees(h)[1]), max(checkTwos(h)[1]), h
        
    #Otherwise we return false and no full house exists
    else:
        return False, h

def straight(h):
    '''Given a hand "h" (a list of strings), determine if there is a straight present'''

    #Create a list to add the values of the "cards" to
    hand_vals = []

    #Add the "value" of each "card" to a list
    for card in range(len(h)):
        x = h[card].split(" ")[0]
        hand_vals.append(val_dict[x])

    #Change the list so it is in order of lowest to highest from left to right
    hand_vals.sort()

    #Make the values from val_dict into a list
    val_dict_list = list(val_dict.values())

    #Index Error occurs if the lowest value we have in a hand is a Jack or higher, so we prevent this error from being raise by using the following try except block

    try:
    #Loop through 3 possible starting positions for straight
        for i in range(3):

            counter = 0

            #Start looking for the highest straight with 3rd "card" and loop to 2nd and 1st if no present
            start_index = val_dict_list.index(hand_vals[2-i])

            #Check if "cards" are in order
            for n in range(5):

                #Immediately break loop if any of the cards are out of order
                if hand_vals[2 - i + n] != val_dict_list[start_index + n]:
                    break
                else:
                    counter +=1

            #If the counter is 5 then a straight is present and we return the values of the hand,
            #what the function identified as the highest present straight, and True
            if counter == 5:
                return True, hand_vals[2-i], hand_vals

    #Prevent error from being thrown when running code
    except IndexError:
        return False, hand_vals, h


    #Exception to check when for when Ace is 1 in straight

    #Use the lowest 4 cards in the hand
    lst = hand_vals[0:4]
    #And add the Ace to the end
    lst.append(hand_vals[-1])

    #Checks if the lowest possible straight (Ace -> 5) is present
    if lst == [2, 3, 4, 5, 14]:
        return True, h

    #Otherwise return false
    return False, hand_vals, h

def flush(h):
    '''Given a hand "h" (a list of strings), determine if there is a flush present'''

    #Create list to track the values of the cards, if there are 5 or more present, to determine the best flush hand possible
    suited_hand_vals = []

    #Tracker to see how many cards of each suit are present
    suits = {'Clubs':0, 'Spades':0, 'Hearts':0, 'Diamonds':0}

    #Start loop to check suit of each "card"
    for card in range(len(h)):

        #Add 1 to whichever suit the "card" has 
        suits[h[card].split(" ")[2]] += 1

    #Loop through the values stored in the "suits" dictionary to check if any have a value of 5
    for type in range(len(list(suits))):

        #If a hand has 5 or more of the same suit, trigger a flush
        if suits[list(suits)[type]] >= 5:

            #Find highest value of card in flush
            for card in range(len(h)):

                #Check each card in hand to see if it is part of the suit
                if list(suits)[type] == h[card].split(" ")[2]:

                    #Add the values of all the cards to the list suited_hand_vals
                    x = h[card].split(" ")[0]
                    suited_hand_vals.append(val_dict[x])

            #Currently return the hand, how many of a suit are present, the max value of the suit, and True to symbolize that a flush was found
            return True, suits, h, max(suited_hand_vals)

    #Otherwise return False
    return False, h

def straightFlush(h):
    '''Given a hand "h" (a list of strings), determine if there is a straight flush present'''

    #List of "cards" that are part of the same suit (Only triggered when there are 5 or more cards of the same suit)
    suited_hand = []

    #List of the values of the "cards" that are suited
    suited_hand_vals = []

    suits = {'Clubs':0, 'Spades':0, 'Hearts':0, 'Diamonds':0}

    val_dict_list = list(val_dict.values())

    #Start loop to check suit of each "card"
    for card in range(len(h)):

        #Add 1 to whichever suit the "card" has 
        suits[h[card].split(" ")[2]] += 1

    #Loop through the values stored in the "suits" dictionary to check if any have a value of 5
    for type in range(len(list(suits))):

        #If a hand has 5 or more of the same suit, trigger a flush
        if suits[list(suits)[type]] >= 5:

            #Check each "card" to see if is part of the suit that has a flush
            for card in range(len(h)):

                #If the "card" is part of the suit then add it to list to check if straight is present
                if h[card].split(" ")[2] == list(suits)[type]:

                    suited_hand.append(h[card])

            #Find the value of each "card" that is in the flush and add it to "suited_hand_vals" list
            for card in range(len(suited_hand)):
                x = suited_hand[card].split(" ")[0]
                suited_hand_vals.append(val_dict[x])

            #Sort the list
            suited_hand_vals.sort()

            #Quickly check for this niche scenario
            lst = suited_hand_vals[0:4]
            lst.append(suited_hand_vals[-1])

            if lst == [2, 3, 4, 5, 14]:
                return True, h

            
            #Check if there is a straight present

            #Little bit of bug protection
            try:

                #Check the starting position for up to 7 "cards" that share the same suit
                for i in range(3):

                    counter = 0

                    start_index = val_dict_list.index(suited_hand_vals[-5 - i])

                    #See if the current set of 5 cards are in order
                    for n in range(5):

                        if suited_hand_vals[-5 - i + n] != val_dict_list[start_index + n]:
                            break
                        else:
                            counter +=1

                    #If there are 5 cards in order then return that there is a straight a flush
                    if counter == 5:
                        return True, suited_hand_vals, suited_hand

            #Bug protection
            except IndexError:

                return False, h

    #Otherwise return false
    else:
        return False, h

def royalFlush(h):
    '''Given a hand "h" (a list of strings), determine if the best hand, a royal flush, is present'''

    #Create a counter dictionary to check if a flush is present
    suits = {'Clubs':0, 'Spades':0, 'Hearts':0, 'Diamonds':0}

    #List for cards that are suited, acts as intermediary list
    suited_hand = []

    #List of values from the list suited_hands
    suited_hand_vals = []

    #Start loop to check suit of each "card"
    for card in range(len(h)):

        #Add 1 to whichever suit the "card" has 
        suits[h[card].split(" ")[2]] += 1

    #Loop through each type of suit to check if there a flush present
    for type in range(len(list(suits))):

        #If a hand has 5 or more of the same suit, trigger a flush
        if suits[list(suits)[type]] >= 5:
            
            #Check each "card" to see if is part of the suit that has a flush
            for card in range(len(h)):

                #If the "card" is part of the suit then add it to list to check if straight is present
                if h[card].split(" ")[2] == list(suits)[type]:

                    suited_hand.append(h[card])

            #Add each "card" value to the "suited_hand_vals" list
            for card in range(len(suited_hand)):
                x = suited_hand[card].split(" ")[0]
                suited_hand_vals.append(val_dict[x])

            #Put the list in order
            suited_hand_vals.sort()

            if suited_hand_vals[-5:] == [10, 11, 12, 13, 14]:
                return True, suited_hand
    
    #Otherwise return false
    return False, h

def bestHand(h):
    '''Take in ONE list of "cards" "h", and scores the hand based on what the best hand the cards can be'''

    #Score is the point values assigned to the player's hand to tell who has the best
    score = 0

    #Minimum is added to tell who has the highest card if there's a tie
    minimum = highCard(h) * .01

    #First check is to see if a flush exists and assign values if it does but not other version of flush exists in hand
    if flush(h)[0] == True:
        
        #If flush exists, then we want to check if it's a straight flush
        if straightFlush(h)[0] == True:

            #Lastly, if a straight flush exists, a royal flush might
            if royalFlush(h)[0] == True:

                score = 9

            score = 8 + minimum

        score = 5 + minimum

    #Check the next highest scoring option, four of a kind
    elif checkFours(h)[0] == True:

        #Add the value of the four of a kind to help distinguish whose 4 of a kind is higher
        score = 7 + (checkFours(h)[1] * .01)
    
    #Check for next highest option in straight
    elif straight(h)[0] == True:

        score = 4 + minimum

    elif fullHouse(h)[0] == True:

        #Score + the maximum values from the 3's
        score = 6 + (fullHouse(h)[1] *.01)

    #Check if three of a kind exists
    elif checkThrees(h)[0] == True:
        
        score = 3 + minimum

    elif checkTwos(h)[0] == True:
        
        if len(checkTwos(h)[1]) == 2:

            score = 2 + (max(checkTwos(h)[1]) * .01)
        
        else:

            score = 1 + (checkTwos(h)[1][0] * .01)

    else:
        
        score = minimum

    return score, h

def checkWin(hands):

    #List of scored hands to be returned
    bestPlayerHand = []

    #Add the values of each hand to list
    for n in range(len(hands)):

        bestPlayerHand.append(bestHand(hands[n])[0])

    #If there is only 1 hand with the highest value, return that
    if bestPlayerHand.count(max(bestPlayerHand)) == 1:

        return max(bestPlayerHand), bestPlayerHand

    #If there is more than one hand with equal value, find which hand should win
    elif bestPlayerHand.count(max(bestPlayerHand)) >= 2:
        
        return max(bestPlayerHand), bestPlayerHand.count(max(bestPlayerHand)), bestPlayerHand

    else:

        #Redundant conditional but is helpful for bug testing
        return bestPlayerHand



#Example simulation code
#print(checkWin(player(3)))