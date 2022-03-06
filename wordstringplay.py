# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

openfile = open("../wordleweb/wordlists/words_alpha.txt", mode="r")
longdict = {}
for line in openfile:
    line = line.strip()
    if len(line) == 5:
        longdict[line] = 1
openfile.close()
print(len(longdict))
longdictlist = list(longdict.keys())
print(longdictlist[1:5])

openfile = open("../wordleweb/wordlists/common5letter.txt", mode="r")
commonwords = []
for line in openfile:
    line = line.strip()
    if len(line) == 5:
        commonwords.append(line)
openfile.close()

vowels = list("aeiou")


def generate_wordchain(onevowel=False):
    wordchain: list[str] = []
    lettersused = []
    totaltries = 0
    pickword = ""

    # main loop to start here
    for count in range(5):
        lettersused += list(pickword)
        for tries in range(5000):
            pickword = random.choice(commonwords)
            totaltries += 1
            ok = True
            vowelcount = 0
            for idx, l in enumerate(pickword):
                if l in vowels: vowelcount += 1
                if l in lettersused or l in pickword[idx + 1:]: ok = False
            if onevowel and vowelcount > 1: ok = False

            if ok: break

        # finished choosing a word

        if not ok: break  # would get here because ran out of tries
        wordchain.append(pickword)

    if len(wordchain) > 3: print(totaltries, wordchain)
    return wordchain


def generate_wordchain_londict(onevowel=False):
    wordchain: list[str] = []
    lettersused = []
    totaltries = 0
    pickword = ""

    # main loop to start here
    for count in range(6):
        lettersused += list(pickword)
        for tries in range(5000):
            pickword = random.choice(longdictlist)

            totaltries += 1
            ok = True
            vowelcount = 0
            for idx, l in enumerate(pickword):
                if l in vowels: vowelcount += 1
                if l in lettersused or l in pickword[idx + 1:]: ok = False
            if onevowel and vowelcount > 1: ok = False

            if ok: break

        # finished choosing a word

        if not ok: break  # would get here because ran out of tries
        wordchain.append(pickword)

    if len(wordchain) > 3: print(totaltries, wordchain)
    return wordchain


# londdict  version
bestresult = []
fourormore = 0
for big_tries in range(500):
    wordchain = generate_wordchain_londict(onevowel=True)
    if len(wordchain) > len(bestresult):
        bestresult = wordchain
    if len(wordchain) >= 4: fourormore += 1

print("**LONGDICT***BEST OVERALL**: ", bestresult)
print("4 or more:", fourormore)

# common word version
bestresult = []
fourormore = 0
for big_tries in range(500):
    wordchain = generate_wordchain(onevowel=True)
    if len(wordchain) > len(bestresult):
        bestresult = wordchain
    if len(wordchain) >= 4: fourormore += 1

print("**COMMONDICT -- BEST OVERALL**: ", bestresult)
print("4 or more:", fourormore)

# END
