import random
from nltk.tokenize import WhitespaceTokenizer
from collections import Counter

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

for _ in range(10):
    head = random.choice(bigrams)[0]
    line = head
    for _ in range(9):
        tails = dic[head].most_common(10)
        tail = random.choice(tails)[0]
        line += ' ' + tail
        head = tail
    print(line)

