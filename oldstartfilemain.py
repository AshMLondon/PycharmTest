# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


openfile=open("../wordleweb/wordlists/words_alpha.txt",mode="r")
longdict={}
for line in openfile:
    line=line.strip()
    if len(line)==5:
           longdict[line]=1
openfile.close()

