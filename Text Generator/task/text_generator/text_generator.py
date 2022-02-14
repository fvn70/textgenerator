from nltk.tokenize import word_tokenize

# fn = "../test/corpus.txt"
fn = input()
text = ""
try:
    with open(fn, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"File {fn} not found")

# tokens = word_tokenize(text)
tokens = text.split()
print("Corpus statistics")
print(f"All tokens: {len(tokens)}")
print(f"Unique tokens: {len(set(tokens))}")

while True:
    cmd = input()
    if cmd == "exit":
        break
    try:
        idx = int(cmd)
        print(tokens[idx])
    except IndexError:
        msg = "Index Error. Please input an integer that is in the range of the corpus."
        print(msg)
    except (ValueError, TypeError):
        print("Type Error. Please input an integer.")
