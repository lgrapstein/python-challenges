import random
import re

# Part 1
num = int(raw_input("Enter a number: "))
def times_table(num):
    for row in range(1, num+1):
        str = ''
        for column in range(1, num+1):
            str += '{:3} '.format(row * column)
        print str

times_table(num)

# Part 2
def palindrome(str):
    str = raw_input("\nType a word or phrase to find out if it is a palindrome: ")
    return str == str[::-1]

print palindrome(str)


# Part 3
RPS = {
	'r': 'Rock',
	'p': 'Paper',
	's': 'Scissors'
}

RULES = {
    's': 'p',  # scissors beats paper
    'p': 'r',  # paper beats rock
    'r': 's'   # rock beats scissors
}

# Called for tie breaker
def tie_breaker(player):
    computer = random.choice(RPS.keys())
    print('\t- Computer chose %s' % RPS[computer])
    # if player move beats computer
    if RULES[player] == computer:
        return 'Player', player, computer
    elif RULES[computer] == player:
        return 'Computer', computer, player
    else:
        return None, None, None


def play_rock_paper_scissors(rounds):
    player_wins = 0
    computer_wins = 0

    for r in range(rounds):
        print('\n\nRound %s/%s:' % ((r + 1), rounds))
        winner = None
        while not winner:
            player = raw_input("Rock (r), Paper (p), or Scissors (s): ").lower()
            # Checks the keys of that dictionary as a list ['r', 'p', 's'] and then checks if it's in the list
            while player not in RPS.keys():
                player = raw_input('Please try again: ').lower()
            else:
                print('\n\t- Player chose %s' % RPS[player])
            winner, winning_move, losing_move = tie_breaker(player)
            # if the winner is the player, add one to the player_wins, otherwise add one to computer_wins
            if winner:
                if winner == 'Player':
                    player_wins += 1
                else:
                    computer_wins += 1
                #Appending the round winners and the move that made them win to stats
                stats.append('Round %s: %s won\n   (%s beats %s)' % (r+1, winner, RPS[winning_move], RPS[losing_move]))
            else:
                print('\n* TIE BREAKER *')

    return player_wins, computer_wins


if __name__ == '__main__':
    stats = []
    rounds = 0
    # Checks the type first to avoid comparing if a string is less than 0 since you can't play negative or 0 rounds
    while type(rounds) != int or rounds < 1:
        try:
            rounds = int(raw_input("\nBest of how many rounds: "))
        except ValueError:
            print('Invalid number. Please try again!')
    print('\n\n--Playing %s rounds--' % rounds)
    player_wins, computer_wins = play_rock_paper_scissors(rounds)
    print('\n-----------Final Score-----------')
    #Print the winner for each round
    for st in (stats):
        print('%s' % (st))
    print('Player Wins: %s - Computer Wins: %s' % (player_wins, computer_wins))
    print('Overall Winner: YOU' if player_wins > computer_wins else 'Overall Winner: COMPUTER!' if computer_wins > player_wins else 'Overall Winner: TIE')
    print('---------------------------------\n')
