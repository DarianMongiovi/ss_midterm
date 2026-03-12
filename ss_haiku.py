from ss_headline import word_list
import random
import re


def syllable_counter(word):
    word = word.lower().strip(".:,;!?")
    if len(word) <= 3: return 1

    processing_word = word
    if word.startswith('y'):
        processing_word = word[1:]

    syllables = len(re.findall(r'[aeiouy]+', processing_word))

    if word.endswith("e") and not word.endswith(("le", "ee")):
        syllables -= 1
    if word.endswith(("ed", "es")):
        if not word.endswith(("ted", "ded", "ces", "ses", "xes", "zes", "ches", "shes")):
            syllables -= 1
    if word.endswith(("que", "gue")):
        syllables -= 1
    if word.endswith("ism"):
        syllables += 1

    add_one = ["ia", "io", "iu", "uo", "oa", "eo", "ao", "ua"]
    for pair in add_one:
        if pair in word:
            syllables += 1

    return max(syllables, 1)

def haiku_formatter():
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

    l1 = " ".join(line_one)
    l2 = " ".join(line_two)
    l3 = " ".join(line_three)

    return [l1, l2, l3]
