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

while True:
    cmd = input('\n')
    if cmd == "exit":
        break
    try:
        head = cmd
        print(f"Head: {head}")
        tails = dic[head].most_common()
        for t in tails:
            print(f"Tail: {t[0]} Count: {t[1]}")

    except KeyError:
        msg = "Key Error. The requested word is not in the model. Please input another word."
        print(msg)
