import random
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

def is_first(word):
    return word[0] == word[0].capitalize() and not is_eol(word)

def is_last(word):
    return word[-1] in ".?!"

def is_eol(word):
    return word[-1] in ".?!"


def read_word(head, type):
    if not head:
        head = random.choice(list(dic.keys()))
    tails = dic[head].most_common(20)
    random.shuffle(tails)
    for t in tails:
        word = t[0]
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


# fn = "../test/corpus.txt"
fn = input()
text = ""
try:
    with open(fn, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"File {fn} not found")

tk = WhitespaceTokenizer()
tokens = tk.tokenize(text)

bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append((tokens[i], tokens[i+1]))

dic = {}
for k, v in bigrams:
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
                line += word + ' '
            else:
                loop = False
                j -= 1
                break
        while loop and not is_eol(word):
            word = read_word(word, 'last')
            line += word + ' '
        break
    if loop:
        print(line)
