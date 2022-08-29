import random
from art import logo2
from replit import clear

def deal_card():
    """Generates a random card and returns its value."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_dealt = random.choice(cards)
    return card_dealt

def calculate_score(card_list):
    """Calculates the total value of the cards in a list."""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if sum(card_list) > 21 and 11 in card_list:
        eleven_place = card_list.index(11)
        card_list[eleven_place] = 1
    return sum(card_list)

def compare(comp_score, user_score):
    """Compares the user score and dealer score to determine who won the round."""
    if comp_score == user_score:
        return "\nIt's a draw!"
    elif user_score == 0:
        return "\nBlackjack! You win!"
    elif comp_score == 0:
        return "\nBlackjack! You lose!"
    elif user_score > 21:
        return "\nYou lose!"
    elif comp_score > 21:
        return "\nYou win!"
    elif comp_score > user_score:
        return "\nYou lose!"
    elif user_score > comp_score:
        return "\nYou win!"
        
print(logo2)
play = input("Would you like to play? Yes/No ").lower()

while play == "yes":
    clear()
    print(logo2)
    user_cards = []
    computer_cards = []
    for num in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)
    print(f"\nYour cards: {user_cards} ({user_score} total)")
    print(f"Dealer's first card: {computer_cards[0]}\n")

    if user_score == 0 or comp_score == 0:
        print(compare(comp_score, user_score))
    else:
        keep_going = input("Do you want to draw another card? Yes/No ").lower()
        if keep_going == "yes":
            while keep_going:
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"\nYour cards: {user_cards} ({user_score} total)")
                print(f"Dealer's first card: {computer_cards[0]}\n")
                if user_score == 0 or user_score > 21 or comp_score == 0 or comp_score > 21:
                    keep_going = False
                else:
                    keep_going = input("Do you want to draw another card? Yes/No ").lower()
                    if keep_going == "no":
                        keep_going = False

        while comp_score < 17:
            computer_cards.append(deal_card())
            comp_score = calculate_score(computer_cards)

    print(compare(comp_score, user_score))
    print(f"Your score is {user_score}.")
    print(f"Dealer's score is {comp_score}.\n")
    
    play = input("Would you like to play again? Yes/No ").lower()
    if play == "no":
        print("Thanks for playing!")

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
