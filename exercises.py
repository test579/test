# 1=====================================================================================================================

"""
EXERCISE: https://www.hackerrank.com/challenges/triangle-quest-2/problem
You are given a positive integer .
Your task is to print a palindromic triangle of size .
For example, a palindromic triangle of size  is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.
"""


def palindromic(num):
    for i in range(1, num):
        print(int((10**i-1)/9)**2)

# 2=====================================================================================================================


"""
EXERCISE: https://www.hackerrank.com/challenges/the-minion-game/problem
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""


def minion_game(word, player_1_name="Kevin", player_2_name="Stuart"):

    def check_vowels(letter):
        vowels = ['A', 'E', 'I', 'O', 'U']
        return True if letter in vowels else False

    def score_calculator(score, word, index):
        for i in range(len(word), index, -1):
            score += 1
        return score

    game_word = word.upper()
    player_1_score = 0
    player_2_score = 0
    for index, letter in enumerate(game_word):
        if check_vowels(letter):
            player_2_score = score_calculator(player_2_score, game_word, index)
        else:
            player_1_score = score_calculator(player_1_score, game_word, index)
    if player_1_score > player_2_score:
        return f"Win {player_1_name}: {player_1_score}-{player_2_score}!!!"
    elif player_1_score < player_2_score:
        return f"Win {player_2_name}: {player_1_score}-{player_2_score}!!!"
    else:
        return f"{player_1_name}-{player_2_name}: {player_2_score}-{player_2_score} Draw!!!"

#print(minion_game(player_1_name="Peter", word="ab"))