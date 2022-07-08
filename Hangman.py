import random

word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure',
             'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle',
             'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard',
             'buzzing',
             'buzzwords',
             'caliph',
             'cobweb',
             'cockiness',
             'croquet',
             'crypt',
             'curacao',
             'cycle',
             'daiquiri',
             'dirndl',
             'disavow',
             'dizzying',
             'duplex',
             'dwarves',
             'embezzle',
             'equip',
             'espionage',
             'euouae',
             'exodus',
             'faking',
             'fishhook',
             'fixable',
             'fjord',
             'flapjack',
             'flopping',
             'fluffiness',
             'flyby',
             'foxglove',
             'frazzled',
             'frizzled',
             'fuchsia',
             'funny',
             'gabby',
             'galaxy',
             'galvanize',
             'gazebo',
             'giaour',
             'gizmo',
             'glowworm',
             'glyph',
             'gnarly',
             'gnostic',
             'gossip',
             'grogginess',
             'haiku',
             'haphazard',
             'hyphen',
             'iatrogenic',
             'icebox',
             'injury',
             'ivory',
             'ivy',
             'jackpot',
             'jaundice',
             'jawbreaker',
             'jaywalk',
             'jazziest',
             'jazzy',
             'jelly',
             'jigsaw',
             'jinx',
             'jiujitsu',
             'jockey',
             'jogging',
             'joking',
             'jovial',
             'joyful',
             'juicy',
             'jukebox',
             'jumbo',
             'kayak',
             'kazoo',
             'keyhole',
             'khaki',
             'kilobyte',
             'kiosk',
             'kitsch',
             'kiwifruit',
             'klutz',
             'knapsack',
             'larynx',
             'lengths',
             'lucky',
             'luxury',
             'lymph',
             'marquis',
             'matrix',
             'megahertz', 'microwave',
             'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize',
             'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche',
             'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz',
             'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk',
             'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome',
             'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'diphthong', 'twelfth',
             'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex',
             'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing',
             'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman',
             'yippee', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(stages)
chosen_word = random.choice(word_list)
result = ''

for word in chosen_word:
    result += '_'
results = list(result)
final_res = ''
n = -1

while lives > 0 and final_res != chosen_word:
    guess = input("\nGuess any letter: ").lower()

    if guess in final_res:
        print(f"You have already guessed {guess}.")

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            results[i] = guess
    final_res = ''.join(results)
    print(final_res)

    if guess not in chosen_word:
        print(f"You have guessed {guess} , that is not in the word. You lose a life.")
        print(stages[n])
        lives -= 1
        n -= 1

if final_res == chosen_word:
    print("You have won. Correctly guessed the word!")
else:
    print("All lives exhausted. You Lose!!")
    print(f"Correct word was {chosen_word}")
