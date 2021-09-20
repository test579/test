import sys
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
    if 0 < num < 10:
        for i in range(1, num+1):
            print(int((10**i-1)/9)**2)
    else:
        print("The given number is out of range")

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


def _check_vowels(letter):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return True if letter in vowels else False


def _score_calculator(score, word, index):
    for i in range(len(word), index, -1):
        score += 1
    return score


def minion_game(word, pl1="Kevin", pl2="Stuart"):
    word = word.upper()
    score1 = 0
    score2 = 0
    for index, letter in enumerate(word):
        if _check_vowels(letter):
            score2 = _score_calculator(score2, word, index)
        else:
            score1 = _score_calculator(score1, word, index)
    if score1 > score2:
        return f"Win {pl1}: {score1}-{score2}!!!"
    elif score1 < score2:
        return f"Win {pl2}: {score1}-{score2}!!!"
    else:
        return f"{pl1}-{pl2}: {score1}-{score2} Draw!!!"
#print(minion_game("banana"))


# 3=====================================================================================================================

"""
EXERCISE: https://www.hackerrank.com/challenges/validating-credit-card-number/problem
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a ,  or .
► It must contain exactly  digits.
► It must only consist of digits (-).
► It may have digits in groups of , separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have  or more consecutive repeated digits.
"""
def _count_num(num):
    count = 0
    for i in str(num):
        if i == str(num)[0]:
            count += 1
        else:
            return count
    return count


def credit_card_validation(card_number):
    if len(card_number) != 16 and len(card_number) != 19:
        return "Invalid"
    elif int(card_number[0]) not in [4, 5, 6]:
        return "Invalid"
    elif len(card_number) == 19:
        if card_number[4] != "-" or card_number[9] != "-" \
                or card_number[14] != "-":
            return "Invalid"
    for i in card_number:
        if not i.isdigit() and i != "-":
            return "Invalid"
    changed_card = card_number.replace("-", "")
    while len(changed_card) > 0:
        num_count = _count_num(changed_card)
        if num_count >= 3:
            return "Invalid"
        changed_card = changed_card[num_count:]
    return "Valid"


print(credit_card_validation("4123456789123456"))
print(credit_card_validation("5123-4567-8912-3456"))
print(credit_card_validation("61234-567-8912-3456"))
print(credit_card_validation("4123356789123456"))
print(credit_card_validation("5133-3367-8912-3456"))
print(credit_card_validation("5123 - 3567 - 8912 - 3456"))
# 4=====================================================================================================================


"""
EXERCISE: https://www.hackerrank.com/challenges/compress-the-string/problem
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.
"""


def _count_number(num):
    count = 0
    value = None
    for i in str(num):
        if i == str(num)[0]:
            count += 1
            value = i
        else:
            return count, value
    return count, value


def compress_string(num):
    count = []
    while len(str(num)) > 0:
        count_num = _count_number(num)
        count.append(count_num)
        num = str(num)[count_num[0]:]
    return count

print(compress_string(43333222332211))