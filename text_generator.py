import random

from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

def check_line(line):
    line = line.split()
    for i in range(len(line)-2):
        trigram = " ".join(line[i:i+3])
    if trigram not in trigrams:
        print(" !!! ", trigram)

def is_first(word):
    return word[0][0] == word[0][0].capitalize() and not is_last(word) and not is_eol(word)

def is_last(word):
    return word.split()[0][-1] in punct

def is_eol(word):
    return word.split()[-1][-1] in punct

def read_word(head, type):
    if not head:
        head = random.choice(list(dic.keys()))
    tails = dic[head].most_common()
    for t in tails:
        word = head.split()[1] + ' ' + t[0]
        if type == 'first' and is_first(word):
            return word
        if type == 'middle' and not is_eol(word):
            return word
        if type == 'last':
            return word
    if type == 'first':
        return read_word('', type)
    else:
        return ''


# fn = "../test/corpus1.txt"
fn = input()
with open(fn, "r", encoding="utf-8") as f:
    text = f.read()

punct = {".", "?", "!"}
tk = WhitespaceTokenizer()
tokens = tk.tokenize(text)
trigrams = []
for i in range(len(tokens) - 2):
    trigrams.append((tokens[i] + ' ' + tokens[i+1], tokens[i+2]))
dic = {}
for k, v in trigrams:
    dic.setdefault(k, []).append(v)
dic = {k: Counter(dic[k]) for k in dic}

j = 0
while j < 10:
    j += 1
    line = ''
    word = ''
    loop = True
    while loop:
        word = read_word(word, 'first')
        line += word + ' '
        while len(line.split()) < 5:
            word = read_word(word, 'middle')
            if word:
                line += word.split()[1] + ' '
            else:
                loop = False
                j -= 1
                break
        while loop and not is_eol(word):
            word = read_word(word, 'last')
            line += word.split()[1] + ' '
        break
    if loop:
        print(line)
