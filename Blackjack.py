import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)
user_seq = []
comp_seq = []
score = 0
comp_score = 0
flag = True
def blackjack_user(score):
  user_seq.append(random.choice(cards))
  score = sum(user_seq)
  return score

def blackjack_comp(comp_score):
    comp_seq.append(random.choice(cards))
    comp_score = sum(comp_seq)
    return comp_score
for i in range(0, 2):
    score = blackjack_user(score)
    comp_score = blackjack_comp(comp_score)
print(f"Your cards: {user_seq}, current score: {score}")
print(f"Computer's first card: {comp_seq[0]}")
if score > 21 or comp_seq == [10, 11] or comp_seq == [11, 10] or user_seq == [10, 11] or user_seq == [11, 10]:
    print("You went over. You lose.")
    flag = False
elif comp_seq == [10, 11] or comp_seq == [11, 10]:
    print("You lose!! Opponent has Blackjack.")
    flag = False
elif (user_seq == [10, 11] or user_seq == [11, 10]) and (comp_seq != [10, 11] or comp_seq != [11, 10]):
    print("You win with a Blackjack.")
    flag = False
else:
    extra_card = ''
    while flag is not False:
        if 11 in user_seq and sum(user_seq) > 21:
            user_seq.remove(11)
            user_seq.append(1)
        extra_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if extra_card == 'y':
            score = blackjack_user(score)
            print(f"\nYour cards: {user_seq}, current score: {score}")
            print(f"Computer's first card: {comp_seq[0]}")
        if score > 21 or extra_card == 'n':
            flag = False
    while comp_score <= 16:
        comp_score = blackjack_comp(comp_score)
    print(f"\nYour final hand: {user_seq}, current score: {score}")
    print(f"Computer's final hand: {comp_seq} and final score: {comp_score}")
    if score == comp_score:
        print("\nDraw")
    elif score > 21:
        print("\nYou went over. You lose.")
    elif comp_score > 21:
        print("\nOpponent went over. You win.")
    elif score > comp_score:
        print("\nUser wins.")
    else:
        print("\nComputer wins.")
