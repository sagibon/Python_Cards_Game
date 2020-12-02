from Project_Package.CardGame import CardGame
from Project_Package.card import DeckOfCards

DeckClass = DeckOfCards()
MainDeck = DeckClass.deck

Game1 = CardGame("Sagi", "Adi", 5)  # Intializing the game with two players and cards for each one
Game1.new_game()

print(f"{Game1.player1.PlayerName} : {Game1.player1.cardList} \n\
{Game1.player2.PlayerName} : {Game1.player2.cardList}")

# The game will last for 10 rounds
count_rounds = 0
for round in range(10):
    if len(Game1.player1.cardList) == 0 or len(Game1.player2.cardList) == 0:
        break
    count_rounds += 1
    Card1 = Game1.player1.get_card()  # getting a random card from the player1 deck
    Card2 = Game1.player2.get_card()  # getting a random card from the player2 deck

    print(f"{Game1.player1.PlayerName}'s card:{Card1}   VS   {Game1.player2.PlayerName}'s card:{Card2}")
    if Card1.who_higher(Card2) == Card1:  # Check who's card is higher and then take the cards - add to the other player
        print(f"{Game1.player1.PlayerName} won the round {round+1}")
        Game1.player2.add_card(Card1, Card2)

    elif Card1.who_higher(Card2) == Card2:
        print(f"{Game1.player2.PlayerName} won the round {round+1}")
        Game1.player1.add_card(Card1, Card2)
    else:                                  # Third option - Returns that its a tie
        print(Card1.who_higher(Card2))

print(f"final card deck {Game1.player1.PlayerName}: ", Game1.player1.cardList)  # Card decks in the end
print(f"final card deck {Game1.player2.PlayerName}: ", Game1.player2.cardList)
print(f"The winner is: {Game1.get_winner()}, after {count_rounds} rounds")  # Return the details of the winner
