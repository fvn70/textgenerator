
# fn = "../test/corpus.txt"
fn = input()
text = ""
try:
    with open(fn, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"File {fn} not found")

tokens = text.split()
bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append(tokens[i] + ' ' + tokens[i + 1])
print(f"Number of bigrams: {len(bigrams)}\n")

while True:
    cmd = input()
    if cmd == "exit":
        break
    try:
        idx = int(cmd)
        b = bigrams[idx].split()
        print(f"Head: {b[0]} Tail: {b[1]}")
    except IndexError:
        msg = "Index Error. Please input an integer that is in the range of the corpus."
        print(msg)
    except (ValueError, TypeError):
        print("Type Error. Please input an integer.")
