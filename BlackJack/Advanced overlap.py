#not running is it too complicated? or does it loop or smthing?
import random
from tkinter import *
from tkinter import ttk
root = Tk()
root.state('zoomed')
chips = 100
hit = 0
dealer_hit=0
#print ('You start with %s chips' % chips)

while chips > 0:

    #put the whole thing in a while statement thats as long as they have more money then 0
    spades = ['2','3','4','5','6','7','8','9','10','jack','queen','king']#can't really be simplified
    clubs = ['2','3','4','5','6','7','8','9','10','jack','queen','king']
    hearts = ['2','3','4','5','6','7','8','9','10','jack','queen','king']
    dimonds = ['2','3','4','5','6','7','8','9','10','jack','queen','king']
    
    cards_chosen = []#list for the dictionary to get the values
    cards_chosen_with_suit = []#list to get the images with the suits
    display_cards=[]#could be wrong, just hoping you can add images to list and like save em that way
    
    index = 0
    index2=0


    def pick_four_cards():
        #trying to get random cards from a list and put them into a new list
        suit = random.randint(0,3)#randomizes the suit
        #card = random.randint(0,12)#randomizes the value oF the card !!!!!WHAT HAPPENS WHEN ITS INDEX 12 BUT THERE IS NO 12? CRASHES!!!!?~~~!
            #make a common list for every suit?
        if suit == 3:
            card = random.randint(0,len(spades)-1)
            card_and_suit = spades.pop(card) #removes the card and assigns a card
            cards_chosen_with_suit.append('s'+card_and_suit)
        elif suit == 2:
            card = random.randint(0,len(clubs)-1)
            card_and_suit = clubs.pop(card) #removes the card and assigns a card
            cards_chosen_with_suit.append('c'+card_and_suit)
        elif suit == 1:
            card = random.randint(0,len(hearts)-1)
            card_and_suit = hearts.pop(card) #removes the card and assigns a card
            cards_chosen_with_suit.append('h'+card_and_suit)
        else:
            card = random.randint(0,len(dimonds)-1)
            card_and_suit = dimonds.pop(card) #removes the card and assigns a card
            cards_chosen_with_suit.append('d'+card_and_suit)
        cards_chosen.append(card_and_suit)

        #dictionaries dont have a index so make a list of lists? nope
        #SO IM GOING TO HAVE TO make a list find a number in the list with a name then retreve the value by useing a dictionary
        #(list_of_cards)
        #i think a dicionalry wud be better cuz it we can have the same values, but then we'd have to make sure we don't get the same cards.
        #i think we should random to find the suit, then random to find number, and confirm that the next cards are not previesly chosen
        #i think its better to use a dictionary
        #or should i just remove the key for the list and write something that gives those keys values ie. 'jack' = 11
        
        #just for testing purpose
    while len(cards_chosen) < 10:
        pick_four_cards()

    integer=0
    integer2=0
    
    
    while index<10:

        x = cards_chosen_with_suit[index] + '.png'#its having issue cuz they are the same varible name?
        image = PhotoImage(file = 'D:\\Python\\Programs\\BlackJack\\Cards\\%s' % x)#the pixle width is 200 of the cards
        display_cards.append(image)
        index = index + 1

    display_cards2=[]#needs to display when requested to hit
    display_cards2.append(display_cards[0])
    def hit_case():
        display_cards2.append(display_cards[1+hit])

    hit_case()
    hit = hit + 1#just for testing
    hit_case()

    for thing3 in display_cards2:
        label = Label(image=thing3)
        label.place(x=300+integer,y=0)#works but no easy way to seperate the dealer's cards from your own
        integer=integer+70#5 cards takes up 480 pixles
    def player_is_done():
        for thing4 in display_cards2:
            if thing4 == display_cards2:
                display_cards.remove(thing4)
    #close should i calculate it before hand then pretend i don't know if we should hit
    label = Label(image=display_cards[5])
    label.place(x=950+integer2,y=0)#works but no easy way to seperate the dealer's cards from your own
    integer2=integer2+70

    hit_case()
    player_is_done()
    
    break #im having an issue showing multiple images at once maybe cuz i .pack
#do i need to mainloop.root???


