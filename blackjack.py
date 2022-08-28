import random
from clear import clear
from art import logo

def blackjack():
    print(logo)
    player_cards = []
    dealer_cards = []
    player_total = 0
    dealer_total = 0
    dealer_print_total = f"Dealer's total is {dealer_total}."
    player_print_total = f"Your total is {player_total}."
    #Variables for consistant run through
    wins = int()
    loses = int()
    ties = int()
    start = input("Wanna play a hand? (Yes/No)\n").lower()

    
    while start:
        player_cards = []
        dealer_cards = []
        player_total = 0
        dealer_total = 0
        clear()
        print(logo)
        #Scoreboard
        print(f"Wins: {wins}")
        print(f"Loses: {loses}")
        print(f"Ties: {ties}")
        

        #Functions
        def eleven(whose_cards, whose_total):
            """Using card list and total card value to find if the ace needs to equal 1 instead of 11"""
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            if 11 in whose_cards and whose_total > 21:
                num11cards = cards.index(11)
                num11 = whose_cards.index(11)
                cards[num11cards] == 1
                whose_cards[num11] = 1
                whose_total -= 10

        def randcard(whose_cards, whose_total):
            """Adding a random card to the list and total value while checking the eleven condition"""
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            num_index = random.randrange(len(cards))
            card_dealt = cards[num_index]
            eleven(whose_cards, whose_total)
            whose_cards.append(card_dealt)


            
        
        #Creating card lists and total points
        while len(player_cards) < 2:
            randcard(player_cards, player_total)
        while len(dealer_cards) < 2:
            randcard(dealer_cards, dealer_total)
            
        for card in player_cards:
            player_total += card
        for card in dealer_cards:
            dealer_total += card

        #First deal
        print(f"\nYour cards: {player_cards} ({player_total} total)")
        print(f"Dealer's first card: {dealer_cards[0]}\n")
        if player_total == 21:
            print("Blackjack! You win!")
            print(dealer_print_total)
            wins += 1
        elif dealer_total == 21:
            print("Blackjack! Dealer wins!")
            print(player_print_total)
            loses += 1

            
        else:
            #Making Dealer hit if their cards add up to less than 16
            if dealer_total < 16 and len(dealer_cards) < 3:
                randcard(dealer_cards, dealer_total)
                dealer_total = 0
                for card in dealer_cards:
                    dealer_total += card
    
                
            #Hit or Pass function
            next_move = input("Hit or Pass? ").lower()
            if not next_move == "hit" and not next_move == "pass":
                print("Invalid selection.")
                next_move = input("Hit or Pass? ").lower()
            elif next_move == "hit":
                stop_loop = False
                while next_move == "hit" and not stop_loop:
                    stop_loop = False
                    next = 1
                    if player_total < 21 and dealer_total < 21 and next == 1:
                        randcard(player_cards, player_total)
                        player_total = 0
                        for card in player_cards:
                            player_total += card
                    if player_total == 21:
                        print("Blackjack! You win!")
                        print(dealer_print_total)
                        wins += 1
                        next_move = "pass"
                    elif dealer_total == 21:
                        print("Blackjack! Dealer wins!")
                        print(player_print_total)
                        loses += 1
                        next_move = "pass"
                    
                    else:    
                        #Making Dealer hit if their cards add up to less than 16
                        if dealer_total < 16 and len(dealer_cards) < 4:
                            randcard(dealer_cards, dealer_total)
                            dealer_total = 0
                            for card in dealer_cards:
                                dealer_total += card
                                
                            
                        print(f"\nYour cards: {player_cards} ({player_total} total)")
                        print(f"Dealer's first card: {dealer_cards[0]}\n")
                        if player_total < 21 and dealer_total < 21:
                            next_move = input("Hit or Pass? ").lower()
                        else:
                            stop_loop = True
                    
            #Game enders
            dealer_print_total = f"Dealer's total is {dealer_total}."
            player_print_total = f"Your total is {player_total}."
            
            if player_total > 21 and dealer_total > 21 or player_total == 21 and dealer_total == 21 or dealer_total == player_total:
                print("It's a tie!")
                print(player_print_total)
                print(dealer_print_total)
                ties += 1
            elif dealer_total < 21 and player_total < 21 and dealer_total > player_total:
                print("Dealer wins!")
                print(player_print_total)
                print(dealer_print_total)
                loses += 1
            elif dealer_total < 21 and player_total < 21 and player_total > dealer_total:
                print("Player wins!")
                print(player_print_total)
                print(dealer_print_total)
                wins += 1
            elif player_total == 21:
                print("Blackjack! You win!")
                print(dealer_print_total)
                wins += 1
            elif dealer_total == 21:
                print("Blackjack! Dealer wins!")
                print(player_print_total)
                loses += 1  
            elif player_total > 21:
                print(f"Bust! Your total is {player_total}.")
                print(dealer_print_total)
                loses += 1
            elif dealer_total > 21:
                print(f"Dealer busts! Dealer's total is {dealer_total}. You win!")
                print(player_print_total)
                wins += 1
                   

                    
        #Repeating/ending while loop
        start = input("\nPlay again? ").lower()
        if not start == "yes" and not start == "no":
            print("Invalid selection.")
            start = input("\nPlay again? ").lower()
        elif start == "yes":
            start = True
        else:
            start == False            
            print("Thank you for playing!")

    blackjack()

blackjack()
