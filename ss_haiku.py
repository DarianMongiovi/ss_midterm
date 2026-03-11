from ss_headline import word_list
import random
import re


def syllable_counter(word):
    word = word.lower()
    syllables = len(re.findall(r'[aeiouy]+', word))

    if word.endswith("e") and not word.endswith(("le", "ee")):
        syllables -= 1

    if word.endswith("le") and not word.endswith("tle"):
        syllables += 1

    return max(syllables, 1)

haiku_word_bank = word_list()

line_one = []
line_one_count = 0
line_one_limit = 5

line_two = []
line_two_count = 0
line_two_limit = 7

line_three = []
line_three_count = 0
line_three_limit = 5

while line_one_count < line_one_limit:
    if not line_one:
        first_word = random.choice(haiku_word_bank)
        line_one.append(first_word)
        line_one_count += syllable_counter(first_word)
    else:
        push = random.choice(haiku_word_bank)
        remaining_syllables = line_one_limit - sum(syllable_counter(i) for i in line_one)

        if syllable_counter(push) <= remaining_syllables and (not line_one or push != line_one[-1]):
            line_one.append(push)
            line_one_count += syllable_counter(push)

while line_two_count < line_two_limit:
    if not line_two:
        first_word = random.choice(haiku_word_bank)
        line_two.append(first_word)
        line_two_count += syllable_counter(first_word)
    else:
        push = random.choice(haiku_word_bank)
        remaining_syllables = line_two_limit - sum(syllable_counter(i) for i in line_two)

        if syllable_counter(push) <= remaining_syllables and (not line_two or push != line_two[-1]):
            line_two.append(push)
            line_two_count += syllable_counter(push)

while line_three_count < line_three_limit:
    if not line_three:
        first_word = random.choice(haiku_word_bank)
        line_three.append(first_word)
        line_three_count += syllable_counter(first_word)
    else:
        push = random.choice(haiku_word_bank)
        remaining_syllables = line_three_limit - sum(syllable_counter(i) for i in line_three)

        if syllable_counter(push) <= remaining_syllables and (not line_three or push != line_three[-1]):
            line_three.append(push)
            line_three_count += syllable_counter(push)

print(" ".join(line_one))
print(" ".join(line_two))
print(" ".join(line_three))
